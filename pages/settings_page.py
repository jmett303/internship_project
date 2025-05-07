from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class SettingsPage(Page):
    USER_GUIDE = (By.CSS_SELECTOR, '[class*="settings"] [href="/user-guide"]')
    SUBSCRIPTION = (By.CSS_SELECTOR, '[class*="settings"] [href="/subscription"]')


    def click_user_guide(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_GUIDE)).click()

    def click_mobile_user_guide(self):
        self.hover_element(*self.SUBSCRIPTION)
        self.wait.until(EC.element_to_be_clickable(self.USER_GUIDE)).click()