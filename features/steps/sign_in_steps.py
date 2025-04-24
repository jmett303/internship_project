from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Enter email: {email}') #email: jackiemettler@yahoo.com
def enter_email(context, email):
    context.app.sign_in_page.enter_email(email)

@when('Enter password: {password}') #password: si5xFhT&$74dG#DN
def enter_password(context, password):
    context.app.sign_in_page.enter_password(password)

@when('Click continue')
def click_continue(context):
    context.app.sign_in_page.click_continue()
