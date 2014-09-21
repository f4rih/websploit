#!/usr/bin/env python
#
#Websploit FrameWork Database Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

from core import wcolors
from time import sleep
def modules_database():
    print ""
    print (wcolors.color.BLUE + "Web Modules\t\t\tDescription" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "web/apache_users\t\tScan Directory Of Apache Users"
    print "web/dir_scanner\t\t\tDirectory Scanner"
    print "web/wmap\t\t\tInformation Gathering From Victim Web Using (Metasploit Wmap)"
    print "web/pma\t\t\t\tPHPMyAdmin Login Page Scanner"
    print "web/cloudflare_resolver\t\tCloudFlare Resolver"
    print "\n"
    print (wcolors.color.BLUE + "Network Modules\t\t\tDescription" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "network/arp_dos\t\t\tARP Cache Denial Of Service Attack"
    print "network/mfod\t\t\tMiddle Finger Of Doom Attack"
    print "network/mitm\t\t\tMan In The Middle Attack"
    print "network/mlitm\t\t\tMan Left In The Middle Attack"
    print "network/webkiller\t\tTCP Kill Attack"
    print "network/fakeupdate\t\tFake Update Attack Using DNS Spoof"
    print "network/arp_poisoner\t\tArp Poisoner"
    print "\n"
    print (wcolors.color.BLUE + "Exploit Modules\t\t\tDescription" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "exploit/autopwn\t\t\tMetasploit Autopwn Service"
    print "exploit/browser_autopwn\t\tMetasploit Browser Autopwn Service"
    print "exploit/java_applet\t\tJava Applet Attack (Using HTML)"
    print "\n"
    print (wcolors.color.BLUE + "Wireless / Bluetooth Modules\tDescription" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "-------------------\t\t---------------------" + wcolors.color.ENDC)
    print "wifi/wifi_jammer\t\tWifi Jammer"
    print "wifi/wifi_dos\t\t\tWifi Dos Attack"
    print "wifi/wifi_honeypot\t\tWireless Honeypot(Fake AP)"
    print "wifi/mass_deauth\t\tMass Deauthentication Attack"
    print "bluetooth/bluetooth_pod\t\tBluetooth Ping Of Death Attack"
    print "\n"
