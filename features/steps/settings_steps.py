from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on the User Guide Option')
def click_user_guide(context):
    context.app.settings_page.click_user_guide()