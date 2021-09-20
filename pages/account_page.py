from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountPage(BasePage):

    def should_be_account_page(self):
        account_text = self.find_element((By.CSS_SELECTOR, '.row.addresses-lists')).text