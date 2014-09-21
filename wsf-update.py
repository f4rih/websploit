#!/usr/bin/env python
#
# WebSploit FrameWork Update Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import subprocess
import os
from core import wcolors

def update_websploit():
	os.chdir("/tmp")
	subprocess.Popen("mkdir test", shell=True)


if __name__ == "__main__":
	update_websploit()