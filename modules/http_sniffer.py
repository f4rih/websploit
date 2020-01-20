import cmd
from scapy.all import *
from scapy.layers.http import HTTPRequest
from core import base

conf.verb = 0

class Main(base.Module):
    """Sniff HTTP traffic"""

    parameters = {"iface": "eth0"}
    completions = list(parameters.keys())

    def packet_handler(self, packet):
        if packet.haslayer(HTTPRequest):
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            ip = packet[IP].src
            method = packet[HTTPRequest].Method.decode()
            self.cp.success(text=f"[+] {ip} Requested {url} with {method}")
            if packet.haslayer(Raw) and method == "POST":
                self.cp.info(text=f"[+] Raw data: {packet[Raw].load}")

    def do_execute(self, line):
        """Execute current module"""
        sniff(filter="port 80", prn=self.packet_handler, iface=self.parameters['iface'], store=False)

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
