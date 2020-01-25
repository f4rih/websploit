from scapy.all import *


def get_mac(ip):
    """Get user MAC address"""
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src
    else:
        return None


def enable_ip_forward():
    """Enable ip forwarding on linux machine"""

    file_path = "/proc/sys/net/ipv4/ip_forward"
    try:
        with open(file_path) as file:
            if file.read() == 1:
                return True
        with open(file_path, "w") as file:
            print(1, file=file)
            return True
    except Exception:
        return False