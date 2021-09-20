from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def open_login_page(self):
        self.find_element((By.CLASS_NAME, 'login')).click()

    def open_contact_us_page(self):
        self.find_element((By.ID, 'contact-link')).click()
