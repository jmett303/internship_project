from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[class*="login-button"]')

    def enter_email(self, email):
        self.wait_until_clickable(*self.EMAIL_FIELD)
        sleep(1)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(2)




