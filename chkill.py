import os


def kill_chrome():
    try:
        os.system("taskkill /im chrome.exe")
        os.system("taskkill /im chrome.exe")
        os.system("taskkill /im chrome.exe")
    except Exception:
        print(Exception)
