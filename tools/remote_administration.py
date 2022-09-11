# coding=utf-8
from base import ABHIG
from base import ABHIG TOOLS


class Stitch(ABHIG):
    TITLE = "Stitch"
    DESCRIPTION = "Stitch is a cross platform python framework.\n" \
                  "which allows you to build custom payloads\n" \
                  "For Windows, Mac and Linux."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nathanlopez/Stitch.git",
        "cd Stitch;sudo pip install -r lnx_requirements.txt"
    ]
    RUN_COMMANDS = ["cd Stitch;python main.py"]
    PROJECT_URL = "https://github.com/nathanlopez/Stitch"


class Pyshell(ABHIG):
    TITLE = "Pyshell"
    DESCRIPTION = "Pyshell is a Rat Tool that can be able to download & upload " \
                  "files,\n Execute OS Command and more.."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/knassar702/Pyshell.git;"
        "sudo pip install pyscreenshot python-nmap requests"
    ]
    RUN_COMMANDS = ["cd Pyshell;./Pyshell"]
    PROJECT_URL = "https://github.com/knassar702/pyshell"


class RemoteAdministrationTools(ABHIG TOOLS):
    TITLE = "Remote Administrator Tools (RAT)"
    TOOLS = [
        Stitch(),
        Pyshell()
    ]
