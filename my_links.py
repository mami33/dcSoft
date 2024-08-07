from configparser import ConfigParser

import mysql

config = ConfigParser()
config.sections()
"""
config["whatsAppLinks"] = {
"QR_CODE_CSS" : "#app > div > div.landing-wrapper > div.landing-window > div.landing-main > div > div > div._ak96 > div",
"QR_CODE_XPATH" : "//*[@id='app']/div/div[2]/div[3]/div[1]/div/div/div[2]/div",
"NEW_MESSAGE_BUTTON_CSS" : "#app > div > div.two._aigs > div._aigv._aigw > header > div._ak0z > div > span > div:nth-child(4) > div",
"NEW_MESSAGE_BUTTON_XPATH" : "//*[@id='app']/div/div[2]/div[3]/header/div[2]/div/span/div[4]/div",
"SEARCH_LINE_CSS" : "#app > div > div.two._aigs > div._aigu > div._aigv._aigw._aigx > span > div > span > div > div._ai07._ai01._akmh > div._ai04 > div._ai05 > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x6prxxf.x1k6rcq7.x1whj5v > p",
"SEARCH_LINE_XPATH" : "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p",
"USER_NOT_FIND_CSS" : "#app > div > div.two._aigs > div._aigu > div._aigv._aigw._aigx > span > div > span > div > div.x1n2onr6.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x6ikm8r.x1odjw0f.x1hc1fzr.x150wa6m > div > div > span",
"FINDED_USER_CSS" : "div.x10l6tqk:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)",
"FINDED_USER_XPATH" : "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div[2]",
"MESSAGE_TEXT_CSS" : "#main > footer > div._ak1k.xnpuxes.copyable-area > div > span:nth-child(2) > div > div._ak1r > div._ak1l > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x6prxxf > p",
"MESSAGE_TEXT_XPATH" : "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"
}
"""

config.read("whatsapp_config.ini")

QR_CODE_CSS = config["whatsAppLinks"]["QR_CODE_CSS"]
QR_CODE_XPATH = config["whatsAppLinks"]["QR_CODE_XPATH"]
NEW_MESSAGE_BUTTON_CSS = config["whatsAppLinks"]["NEW_MESSAGE_BUTTON_CSS"]
NEW_MESSAGE_BUTTON_XPATH = config["whatsAppLinks"]["NEW_MESSAGE_BUTTON_XPATH"]
SEARCH_LINE_CSS = config["whatsAppLinks"]["SEARCH_LINE_CSS"]
SEARCH_LINE_XPATH = config["whatsAppLinks"]["SEARCH_LINE_XPATH"]
USER_NOT_FIND_CSS =config["whatsAppLinks"]["USER_NOT_FIND_CSS"]
FINDED_USER_CSS = config["whatsAppLinks"]["FINDED_USER_CSS"]
FINDED_USER_XPATH = config["whatsAppLinks"]["FINDED_USER_XPATH"]
MESSAGE_TEXT_CSS = config["whatsAppLinks"]["MESSAGE_TEXT_CSS"]
MESSAGE_TEXT_XPATH = config["whatsAppLinks"]["MESSAGE_TEXT_XPATH"]

current_ver= config["version"]["ver"]


