from .version import version
import platform

def logo():
    windows =  f"""
    ____    __    ____
    \   \  /  \  /   /     |    Welcome to Websploit 
     \   \/    \/   /      |    Version : {version} 
      \            /       |    https://github.com/websploit/websploit 
       \    /\    /        |    Author : Fardin Allahverdinazhand 
        \__/  \__/         |    Codename : Reborn 

    
    """
    not_windows =  f"""\033[92m
    ____    __    ____
    \   \  /  \  /   /     |   \033[95m Welcome to Websploit \033[92m
     \   \/    \/   /      |   \033[95m Version : {version} \033[92m
      \            /       |   \033[95m https://github.com/websploit/websploit \033[92m
       \    /\    /        |   \033[95m Author : Fardin Allahverdinazhand \033[92m
        \__/  \__/         |   \033[95m Codename : Reborn \033[92m

    \033[0m
    """
    return windows if platform.system() == "Windows" else not_windows
