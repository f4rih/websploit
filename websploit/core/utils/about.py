import platform

def about():
    s_color = "\033[92m" if platform.system() != "Windows" else ""
    e_color = "\033[0m" if platform.system() != "Windows" else ""
    about = f"""{s_color}
    
            Websploit Framework
            Author : Fardin Allahverdinazhand
            Contact : 0x0ptim0us[~A~]Gmail.Com
            Twitter : @0x0ptim0us
            Codename : Reborn
            Project Github : https://github.com/websploit/websploit
            Other Projects : https://github.com/0x0ptim0us
            
    {e_color}"""
    print(about)