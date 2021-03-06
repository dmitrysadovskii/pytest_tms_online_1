import allure
from selenium import webdriver
import pytest
import os
from datetime import datetime


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('html_reports'):
        os.makedirs('html_reports')
    config.option.htmlpath = f'html_reports/ {datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.html'


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        try:
            if 'browser' in item.fixturenames:
                browser = item.funcargs['browser']
            else:
                print('Does not have browser fixture')
                return
            allure.attach(browser.get_screenshot_as_png(), "Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f'Failed to make screenshot: {e}')
