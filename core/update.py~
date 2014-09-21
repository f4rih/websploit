#!/usr/bin/env python
#
# WebSploit FrameWork Update Module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com

import os
import subprocess
from core import wcolors
from time import sleep

def update():
    print(wcolors.color.GREEN + "[*]Updating Websploit framework, Please Wait ..." + wcolors.color.ENDC)
    sleep(2)
    subprocess.Popen("git init", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
    sleep(2)
    os.system("git pull https://github.com/websploit/update.git")
    print(wcolors.color.GREEN + "[*]Update was completed successfully." + wcolors.color.ENDC)
    sleep(1)
