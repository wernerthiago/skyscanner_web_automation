# It's importing the BasePage class, who has all the definitions that are using the Appium driver.
from support.pages import BasePage
# It's importing the way to search elements through ANDROID_UIAUTOMATOR
# from support.android.ui_automator import get_text, get_description
# It's importing the constants file
from support.constants.navigation import switch as navigation_switch
# from support.constants.ida import switch as ida_switch
# from support.constants.volta import switch as volta_switch
from support.constants.home import switch as home_switch
from .home import locators as HomePage_locators
# from .ida import locators as IdaPage_locators
# from .volta import locators as VoltaPage_locators


class NavigationPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def navigate_to(self, context, page):
        if page == navigation_switch.get('HOME_PAGE'):  # Desired page
            pass
        elif page == navigation_switch.get('IDA_PAGE'):  # Desired page
            self.element_tap(home_switch.get('IDA_BUTTON'), 'button', 40, HomePage_locators)
        elif page == navigation_switch.get('VOLTA_PAGE'):  # Desired page
            self.element_tap(home_switch.get('VOLTA_BUTTON'), 'button', 40, HomePage_locators)
