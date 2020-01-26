import platform
import importlib.util
import sys


def check_dependencies():
    """Check system befor starting core"""
    modules = [
        'scapy',
        'requests'
    ]

    not_installed_modules = []

    for module in modules:
        spec = importlib.util.find_spec(module)
        if spec is None:
            print(f"[-] WARNING : `{module}` library not installed.")
            not_installed_modules.append(module)

    if not_installed_modules:
        install_string = ""
        for module in not_installed_modules:
            install_string += f"{module} "

        install_command = f"python3 -m pip install {install_string}"

        print("[+] Use below command for installing missing libraries.")
        print(f"[+] {install_command}")
        sys.exit()
