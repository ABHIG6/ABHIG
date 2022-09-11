# coding=utf-8
from base import ABHIG
from base import ABHIGTOOLS


class GoSpider(ABHIG):
    TITLE = "Gospider"
    DESCRIPTION = "Gospider - Fast web spider written in Go"
    INSTALL_COMMANDS = ["sudo go get -u github.com/jaeles-project/gospider"]
    PROJECT_URL = "https://github.com/jaeles-project/gospider"

    def __init__(self):
        super(GoSpider, self).__init__(runnable = False)


class WebCrawlingTools(ABHIGTOOLS):
    TITLE = "Web crawling"
    TOOLS = [GoSpider()]
