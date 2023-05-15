# Run WebSploit with 'Docker'

![docker](https://img.shields.io/badge/Docker-v19.03.12-blue?style=plastic&logo=docker)
![Maintainer](https://img.shields.io/badge/Maintainer-Equinockx-success?style=plastic&logo=terraform)

## Requeriments

- [X] Docker

## Usage Mode

Clone the repo from Github
```bash
git clone https://github.com/MoisesTapia/websploit
cd websploit
```

## Build the docker image

```bash
docker build -t websploit .
```
if you wanna put the tag to the image just add :<tag> like this websploit:v1.0

Run the container

```bash
docker run -dti --name websploit websploit:<tag> websploit 
```
## Build the network

```bash
docker network create security 
```

connect the container to the network

                        network container_name
```bash
docker network connect security websploit
```

## Execute websploit in container

```bash
docker exec -ti websploit websploit

➜  websploit git:(master) ✗ docker exec -ti websploit websploit

    ____    __    ____
    \   \  /  \  /   /     |    Welcome to Websploit 
     \   \/    \/   /      |    Version : 4.0.4 
      \            /       |    https://github.com/websploit/websploit 
       \    /\    /        |    Author : Fardin Allahverdinazhand 
        \__/  \__/         |    Codename : Reborn 

    
    
wsf > 
```
Exit the container 'CTRL + c'


## Testing 

```bash
➜  websploit git:(master) ✗ docker exec -ti websploit websploit

    ____    __    ____
    \   \  /  \  /   /     |    Welcome to Websploit 
     \   \/    \/   /      |    Version : 4.0.4 
      \            /       |    https://github.com/websploit/websploit 
       \    /\    /        |    Author : Fardin Allahverdinazhand 
        \__/  \__/         |    Codename : Reborn 

    
    
wsf > help

Commands
========
about  exit  help  show  update  use

wsf > update
[✔] You are using the latest version of websploit.
wsf > 
```
More commands

```bash
wsf > about

    
            Websploit Framework
            Author : Fardin Allahverdinazhand
            Contact : 0x0ptim0us[~A~]Gmail.Com
            Twitter : @0x0ptim0us
            Codename : Reborn
            Project Github : https://github.com/websploit/websploit
            Other Projects : https://github.com/0x0ptim0us
            
    
wsf > show
Modules             	Description         
--------------------	--------------------------
arp_spoof           	ARP Cache poisoning
http_sniffer        	Sniff HTTP traffic
scan_network        	Scan IP range for new devices 
scan_wifi           	Scan Wireless devices 
wifi_deauth         	Force device to disconnect from WIFI - De-authentication attack 
wifi_fap            	Start Fake Access point (AP) 
wifi_fap_spam       	Spamming Fake access points 


wsf > 
```