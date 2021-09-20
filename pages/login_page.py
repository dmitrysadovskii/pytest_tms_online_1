from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.auth_test_is_present()

    def auth_test_is_present(self):
        auth_text = self.find_element((By.CLASS_NAME, 'page-heading')).text
        assert auth_text == "AUTHENTICATION"
