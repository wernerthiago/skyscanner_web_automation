from selenium.webdriver.common.by import By
# It's importing the BasePage class, who has all the definitions that are using the Appium driver.
from support.pages.base import BasePage
# It's importing the way to search elements through ANDROID_UIAUTOMATOR
# from support.android.ui_automator import get_text, get_description
# It's importing the constants file
from support.constants.result import switch

locators = {
    'button': {
        switch.get('LIST_BUTTON'): {
            'chrome':
            (By.ID, 'browse-section'),
            'firefox':
            (By.ID, 'browse-section'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        }
    }
}


class ResultPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.locator = locators

    def navigate(self):
        """You should implement the way to navigate to this Page"""
        pass

    def page_is_displayed(self):
        """You should use the definitons from the BasePage to check if the Page is really displayed"""
        self.element_is_displayed(switch.get('LIST_BUTTON'), 'button', 80)
