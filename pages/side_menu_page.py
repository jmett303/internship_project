from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class SideMenuPage(Page):
    SETTINGS_OPTION = (By.CSS_SELECTOR, '[class="menu-block"] [href="/settings"]')
    SETTINGS_ICON = (By.CSS_SELECTOR, '[class*="settings-link"]')


    def click_settings_option(self):
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_OPTION)).click()
        sleep(2)

    def click_settings_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_ICON)).click()
        sleep(2)