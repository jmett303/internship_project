from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify User Guide page opens')
def verify_user_guide_page_open(context):
    context.app.user_guide_page.verify_user_guide_page_open()

@then('Switch to iFrame')
def switch_to_iframe(context):
    context.app.user_guide_page.switch_to_iframe()

@then('Verify the lesson video title is: {expected_title}')
def verify_video_title(context, expected_title):
    context.app.user_guide_page.verify_video_title(expected_title)