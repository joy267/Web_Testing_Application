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
from webdriver_manager.chrome import ChromeDriverManager


def configure_chrome_options_for_logging():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # If running headless
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})


def save_excel_sheet(sheet_name):
    Workbook.save(sheet_name)


def open_excel_sheet(sheet_name):
    openpyxl.load_workbook(sheet_name)


class Console_Logs:

    def __init__(self):
        self.driver = None
        self.webdriver_path = "C:\\Projects\\Python_Selenium\\Webdrivers\\chromedriver.exe"

        self.website_body = (By.TAG_NAME, "body")
        self.Selenium_Grid_URL = ("https://mamal_AROq6B:u1xogwyxP69m2VCwQjgo@hub-cloud.browserstack.com/wd"
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

    # def fetch_console_logs(self):
    #     if not hasattr(self.driver, 'get_log'):
    #         raise AttributeError("The WebDriver instance does not support 'get_log'.")
    #
    #     try:
    #         logs = self.driver.get_log("browser")
    #         return logs
    #     except Exception as e:
    #         raise RuntimeError(f"Failed to fetch browser logs: {str(e)}")

    def fetch_console_logs(self):
        # Check if the driver has the get_log method
        if not hasattr(self.driver, 'get_log'):
            return "Logging is not supported on this WebDriver instance."

        try:
            # Attempt to fetch the logs
            logs = self.driver.get_log('browser')
            return logs
        except Exception as e:
            # If logging is not supported, provide clear feedback
            if "not supported" in str(e).lower():
                return "Console logging is not supported in the current environment."
            else:
                # Other errors
                raise RuntimeError(f"Error while fetching console logs: {str(e)}")

    def close_browser(self):
        self.driver.quit()


