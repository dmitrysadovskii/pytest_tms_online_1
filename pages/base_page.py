from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://automationpractice.com/index.php"

    def open_main_page(self):
        self.driver.get(self.url)

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))