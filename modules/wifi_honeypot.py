#!/usr/bin/env python
#
# WebSploit Framework Wifi Honeypot (Fake Access Point) module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com
import os
import subprocess
from time import sleep
from core import help
from core import wcolors

options = ["wlan0", "FreeNet", "9", "a1:a2:a3:a4:a5:a6", "/home/wh_logs.txt", "mon0", "1"]

def wifi_honeypot():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Wifi_Honeypot" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:13] == 'set interface':
            options[0] = com[14:20]
            print "INTERFACE => ", options[0]
            wifi_honeypot()
        elif com[0:9] == 'set essid':
            options[1] = com[10:]
            print "ESSID => ", options[1]
            wifi_honeypot()
        elif com[0:11] == 'set channel':
            options[2] = com[12:14]
            print "CHANNEL => ", options[2]
            wifi_honeypot()
        elif com[0:7] == 'set mac':
            options[3] = com[8:25]
            print "MAC => ", options[3]
            wifi_honeypot()
        elif com[0:10] == 'set output':
            options[4] = com[11:]
            print "OUTPUT => ", options[4]
            wifi_honeypot()
        elif com[0:7] == 'set mon':
            options[5] = com[8:12]
            print "MON => ", options[5]
            wifi_honeypot()
        elif com[0:11] =='set encrypt':
            options[6] = com[12:13]
            print "ENCRYPT => ", options[6]
            wifi_honeypot()
        elif com[0:2] =='os':
            os.system(com[3:])
            wifi_honeypot()
        elif com[0:4] =='help':
            help.help()
            wifi_honeypot()
        elif com[0:4] =='back':
            pass
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t\t RQ\t Description"
            print "---------\t--------------\t\t\t----\t--------------"
            print "interface\t"+options[0]+"\t\t\t\tyes\tWireless Interface Name"
            print "essid\t\t"+options[1]+"\t\t\t\tyes\tFakeAP Essid"
            print "channel\t\t"+options[2]+"\t\t\t\tyes\tFakeAP Channel"
            print "mac\t\t"+options[3]+"\t\tyes\tFakeAP Mac Address"
            print "output\t\t"+options[4]+"\t\tyes\tLog File Location"
            print "mon\t\t"+options[5]+"\t\t\t\tyes\tMonitor Mod(default)"
            print "encrypt\t\t"+options[6]+"\t\t\t\tyes\tType Of Encryptions"
            print "\n"
            print "Numbers\t\t Encryptions"
            print "-------\t\t--------------"
            print "1\t\t Unencrypted"
            print "2\t\t wep"
            print "3\t\t wpa"
            print "4\t\t wpa2"
            print ""
            wifi_honeypot()
        elif com[0:3] == 'run':
            comm1= "xterm -e airbase-ng -a %s -c %s --essid %s %s > %s &" % (options[3], options[2], options[1], options[5], options[4])
            comm2= "xterm -e airbase-ng -a %s -c %d --essid %s -W 1 %s > %s &" % (options[3], options[2], options[1], options[5], options[4])
            comm3= "xterm -e airbase-ng -a %s -c %d --essid %s -W 1 -z 2 %s > %s &" % (options[3], options[2], options[1], options[5], options[4])
            comm4= "xterm -e airbase-ng -a %s -c %d --essid %s -W 1 -Z 4 %s > %s &" % (options[3], options[2], options[1], options[5], options[4])
            monit_mod_start= "airmon-ng start %s" % (options[1])
            print(wcolors.color.GREEN+"[*]Enable monitor mod on your interface [%s] ..."+wcolors.color.ENDC)% (options[0]),
            subprocess.Popen(monit_mod_start, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            print(wcolors.color.GREEN+" [OK]"+wcolors.color.ENDC)
            print(wcolors.color.GREEN+"[*]Creating Fake Access Point ..."+wcolors.color.ENDC),
            if options[6]==1:
                os.system(comm1)
            elif options[6]==2:
                os.system(comm2)
            elif options[6]==3:
                os.system(comm3)
            elif options[6]==4:
                os.system(comm4)
            else:
                print(wcolors.color.RED+"[!]Error : Encryption ID not Found!"+wcolors.color.ENDC)
                pass
            sleep(2)
            print(wcolors.color.GREEN+" [OK]"+wcolors.color.ENDC)
            wifi_honeypot()
        elif com[0:4]=='stop':
            os.system("killall xterm")
            os.system("killall airbase-ng")
            wifi_honeypot()
        else:
            print "Wrong Command => ", com
            wifi_honeypot()
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)