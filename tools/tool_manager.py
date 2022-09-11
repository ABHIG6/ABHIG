# coding=utf-8
import os
from time import sleep

from base import ABHIG
from base import ABHIG TOOLS


class UpdateTool(ABHIG):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update ABHIG", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/ABHIG/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/ABHIG/;"
                  "mkdir ABHIG;"
                  "cd ABHIG;"
                  "git clone https://github.com/ABHIG6/ABHIG.git;"
                  "cd ABHIG;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(ABHIG):
    TITLE = "Uninstall ABHIG"
    DESCRIPTION = "Uninstall ABHIG TOOLS"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("ABHIG started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/ABHIG/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/ABHIG/;")
        print("\nABHIG Successfully Uninstalled..")
        print("  Happy Hacking..!!  ")
        sleep(1)


class ToolManager(ABHIG TOOLS):
    TITLE = "Update or Uninstall | ABHIG"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
