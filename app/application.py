from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.settings_page import SettingsPage
from pages.user_guide_page import UserGuidePage
from pages.side_menu_page import SideMenuPage



class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.settings_page = SettingsPage(driver)
        self.user_guide_page = UserGuidePage(driver)
        self.side_menu_page = SideMenuPage(driver)
