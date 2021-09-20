from pytest_bdd import scenario
from steps.test_main_page_steps import *


@scenario('../features/login_page.feature', 'Test user can open login page')
def test_login_page():
    pass


@scenario('../features/login_page.feature', 'Test user can open contact us page')
def test_open_contact_us_page():
    pass