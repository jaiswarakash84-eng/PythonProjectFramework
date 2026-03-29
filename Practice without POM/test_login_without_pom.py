#test file what to test without pom

import pytest
from playwright.sync_api import Page, expect

def test_login(page:Page):
    #open url
    page.goto("https://www.demoblaze.com/")

    #click login
    page.click("#login2")

    #enter username
    page.fill("#loginusername","akax")

    #enter password
    page.fill("#loginpassword","akax@123")

    #click login button
    page.click("button[onclick='logIn()']")

    #validation
    user=page.locator("#nameofuser")
    expect(user).to_be_visible()

