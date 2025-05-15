from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Tracking:

    def __init__(self):
        self.driver = None,
        self.chrome_webdriver_path = "C:\\Projects\\automation\\Webdriver\\chromedriver.exe"
        self.edge_webdriver_path = "C:\\Projects\\automation\\Webdriver\\msedgedriver.exe"
        self.firefox_webdriver_path = "C:\\Projects\\automation\\Webdriver\\geckodriver.exe"
        self.username_id = "input_username",
        self.password_id = "input_password",
        self.login_id = "input_go",
        self.database_xpath = "//a[normalize-space()='ppcbingo']"
        self.user_click_in_xpath = "//a[normalize-space()='wp_user_click_in']"
        self.keyword_xpath = "//tr/td[normalize-space()='']"
        self.click_in_id_xpath = "//tr/td[normalize-space()='']/preceding::td[2]"

    def open_chrome_webdriver(self):
        s = Service(self.chrome_webdriver_path)
        self.driver = webdriver.Chrome(service=s)

    def open_edge_webdriver(self):
        s = Service(self.edge_webdriver_path)
        self.driver = webdriver.Edge(service=s)

    def open_firefox_webdriver(self):
        s = Service(self.firefox_webdriver_path)
        self.driver = webdriver.Edge(service=s)

    def maximize_window(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def implicit_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def test_url(self, url):
        self.driver.get(url)

    def db_url(self, url):
        self.driver.get(url)

    def new_tab(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_id).click()

    def choose_db_table(self, table_name):
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{table_name}']").click()

    def click_user_clicking(self):
        self.driver.find_element(By.XPATH, self.user_click_in_xpath).click()

    def find_keyword(self, keyword):
        return self.driver.find_element(By.XPATH, f"//tr/td[normalize-space()='{keyword}']").text

    def get_click_in_id(self, keyword):
        return self.driver.find_element(By.XPATH, f"//tr/td[normalize-space()='{keyword}']/preceding::td[2]").text

    def close_window(self):
        self.driver.quit()
