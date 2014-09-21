#!/usr/bin/env python
#
# WebSploit Framework Browser Autopwn module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
from core import wcolors
from core import help
from time import sleep
options =["192.168.1.1"]
def wmap():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Wmap" + wcolors.color.ENDC
		line_1 += " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:10] =='set target':
			options[0] = com[11:26]
			print "TARGET => ", options[0]
			wmap()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\t\t RQ\t Description"
			print "---------\t--------------\t\t\t----\t--------------"
			print "TARGET\t\t"+options[0]+"\t\t\tyes\tTarget IP Address"
			print ""
			wmap()
		elif com[0:2] =='os':
			os.system(com[3:])
			wmap()
		elif com[0:4] =='help':
			help.help()
			wmap()
		elif com[0:4] =='back':
			pass
		elif com[0:3] =='run':
			print(wcolors.color.YELLOW + "[*]Engine Has Been Started." + wcolors.color.ENDC)
			sleep(2)
			os.chdir('//tmp')
			check_tmp = os.listdir(os.curdir)
			if 'websploit_wmap.rc' in check_tmp:
				os.system('rm -rf websploit_wmap.rc')
			myfile = open ('websploit_wmap.rc', 'w')
			myfile.write('workspace -d websploit-wmap\n')
			myfile.write('workspace -a websploit-wmap\n')
			myfile.write('load wmap\n')
			myfile.write('sleep 3\n')
			myfile.write('wmap_targets -c\n')
			myfile.write('wmap_sites -a '+ options[0] + '\n')
			myfile.write('wmap_targets -t '+ options[0] + '\n')
			myfile.write('wmap_run -t\n')
			myfile.write('sleep 3\n')
			myfile.write('wmap_run -e\n')
			myfile.write('exit -y\n')
			myfile.close()
			os.system ('msfconsole -r websploit_wmap.rc')
		else:
			print "Wrong Command => ", com
			wmap()
	except(KeyboardInterrupt):
		print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
