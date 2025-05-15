from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Page_Speed:

    def __init__(self):
        self.wait = None
        self.driver = None
        self.webdriver_path = "C:\\Projects\\Python_Selenium\\Webdrivers\\chromedriver.exe"
        self.locator_of_input_field_pagespeed_insights = (By.XPATH, "//input[@inputmode='url']")
        self.click_button_locator = (By.XPATH, "//span[text()='Analyze']")
        self.wait_element = (By.XPATH, "//div[@class='lh-exp-gauge__svg-wrapper']")
        self.locator_of_mobile_device = (By.XPATH, "//button[@id='mobile_tab']/span[1]/span[1]")
        self.locator_of_mobile_performance = (By.XPATH, "//div[@class='lh-scores-header']/a[1]/div[2]")
        self.locator_of_mobile_accessibility = (By.XPATH, "//div[@class='lh-scores-header']/a[2]/div[2]")
        self.locator_of_mobile_best_practices = (By.XPATH, "//div[@class='lh-scores-header']/a[3]/div[2]")
        self.locator_of_mobile_seo = (By.XPATH, "//div[@class='lh-scores-header']/a[4]/div[2]")
        self.locator_of_mobile_first_contentful_paint = (By.XPATH, "//div[@id='first-contentful-paint']/div[1]/div[2]")
        self.locator_of_mobile_largest_contentful_paint = (By.XPATH, "//div[@id='largest-contentful-paint']/div["
                                                                     "1]/div[2]")
        self.locator_of_mobile_total_blocking_time = (By.XPATH, "//div[@id='total-blocking-time']/div[1]/div[2]")
        self.locator_of_mobile_cumulative_layout_shift = (
            By.XPATH, "//div[@id='cumulative-layout-shift']/div[1]/div[2]")
        self.locator_of_mobile_speed_index = (By.XPATH, "//div[@id='speed-index']/div[1]/div[2]")
        self.locator_of_desktop_device = (By.XPATH, "//button[@id='desktop_tab']/span[1]/span[1]")
        self.locator_of_switching_desktop_tab = (By.XPATH, "//button[@id='desktop_tab']")
        self.locator_of_desktop_performance = (By.XPATH, "//div[@class='lh-scores-header']/a[1]/div[2]")
        self.locator_of_desktop_accessibility = (By.XPATH, "//div[@class='lh-scores-header']/a[2]/div[2]")
        self.locator_of_desktop_best_practices = (By.XPATH, "//div[@class='lh-scores-header']/a[3]/div[2]")
        self.locator_of_desktop_seo = (By.XPATH, "//div[@class='lh-scores-header']/a[4]/div[2]")
        self.locator_of_desktop_first_contentful_paint = (By.XPATH, "//div[@id='first-contentful-paint']/div[1]/div[2]")
        self.locator_of_desktop_largest_contentful_paint = (By.XPATH, "//div[@id='largest-contentful-paint']/div["
                                                                      "1]/div[2]")
        self.locator_of_desktop_total_blocking_time = (By.XPATH, "//div[@id='total-blocking-time']/div[1]/div[2]")
        self.locator_of_desktop_cumulative_layout_shift = (By.XPATH, "//div[@id='cumulative-layout-shift']/div["
                                                                     "1]/div[2]")
        self.locator_of_desktop_speed_index = (By.XPATH, "//div[@id='speed-index']/div[1]/div[2]")
        self.data_list = []
        self.Selenium_Grid_URL = ("https://josh_hnveYE:V1axf7smmuAky3spdYNh@hub-cloud.browserstack.com/wd""/hub")

    def open_webdriver(self):
        options = Options()
        options.add_argument("--headless")  # for hide the web browser
        # s = Service(self.webdriver_path)
        self.driver = webdriver.Remote(command_executor=self.Selenium_Grid_URL, options=options)

    def maximize_window(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def open_pagespeed_insights(self, url):
        self.driver.get(url)

    def accept_cookies(self):
        self.driver.find_element(By.XPATH, "//button/span[text()='Ok, Got it.']").click()

    def implicit_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def explicit_wait(self, timeout):
        try:
            self.wait = WebDriverWait(self.driver, timeout)
            return self.wait.until(EC.presence_of_element_located(self.wait_element))
        except TimeoutException:
            return "Element not found within the specified time"

    def test_page_url(self, url):
        try:
            locator_strategy, locator_value = self.locator_of_input_field_pagespeed_insights
            self.driver.find_element(locator_strategy, locator_value).send_keys(url)
        except ():
            print("The test page url data was not found")

    def click_analyze_button(self):
        try:
            locator_strategy, locator_value = self.click_button_locator
            self.driver.find_element(locator_strategy, locator_value).click()
        except ():
            print("The analyze button data was not found")

    def get_mobile_site_performance(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_performance

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile site performance data was not found")

    def get_mobile_accessibility(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_accessibility

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile accessibility data was not found")

    def get_mobile_best_practices(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_best_practices

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile best practices data was not found")

    def get_mobile_seo(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_seo

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile SEO data was not found")

    def get_mobile_first_contentful_paint(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_first_contentful_paint

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile first contentful paint data was not found")

    def get_mobile_largest_contentful_paint(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_largest_contentful_paint

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile largest contentful paint data was not found")

    def get_mobile_total_blocking_time(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_total_blocking_time

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile total blocking time data was not found")

    def get_mobile_cumulative_layout_shift(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_cumulative_layout_shift

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile cumulative layout shift data was not found")

    def get_mobile_speed_index(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_speed_index

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The mobile speed index data was not found")

    def get_device_name_mobile(self):

        try:
            locator_strategy, locator_value = self.locator_of_mobile_device

            return self.driver.find_element(locator_strategy, locator_value).text
        except ():
            print("The device name mobile data was not found")

    def get_device_name_desktop(self):
        locator_strategy, locator_value = self.locator_of_desktop_device
        return self.driver.find_element(locator_strategy, locator_value).text

    def switching_to_desktop_tab(self):
        locator_strategy, locator_value = self.locator_of_switching_desktop_tab
        self.driver.find_element(locator_strategy, locator_value).click()

    def get_desktop_site_performance(self):
        locator_strategy, locator_value = self.locator_of_desktop_performance
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_accessibility(self):
        locator_strategy, locator_value = self.locator_of_desktop_accessibility
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_best_practices(self):
        locator_strategy, locator_value = self.locator_of_desktop_best_practices
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_seo(self):
        locator_strategy, locator_value = self.locator_of_desktop_seo
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_first_contentful_paint(self):
        locator_strategy, locator_value = self.locator_of_desktop_first_contentful_paint
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_largest_contentful_paint(self):
        locator_strategy, locator_value = self.locator_of_desktop_largest_contentful_paint
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_total_blocking_time(self):
        locator_strategy, locator_value = self.locator_of_desktop_total_blocking_time
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_cumulative_layout_shift(self):
        locator_strategy, locator_value = self.locator_of_desktop_cumulative_layout_shift
        return self.driver.find_element(locator_strategy, locator_value).text

    def get_desktop_speed_index(self):
        locator_strategy, locator_value = self.locator_of_desktop_speed_index
        return self.driver.find_element(locator_strategy, locator_value).text

    def close_window(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def delete_all_cache(self):
        if self.driver is not None:
            self.driver.delete_all_cookies()
