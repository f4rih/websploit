from scapy.all import *
from websploit.core import base

conf.verb = 0

class Main(base.Module):
    """Scan IP range for new devices """

    parameters = {
        "ip": "192.168.1.1/24"
    }
    completions = list(parameters.keys())

    def do_execute(self, line):
        """Execute current module"""
        # create arp packet
        arp = ARP(pdst=self.parameters['ip'])
        # set mac address for broadcasting
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        # stack them
        packet = ether/arp
        result = srp(packet, timeout=5)[0]
        self.cp.green(f"{'IP':<16}\t {'MAC':^15}")
        for _, received in result:
            self.cp.yellow(f"{received.psrc:<20} {received.hwsrc:^18}")

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]


