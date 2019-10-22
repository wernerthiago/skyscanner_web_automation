from selenium.webdriver.common.by import By
# It's importing the BasePage class, who has all the definitions that are using the Appium driver.
from support.pages.base import BasePage
# It's importing the way to search elements through ANDROID_UIAUTOMATOR
# from support.android.ui_automator import get_text, get_description
# It's importing the constants file
from support.constants.volta import switch

locators = {
    'prompt': {
        switch.get('VOLTA_DATE_PICKER'): {
            'chrome':
            (By.ID, 'return-fsc-datepicker-popover'),
            'firefox':
            (By.ID, 'return-fsc-datepicker-popover'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        }
    },
    'button': {
        switch.get('VOLTA_DATE_PICKER'): {
            'chrome':
            (By.ID, 'return-fsc-datepicker-popover'),
            'firefox':
            (By.ID, 'return-fsc-datepicker-popover'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        },
        switch.get('DAY_BUTTON'): {
            'chrome':
            (By.XPATH, '//*[@id="return-fsc-datepicker-popover"]/div/div/div[2]/div/table/tbody/tr[1]/td[3]/button'),
            'firefox':
            (By.XPATH, '//*[@id="return-fsc-datepicker-popover"]/div/div/div[2]/div/table/tbody/tr[1]/td[3]/button'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        },
        switch.get('MONTH_BUTTON'): {
            'chrome':
            (By.ID, 'return-calendar__bpk_calendar_nav_select'),
            'firefox':
            (By.ID, 'return-calendar__bpk_calendar_nav_select'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        }
    }
}


class VoltaPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.locator = locators

    def navigate(self):
        """You should implement the way to navigate to this Page"""
        pass

    def page_is_displayed(self):
        """You should use the definitons from the BasePage to check if the Page is really displayed"""
        self.element_is_displayed(switch.get('VOLTA_DATE_PICKER'), 'button', 40)
