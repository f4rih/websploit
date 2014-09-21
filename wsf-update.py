#!/usr/bin/env python
#
# WebSploit FrameWork Update Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import subprocess
import os
from core import wcolors

def update_websploit():
	print wcolors.color.GREEN + "[*]Updating Websploit framework, Please Wait ..." + wcolors.color.ENDC
	os.chdir("/usr/share/")
	try:
		subprocess.Popen("git clone https://github.com/websploit/websploit.git", shell=True)
	except Exception, e:
		print wcolors.color.RED + "[!] Update Failed."+ wcolors.color.ENDC
		pass

	print wcolors.color.GREEN + "[*]Update was completed successfully." + wcolors.color.ENDC
if __name__ == "__main__":
	update_websploit()