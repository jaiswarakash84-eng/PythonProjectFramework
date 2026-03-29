import pytest

from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_link = page.locator("#login2")
        self.username = page.locator("#loginusername")
        self.password = page.locator("#loginpassword")
        self.login_button = page.locator("button[onclick='logIn()']")
        self.name_of_user = page.locator("#nameofuser")

    #Actions
    def open_login_page(self):
        self.page.goto("https://www.demoblaze.com")

    def click_login_link(self):
        self.login_link.click()

    def enter_username(self,username):
        self.username.fill(username)

    def enter_password(self,password):
        self.password.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def logged_user(self):
        return self.name_of_user