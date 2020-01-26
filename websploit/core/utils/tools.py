from scapy.all import *
import random


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

def get_fake_mac():
    file_path = os.path.join(os.path.dirname(__file__), 'fake_mac')
    with open(file_path) as file:
        mac_list = file.readlines()
        random_mac = random.choice(mac_list)
        random_mac = random_mac.strip("\n")
        random_mac = random_mac.strip()
        return random_mac

def get_fake_name():
    file_path = os.path.join(os.path.dirname(__file__), 'fake_names')
    with open(file_path) as file:
        name_list = file.readlines()
        random_name = random.choice(name_list)
        random_name = random_name.strip("\n")
        random_name = random_name.strip()
        return random_name
