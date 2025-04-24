from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    MAIN_PAGE_URL = 'https://soft.reelly.io'

    def open_main_page(self):
        self.driver.get(self.MAIN_PAGE_URL)
