from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on the settings option')
def click_settings_option(context):
    context.app.side_menu_page.click_settings_option()

@when('Click on the settings icon')
def click_settings_icon(context):
    context.app.side_menu_page.click_settings_icon()