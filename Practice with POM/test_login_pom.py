
import pytest
from playwright.sync_api import Page, expect
from login_page import LoginPage

def test_login(page: Page):
    login = LoginPage(page)

    login.open_login_page()
    login.click_login_link()
    login.enter_username("akax")
    login.enter_password("akax@123")
    login.click_login_button()

    expect(login.logged_user()).to_be_visible()

