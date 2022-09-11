# coding=utf-8
import os
import socket
import subprocess
import webbrowser

from base import ABHIG
from base import ABHIGTOOLS
from base import clear_screen


class NMAP(ABHIG):
    TITLE = "Network Map (nmap)"
    DESCRIPTION = "Free and open source utility for network discovery and security auditing"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nmap/nmap.git",
        "sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def __init__(self):
        super(NMAP, self).__init__(runnable = True)


class Dracnmap(ABHIG):
    TITLE = "Dracnmap"
    DESCRIPTION = "Dracnmap is an open source program which is using to \n" \
                  "exploit the network and gathering information with nmap help."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Dracnmap.git",
        "cd Dracnmap && chmod +x dracnmap-v2.2-dracOs.sh  dracnmap-v2.2.sh"
    ]
    RUN_COMMANDS = ["cd Dracnmap;sudo ./dracnmap-v2.2.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Dracnmap"

#    def __init__(self):
#        super(Dracnmap, self).__init__(runnable = False)


class PortScan(ABHIG):
    TITLE = "Port scanning"

    def __init__(self):
        super(PortScan, self).__init__(installable = False)

    def run(self):
        clear_screen()
        target = input('Select a Target IP: ')
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])


class Host2IP(ABHIG):
    TITLE = "Host to IP "

    def __init__(self):
        super(Host2IP, self).__init__(installable = False)

    def run(self):
        clear_screen()
        host = input("Enter host name (e.g. www.google.com):-  ")
        ips = socket.gethostbyname(host)
        print(ips)


class XeroSploit(ABHIG):
    TITLE = "Xerosploit"
    DESCRIPTION = "Xerosploit is a penetration testing toolkit whose goal is to perform\n" \
                  "man-in-the-middle attacks for testing purposes"
    INSTALL_COMMANDS = [
        "git clone https://github.com/LionSec/xerosploit.git",
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://github.com/LionSec/xerosploit"


class RedHawk(ABHIG):
    TITLE = "RED HAWK (All In One Scanning)"
    DESCRIPTION = "All in one tool for Information Gathering and Vulnerability Scanning."
    INSTALL_COMMANDS = [
        "git clone https://github.com/Tuhinshubhra/RED_HAWK.git"]
    RUN_COMMANDS = ["cd RED_HAWK;php rhawk.php"]
    PROJECT_URL = "https://github.com/Tuhinshubhra/RED_HAWK"


class ReconSpider(ABHIG):
    TITLE = "ReconSpider(For All Scaning)"
    DESCRIPTION = "ReconSpider is most Advanced Open Source Intelligence (OSINT)" \
                  " Framework for scanning IP Address, Emails, \n" \
                  "Websites, Organizations and find out information from" \
                  " different sources.\n"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/bhavsec/reconspider.git",
        "sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd reconspider;python3 reconspider.py"]
    PROJECT_URL = "https://github.com/bhavsec/reconspider"

#    def __init__(self):
#        super(ReconSpider, self).__init__(runnable = False)


class IsItDown(ABHIG):
    TITLE = "IsItDown (Check Website Down/Up)"
    DESCRIPTION = "Check Website Is Online or Not"

    def __init__(self):
        super(IsItDown, self).__init__(
            [('Open', self.open)], installable = False, runnable = False)

    def open(self):
        webbrowser.open_new_tab("https://www.isitdownrightnow.com/")


class Infoga(ABHIG):
    TITLE = "Infoga - Email OSINT"
    DESCRIPTION = "Infoga is a tool gathering email accounts informations\n" \
                  "(ip, hostname, country,...) from different public source"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/Infoga.git",
        "cd Infoga;sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd Infoga;python3 infoga.py"]
    PROJECT_URL = "https://github.com/m4ll0k/Infoga"


class ReconDog(ABHIG):
    TITLE = "ReconDog"
    DESCRIPTION = "ReconDog Information Gathering Suite"
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/ReconDog.git"]
    RUN_COMMANDS = ["cd ReconDog;sudo python dog"]
    PROJECT_URL = "https://github.com/s0md3v/ReconDog"


class Striker(ABHIG):
    TITLE = "Striker"
    DESCRIPTION = "Recon & Vulnerability Scanning Suite"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Striker.git",
        "cd Striker && pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/s0md3v/Striker"

    def run(self):
        site = input("Enter Site Name (example.com) >> ")
        os.chdir("Striker")
        subprocess.run(["sudo", "python3", "striker.py", site])


class SecretFinder(ABHIG):
    TITLE = "SecretFinder (like API & etc)"
    DESCRIPTION = "SecretFinder - A python script for find sensitive data \n" \
                  "like apikeys, accesstoken, authorizations, jwt,..etc \n " \
                  "and search anything on javascript files.\n\n " \
                  "Usage: python SecretFinder.py -h"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/SecretFinder.git secretfinder",
        "cd secretfinder; sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/m4ll0k/SecretFinder"

    def __init__(self):
        super(SecretFinder, self).__init__(runnable = False)


class Shodan(ABHIG):
    TITLE = "Find Info Using Shodan"
    DESCRIPTION = "Get ports, vulnerabilities, informations, banners,..etc \n " \
                  "for any IP with Shodan (no apikey! no rate limit!)\n" \
                  "[X] Don't use this tool because your ip will be blocked by Shodan!"
    INSTALL_COMMANDS = ["git clone https://github.com/m4ll0k/Shodanfy.py.git"]
    PROJECT_URL = "https://github.com/m4ll0k/Shodanfy.py"

    def __init__(self):
        super(Shodan, self).__init__(runnable = False)


class PortScannerRanger(ABHIG):
    TITLE = "Port Scanner - rang3r"
    DESCRIPTION = "rang3r is a python script which scans in multi thread\n " \
                  "all alive hosts within your range that you specify."
    INSTALL_COMMANDS = [
        "git clone https://github.com/floriankunushevci/rang3r.git;"
        "sudo pip install termcolor"]
    PROJECT_URL = "https://github.com/floriankunushevci/rang3r"

    def run(self):
        ip = input("Enter Ip >> ")
        os.chdir("rang3r")
        subprocess.run(["sudo", "python", "rang3r.py", "--ip", ip])


class Breacher(ABHIG):
    TITLE = "Breacher"
    DESCRIPTION = "An advanced multithreaded admin panel finder written in python."
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/Breacher.git"]
    PROJECT_URL = "https://github.com/s0md3v/Breacher"
    
    def run(self):
        domain = input("Enter domain (example.com) >> ")
        os.chdir("Breacher")
        subprocess.run(["python3", "breacher.py", "-u", domain])

class InformationGatheringTools(ABHIGTOOLS):
    TITLE = "Information gathering tools"
    TOOLS = [
        NMAP(),
        Dracnmap(),
        PortScan(),
        Host2IP(),
        XeroSploit(),
        RedHawk(),
        ReconSpider(),
        IsItDown(),
        Infoga(),
        ReconDog(),
        Striker(),
        SecretFinder(),
        Shodan(),
        PortScannerRanger(),
        Breacher()
    ]
