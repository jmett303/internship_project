from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep, process_time_ns

@given('Open Reelly main page')
def open_reelly_main(context):
    context.app.main_page.open_main_page()
    sleep(2)
