from selenium import webdriver
import pytest
import os
from datetime import datetime


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('html_reports'):
        os.makedirs('html_reports')
    config.option.htmlpath = f'html_reports/ {datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.html'
