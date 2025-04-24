from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class UserGuidePage(Page):
    VIDEO_TITLE = (By.CSS_SELECTOR, '[class*="ytp-title-link"]')
    FRAME1 = (By.CSS_SELECTOR, 'div[class*="video-2"] iframe')

    def verify_user_guide_page_open(self):
        self.wait.until(EC.url_contains('user-guide'), message='URL does not contain {expected_partial_url}.')

    def switch_to_iframe(self):
        frame1= self.driver.find_element(*self.FRAME1)
        self.driver.switch_to.frame(frame1)
        self.driver.switch_to.frame('player')

    def verify_video_title(self, expected_title):
        actual_title = self.find_element(*self.VIDEO_TITLE).text
        assert expected_title in actual_title, f'Error: {expected_title} not found in {actual_title}'
        print(f'Video title: "{actual_title}" is correct')
