from configparser import ConfigParser
config = ConfigParser()
"""
config["whatsAppLinks"] = {
    "qr_code_css" : "#app > div > div.landing-wrapper > div.landing-window > div.landing-main > div > div > div._ak96 > div",
    "qr_code_xpath" : "//*[@id='app']/div/div[2]/div[3]/div[1]/div/div/div[2]/div",
    "new_message_button_css" : "#app > div > div.two._aigs > div._aigv._aigw > header > div._ak0z > div > span > div:nth-child(4) > div",
    "new_message_button_xpath" : "//*[@id='app']/div/div[2]/div[3]/header/div[2]/div/span/div[4]/div",
    "search_line_css" : "#app > div > div.two._aigs > div._aigu > div._aigv._aigw._aigx > span > div > span > div > div._ai07._ai01._akmh > div._ai04 > div._ai05 > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x6prxxf.x1k6rcq7.x1whj5v > p",
    "search_line_xpath" : "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p",
    "user_not_find_css" : "#app > div > div.two._aigs > div._aigu > div._aigv._aigw._aigx > span > div > span > div > div.x1n2onr6.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x6ikm8r.x1odjw0f.x1hc1fzr.x150wa6m > div > div > span",
    "finded_user_css" : "div.x10l6tqk:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)",
    "finded_user_xpath" : "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div[2]",
    "message_text_css" : "#main > footer > div._ak1k.xnpuxes.copyable-area > div > span:nth-child(2) > div > div._ak1r > div._ak1l > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x6prxxf > p",
    "message_text_xpath" : "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"
}
config["version"] = {
    "ver" : "1.0.0"
}
config["comp_name"] = {
    "name" : "deneme_firma",
    "number" : "numara_firmam"
}
config["excel_data"] = {
    "path" : "-",
    "chosen_columns" : "-,-,-,-"
}


with open('whatsapp_config.ini', 'w') as configfile:
  config.write(configfile)
"""

config.read('whatsapp_config.ini')
config.sections()

def config_get(section, key):
    return config.get(section, key)
def config_write(section, key, value):
    config.set(section, key, value)
    with open('whatsapp_config.ini', 'w') as configfile:
        config.write(configfile)


#config_write("excel_data", "path", "deneme1")



company_name = config["comp_name"]["name"]
company_cont = config["comp_name"]["number"]
excel_path = config["excel_data"]["path"]
chosen_columns = config["excel_data"]["chosen_columns"]