import requests
from .version import version
from .output import CPrint


def update(where):
    cp = CPrint()
    try:
        res = requests.get("https://api.github.com/repos/websploit/websploit/releases/latest", timeout=2)
        if res.status_code == 200:
            response = res.json()
            git_version = response['tag_name']
            # check for new version
            if version != git_version:
                cp.success(text=f"New version available: {git_version}")
                cp.info(text=f"Download Link : https://api.github.com/repos/websploit/websploit/zipball/{git_version}")
            else:
                if where == "update_command":
                    cp.success(text="You are using the latest version of websploit.")
                elif where == "main_menu":
                    pass

        else:
            if where == "main_menu":
                pass
            elif where == "update_command":
                cp.warning("Error while updating! Check your internet connection!")
    except:
        pass
