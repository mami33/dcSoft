import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from my_links import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

users = {"+905308461427": "tuçi", "45456465465": "deneme", "+905306565027": "bana"}
users_cant_find = {}



def startDriver():
    app_data_dir = os.getenv('LOCALAPPDATA')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(r'--user-data-dir=' + app_data_dir + '\\Google\\Chrome\\User Data')
    chrome_options.add_argument(r'--profile-directory=Profile 2')
    my_driver_path = os.getcwd() + "\\chromedriver.exe"
    ser = Service(executable_path=my_driver_path)
    driver = webdriver.Chrome(service=ser, options=chrome_options)
    driver.get("https://web.whatsapp.com/")
    time.sleep(2)
    assert "WhatsApp" in driver.title
    return driver



def user_cant_find(name: str, mmessage: str):
    data = [(name, mmessage)]
    users_cant_find.update(data)


def qr_login(driver):
    wait = WebDriverWait(driver, 30)
    try:
        wait.until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, QR_CODE_CSS)))
        return True
    except NoSuchElementException:
        return False
    except TimeoutException:
        return False


def user_not_found(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, USER_NOT_FIND_CSS)
        return False
    except NoSuchElementException:
        return True




def send_message(driver,number, message):

    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ESCAPE)
    actions.perform()
    actions.send_keys(Keys.ESCAPE)
    actions.perform()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, NEW_MESSAGE_BUTTON_CSS))).click()
    driver.find_element(By.CSS_SELECTOR, SEARCH_LINE_CSS).send_keys(number)
    time.sleep(1.5)
    if user_not_found(driver):
        actions.send_keys(Keys.ENTER)
        actions.perform()
        driver.find_element(By.CSS_SELECTOR, MESSAGE_TEXT_CSS).send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(0.5)
    else:
        print("User Not Found")
        data = [(number, message)]
        users_cant_find.update(data)

def close_driver(driver):
    driver.close()
    driver.quit()

if __name__ == "__main__":

    send_message("530656502sdf7","123")


