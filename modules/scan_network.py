from scapy.all import *
from core import base

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
        print(f"{'IP':16} {'MAC':18}")
        print(f"{'_'*16} {'_'*21}")
        for _, received in result:
            print(f"{received.psrc:20} {received.hwsrc}")

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]


