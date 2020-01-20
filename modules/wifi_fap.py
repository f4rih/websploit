from scapy.all import *
from core import base

conf.verb = 0

class Main(base.Module):
    """Start Fake Access point (AP) """

    parameters = {
        "ssid": "websploit",
        "iface": "wlan0mon",
        "mac": str(RandMAC())

    }
    completions = list(parameters.keys())

    def do_execute(self, line):
        """Execute current module"""

        self.cp.success(text=f"Fake Access point started on {self.parameters['iface']}, SSID {self.parameters['ssid']} MAC {self.parameters['mac']}")
        self.cp.info(text="Press Ctrl+C for stop...")
        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=self.parameters['mac'], addr3=self.parameters['mac'])
        beacon = Dot11Beacon()
        essid = Dot11Elt(ID="SSID", info=self.parameters['ssid'], len=len(self.parameters['ssid']))
        rsn = Dot11Elt(ID='RSNinfo', info=(
            '\x01\x00'  # RSN Version 1
            '\x00\x0f\xac\x02'  # Group Cipher Suite : 00-0f-ac TKIP
            '\x02\x00'  # 2 Pairwise Cipher Suites (next two lines)
            '\x00\x0f\xac\x04'  # AES Cipher
            '\x00\x0f\xac\x02'  # TKIP Cipher
            '\x01\x00'  # 1 Authentication Key Managment Suite (line below)
            '\x00\x0f\xac\x02'  # Pre-Shared Key
            '\x00\x00'))  # RSN Capabilities (no extra capabilities)
        frame = RadioTap()/dot11/beacon/essid/rsn
        sendp(frame, inter=0.1, iface=self.parameters['iface'], loop=1)

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]