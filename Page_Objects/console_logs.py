import time

import openpyxl
import pandas as pd
from openpyxl.workbook import Workbook
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def configure_chrome_options_for_logging():
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'browser': 'ALL'}


def save_excel_sheet(sheet_name):
    Workbook.save(sheet_name)


def open_excel_sheet(sheet_name):
    openpyxl.load_workbook(sheet_name)


class Console_Logs:

    def __init__(self):
        self.driver = None
        self.webdriver_path = "C:\\Projects\\Python_Selenium\\Webdrivers\\chromedriver.exe"

        self.website_body = (By.TAG_NAME, "body")
        self.Selenium_Grid_URL = ("https://josh_hnveYE:V1axf7smmuAky3spdYNh@hub-cloud.browserstack.com/wd"
                                  "/hub")

    def create_excel_sheet(sheet_name):
        df = pd.DataFrame
        df.to_excel(sheet_name, index=False)

    def open_webdriver(self):
        options = Options()
        options.add_argument("--headless")  # for hide the web browser
        # s = Service(self.webdriver_path)
        self.driver = webdriver.Remote(command_executor=self.Selenium_Grid_URL, options=options)

    def maximize_window(self):
        self.driver.maximize_window()

    def open_website(self, url):
        self.driver.get(url)

    def implicit_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def scroll_website(self):
        locator_strategy, locator_value = self.website_body
        self.driver.find_element(locator_strategy, locator_value).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        self.driver.find_element(locator_strategy, locator_value).send_keys(Keys.PAGE_DOWN)

    def fetch_console_logs(self):
        return self.driver.get_log("browser")

    def close_browser(self):
        self.driver.quit()
