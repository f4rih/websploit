from scapy.all import *
from core import base
from wifi import Cell

conf.verb = 0


class Main(base.Module):
    """Scan Wireless devices """

    parameters = {
        "iface": "wlan0"
    }
    completions = list(parameters.keys())

    def do_execute(self, line):
        """Execute current module"""
        try:
            print(f"{'SSID':^20}|{'MAC':^18}|{'Encrypted':^11}|{'Channel':^9}")
            print(f"{'_' * 20} {'_' * 18} {'_' * 11} {'_' * 11}")
            for wifi in Cell.all(self.parameters['iface']):
                print(f"{wifi.ssid:<20} {wifi.address:<18} {wifi.encrypted:<11} {wifi.channel:<9}")
        except Exception:
            self.cp.error(text=f"Error: Wireless interface {self.parameters['iface']} is busy or monitor mode enabled!")

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]


