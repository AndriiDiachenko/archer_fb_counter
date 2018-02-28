from selenium import webdriver

import os
import platform


def select_driver():
    chrome_options = webdriver.ChromeOptions()

    # Start browser in incognito mode
    chrome_options.add_argument("--incognito")

    # Block Web App notifications
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # Find OS and select a Driver
    if str(platform.system()).lower() == 'windows':
        driver_location = os.path.abspath('chromedriver.exe').replace('\\', '/').replace('/tests', '/drivers')
        driver = webdriver.Chrome(executable_path=driver_location, chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


class StartDriver(object):
    def __init__(self):
        self.driver = select_driver()

    def start(self):
        driver = self.driver
        driver.implicitly_wait(5)
        return driver
