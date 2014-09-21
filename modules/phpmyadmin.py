#!/usr/bin/env python
#
# WebSploit Framework PHPMyAdmin Page Scanner module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

from time import sleep
from core import wcolors
from core import help
import httplib
import os
options =["http://google.com"]
def phpmyadmin():
	try:
		line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
		line_1 += ":"
		line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "PMA" + wcolors.color.ENDC
		line_1 += " > "
		com = raw_input(line_1)
		com = com.lower()
		if com[0:10] =='set target':
			options[0] = com[11:]
			print "TARGET => ", options[0]
			phpmyadmin()
		elif com[0:12] =='show options':
			print ""
			print "Options\t\t Value"
			print "---------\t--------------"
			print "TARGET\t\t"+options[0]
			print ""
			phpmyadmin()
		elif com[0:2] =='os':
			os.system(com[3:])
			phpmyadmin()
		elif com[0:4] =='help':
			help.help()
			phpmyadmin()
		elif com[0:4] =='back':
			pass
		elif com[0:3] =='run':
			options[0] = options[0].replace("http://", "")
			print(wcolors.color.GREEN + "[*] Your Target : " + options[0] + wcolors.color.ENDC)
			print(wcolors.color.BLUE + "[*]Loading Path List ... Please Wait ..." + wcolors.color.ENDC)
			sleep(2)
			paths = ['/phpMyAdmin/',
		'/phpmyadmin/',
		'/PMA/',
		'/admin/',
		'/dbadmin/',
		'/mysql/',
		'/myadmin/',
		'/phpmyadmin2/',
		'/phpMyAdmin2/',
		'/phpMyAdmin-2/',
		'/php-my-admin/',
		'/phpMyAdmin-2.2.3/',
		'/phpMyAdmin-2.2.6/',
		'/phpMyAdmin-2.5.1/',
		'/phpMyAdmin-2.5.4/',
		'/phpMyAdmin-2.5.5-rc1/',
		'/phpMyAdmin-2.5.5-rc2/',
		'/phpMyAdmin-2.5.5/',
		'/phpMyAdmin-2.5.5-pl1/',
		'/phpMyAdmin-2.5.6-rc1/',
		'/phpMyAdmin-2.5.6-rc2/',
		'/phpMyAdmin-2.5.6/',
		'/phpMyAdmin-2.5.7/',
		'/phpMyAdmin-2.5.7-pl1/',
		'/phpMyAdmin-2.6.0-alpha/',
		'/phpMyAdmin-2.6.0-alpha2/',
		'/phpMyAdmin-2.6.0-beta1/',
		'/phpMyAdmin-2.6.0-beta2/',
		'/phpMyAdmin-2.6.0-rc1/',
		'/phpMyAdmin-2.6.0-rc2/',
		'/phpMyAdmin-2.6.0-rc3/',
		'/phpMyAdmin-2.6.0/',
		'/phpMyAdmin-2.6.0-pl1/',
		'/phpMyAdmin-2.6.0-pl2/',
		'/phpMyAdmin-2.6.0-pl3/',
		'/phpMyAdmin-2.6.1-rc1/',
		'/phpMyAdmin-2.6.1-rc2/',
		'/phpMyAdmin-2.6.1/',
		'/phpMyAdmin-2.6.1-pl1/',
		'/phpMyAdmin-2.6.1-pl2/',
		'/phpMyAdmin-2.6.1-pl3/',
		'/phpMyAdmin-2.6.2-rc1/',
		'/phpMyAdmin-2.6.2-beta1/',
		'/phpMyAdmin-2.6.2-rc1/',
		'/phpMyAdmin-2.6.2/',
		'/phpMyAdmin-2.6.2-pl1/',
		'/phpMyAdmin-2.6.3/',
		'/phpMyAdmin-2.6.3-rc1/',
		'/phpMyAdmin-2.6.3/',
		'/phpMyAdmin-2.6.3-pl1/',
		'/phpMyAdmin-2.6.4-rc1/',
		'/phpMyAdmin-2.6.4-pl1/',
		'/phpMyAdmin-2.6.4-pl2/',
		'/phpMyAdmin-2.6.4-pl3/',
		'/phpMyAdmin-2.6.4-pl4/',
		'/phpMyAdmin-2.6.4/',
		'/phpMyAdmin-2.7.0-beta1/',
		'/phpMyAdmin-2.7.0-rc1/',
		'/phpMyAdmin-2.7.0-pl1/',
		'/phpMyAdmin-2.7.0-pl2/',
		'/phpMyAdmin-2.7.0/',
		'/phpMyAdmin-2.8.0-beta1/',
		'/phpMyAdmin-2.8.0-rc1/',
		'/phpMyAdmin-2.8.0-rc2/',
		'/phpMyAdmin-2.8.0/',
		'/phpMyAdmin-2.8.0.1/',
		'/phpMyAdmin-2.8.0.2/',
		'/phpMyAdmin-2.8.0.3/',
		'/phpMyAdmin-2.8.0.4/',
		'/phpMyAdmin-2.8.1-rc1/',
		'/phpMyAdmin-2.8.1/',
		'/phpMyAdmin-2.8.2/',
		'/sqlmanager/',
		'/mysqlmanager/',
		'/p/m/a/',
		'/PMA2005/',
		'/pma2005/',
		'/phpmanager/',
		'/php-myadmin/',
		'/phpmy-admin/',
		'/webadmin/',
		'/sqlweb/',
		'/websql/',
		'/webdb/',
		'/mysqladmin/',
		'/mysql-admin/',]
			try:
				for path in paths:
					path = path.replace("\n", "")
					conn = httplib.HTTPConnection(options[0])
					conn.request("GET", path)
					res = conn.getresponse()
					if(res.status==200):
						print(wcolors.color.BOLD + wcolors.color.GREEN + "[%s] ... [%s %s]" % (path, res.status, res.reason) + wcolors.color.ENDC)
					else:
						print(wcolors.color.YELLOW + "[%s] ... [%s %s]" % (path, res.status, res.reason) + wcolors.color.ENDC)
			except(KeyboardInterrupt, SystemExit):
				print(wcolors.color.RED + "[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
		else:
			print "Wrong Command => ", com
			phpmyadmin()
	except(KeyboardInterrupt, SystemExit):
		print(wcolors.color.RED + "[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)

