from scapy.all import *
from websploit.core import base
import subprocess

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
            self.cp.green(f"{'SSID':<30}\t{'BSSID':^18}\t{'CHANNEL':^9}\t{'SIGNAL':^9}\t{'BARS':^8}\t{'SECURITY':^18}")
            result = self.scan()
            if result:
                for wifi in result:
                    self.cp.yellow(f"{wifi['SSID']:<30}\t {wifi['BSSID']:^18}\t {wifi['CHANNEL']:^9}\t {wifi['SIGNAL']:^9}\t {wifi['BARS']:^8}\t {wifi['SECURITY']:^18}")
        except Exception:
            self.cp.error(text=f"Error: Wireless interface {self.parameters['iface']} is busy or monitor mode enabled!")

    def scan(self):
        """Scan wifi with nmcli and parse output"""
        result = []
        output = subprocess.run(["nmcli", "-t", "-e", "yes","-f", "ssid,bssid,chan,signal,bars,security","dev","wifi"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        if output:
            # convert it to list
            list_output = output.split("\n")
            for info in list_output:
                # fix bssid escape char
                info = info.replace("\:", "-")
                try:
                    info = info.split(":")
                    result.append({"SSID":info[0], "BSSID": info[1], "CHANNEL": info[2], "SIGNAL": info[3], "BARS": info[4], "SECURITY": info[5]})
                except IndexError:
                    pass
        else:
            return None
        return result

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
