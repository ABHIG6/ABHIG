# coding=utf-8
from base import ABHIG
from base import ABHIG TOOLS


class KnockMail(ABHIG):
    TITLE = "Knockmail"
    DESCRIPTION = "KnockMail Tool Verify If Email Exists"
    INSTALL_COMMANDS = [
        "git clone https://github.com/heywoodlh/KnockMail.git",
        "cd KnockMail;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd KnockMail;python3 knockmail.py"]
    PROJECT_URL = "https://github.com/heywoodlh/KnockMail"


class EmailVerifyTools(ABHIG TOOLS):
    TITLE = "Email Verify tools"
    TOOLS = [KnockMail()]
    
