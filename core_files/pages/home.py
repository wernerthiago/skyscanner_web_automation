from selenium.webdriver.common.by import By
# It's importing the BasePage class, who has all the definitions that are using the Appium driver.
from support.pages.base import BasePage
# It's importing the way to search elements through ANDROID_UIAUTOMATOR
# from support.android.ui_automator import get_text, get_description
# It's importing the constants file
from support.constants.home import switch

locators = {
    'label': {
        switch.get('ORIGEM_LABEL'): {
            'chrome':
            (By.ID, 'fsc-origin-search'),
            'firefox':
            (By.ID, 'fsc-origin-search'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        },
        switch.get('DESTINO_LABEL'): {
            'chrome':
            (By.ID, 'fsc-destination-search'),
            'firefox':
            (By.ID, 'fsc-destination-search'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        },
        switch.get('IDA_BUTTON'): {
            'chrome':
            (By.ID, 'depart-fsc-datepicker-button'),
            'firefox':
            (By.ID, 'depart-fsc-datepicker-button'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        },
        switch.get('VOLTA_BUTTON'): {
            'chrome':
            (By.ID, 'return-fsc-datepicker-button'),
            'firefox':
            (By.ID, 'return-fsc-datepicker-button'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        }
    },
    'button': {
        switch.get('BUSCAR_BUTTON'): {
            'chrome':
            (By.CLASS_NAME, 'BpkButton_bpk-button__3V91-'),
            'firefox':
            (By.CLASS_NAME, 'BpkButton_bpk-button__3V91-'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        },
        switch.get('IDA_BUTTON'): {
            'chrome':
            (By.ID, 'depart-fsc-datepicker-button'),
            'firefox':
            (By.ID, 'depart-fsc-datepicker-button'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        },
        switch.get('VOLTA_BUTTON'): {
            'chrome':
            (By.ID, 'return-fsc-datepicker-button'),
            'firefox':
            (By.ID, 'return-fsc-datepicker-button'),
            'ie':
            (By.NAME, 'TODO'),  # TODO
        }
    }
}


class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.locator = locators

    def navigate(self):
        """You should implement the way to navigate to this Page"""
        pass

    def page_is_displayed(self):
        """You should use the definitons from the BasePage to check if the Page is really displayed"""
        self.element_is_displayed(switch.get('IDA_BUTTON'), 'button', 40)

    def tap_ida(self):
        """You should use the tap definition from the BasePage to tap on a button from the stepDefinitions"""
        self.element_tap(switch.get('IDA_BUTTON'), 'button', 40)

    def tap_volta(self):
        """You should use the tap definition from the BasePage to tap on a button from the stepDefinitions"""
        self.element_tap(switch.get('VOLTA_BUTTON'), 'button', 40)

    def tap_origem(self):
        """You should use the tap definition from the BasePage to tap on a button from the stepDefinitions"""
        self.element_tap(switch.get('ORIGEM_LABEL'), 'label', 40)

    def tap_destino(self):
        """You should use the tap definition from the BasePage to tap on a button from the stepDefinitions"""
        self.element_tap(switch.get('DESTINO_LABEL'), 'label', 40)

    def tap_buscar(self):
        """You should use the tap definition from the BasePage to tap on a button from the stepDefinitions"""
        self.element_tap(switch.get('BUSCAR_BUTTON'), 'button', 40)
