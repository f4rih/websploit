#!/usr/bin/env python
#
# WebSploit Framework CloudFlare Resolver module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com
import os
import socket
from core import wcolors
from core import help
from time import sleep

options = ["google.com"]
def cloudflare_resolver():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "CloudFlare Resolver" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:10] =="set target":
            options[0]=com[11:]
            print "TARGET => ", options[0]
            cloudflare_resolver()
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t RQ\t Description"
            print "---------\t--------------\t\t----\t--------------"
            print "Target\t\t"+options[0]+"\t\tyes\tTarget Address"
            cloudflare_resolver()
        elif com[0:2] =='os':
            os.system(com[3:])
            cloudflare_resolver()
        elif com[0:4] =='help':
            help.help()
            cloudflare_resolver()
        elif com[0:4] =='back':
            pass
        elif com[0:3] =='run':
            sub = ('mail', 'webmail', 'email', 'direct-connect-mail',
'direct', 'direct-connect', 'cpanel', 'ftp', 'forum', 'blog',
'm', 'dev', 'record', 'ssl', 'dns', 'help', 'ns', 'ns1', 'ns2',
'ns3', 'ns4', 'irc', 'server', 'status', 'status', 'portal', 'beta',
'admin', 'imap', 'smtp')
            try:
                orgip = socket.gethostbyname(options[0])
                print "[-------------------------]"
                print "[+] Default IP Address : %s"%orgip
                print "[-------------------------]"
            except(socket.gaierror):
                print "[-] Error : Host is Down !"
            for i in sub:
                host = i+'.'+options[0]
                try:
                    ip = socket.gethostbyname(host)
                    print "[+] %s : %s"%(host, ip)
                except(socket.gaierror):
                    print "[-] %s : N/A"%host
            cloudflare_resolver()
        else:
            print "Wrong Command =>" + com
    except(KeyboardInterrupt):
        print "\n[!] Operation Stoped By User."