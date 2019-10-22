from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    """Base class for all pages classes

    This class creates the necessary variables that a page objects needs to
    work, and so, it must be inherithed by all of them.

    While this class doesn't deliver any callable methods by the user, it does
    for the elements classes, which execute methods defined here on their
    execution.
    """
    name = ''
    scenario_name = ''

    def __init__(self, context):
        self.driver = context.driver
        self.browser = context.browser
        self.__touch = TouchAction()

    def set_page_name(page):
        """Used to save the current page name"""
        BasePage.name = page

    def get_page_name():
        """Used to return the current page name"""
        return BasePage.name

    def set_scenario_name(scenario):
        """Used to save the current scenario name"""
        BasePage.scenario_name = scenario

    def get_scenario_name():
        """Used to return the current scenario name"""
        return BasePage.scenario_name

    # Generic element methods
    def __get_element(self, by, element_querry, wait_time):
        """Searches for an appium/selenium element

        This method tries to search for an element with the specified querry
        (element querry) using the specified way to search it (by). Also, if a
        'wait_time' is specified, it will wait that long before returning a
        'NoSuchElementException' exception.
        """
        if wait_time:
            el = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, element_querry)))
        else:
            el = self.driver.find_element(by, element_querry)
        return el

    def __get_text_of_element(self, by, element_querry, wait_time):
        if wait_time:
            el = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, element_querry)))
        else:
            el = self.driver.find_element(by, element_querry).text
        return el

    def __get_element_loc(self, loc_name, loc_type, loc_page=None):
        """Searches for a locator tuple in the specified dict

        This method receives a dict of tuples, and the name of the wanted
        element. Then it tries to find a locator with that name, and if found,
        the same is returned.
        """
        if loc_page is not None:
            try:
                return loc_page[loc_type][loc_name][self.browser]
            except KeyError:
                raise Exception(
                    'element doesn\'t exist in page object: {0}'.format(loc_name))
        else:
            try:
                return self.locator[loc_type][loc_name][self.browser]
            except KeyError:
                raise Exception(
                    'element doesn\'t exist in page object: {0}'.format(loc_name))

    def element_is_displayed(self, el_name, el_type, wait_time=0):
        """Find a locator and return True if the same is displayed"""
        el_locator = self.__get_element_loc(el_name, el_type)
        el = self.__get_element(*el_locator, wait_time)
        return el.is_displayed()

    def element_with_text(self, el_name, el_type, wait_time=0):
        """Find a locator with text and return the text"""
        el_locator = self.__get_element_loc(el_name, el_type)
        return self.__get_text_of_element(*el_locator, wait_time)

    def assert_text_element(self, text, el_name, el_type, wait_time=0):
        """TBD"""
        actual = self.element_with_text(el_name, el_type, wait_time)
        if actual.text == text:
            pass
        else:
            raise Exception('The text is not matching: {0}'.format(actual.text))

    def element_is_disabled(self, el_name, el_type, wait_time=0):
        """Find a locator with text and return the text"""
        el_locator = self.__get_element_loc(el_name, el_type)
        el = self.__get_element(*el_locator, wait_time)
        if el.is_enabled() is False:
            pass
        else:
            raise Exception(
                'WRONG: The element is enabled: {0}'.format(el.is_enabled()))

    def element_is_enabled(self, el_name, el_type, wait_time=0):
        """TBD"""
        el_locator = self.__get_element_loc(el_name, el_type)
        el = self.__get_element(*el_locator, wait_time)
        if el.is_enabled() is True:
            pass
        else:
            raise Exception(
                'WRONG: The element is disabled: {0}'.format(el.is_enabled()))

    def element_is_checked(self, el_name, el_type, wait_time=0):
        """TBD"""
        el_locator = self.__get_element_loc(el_name, el_type)
        el = self.__get_element(*el_locator, wait_time)
        return el.get_attribute('checked')

    def send_value(self, el_name, el_type, value, wait_time, loc_page=None):
        """TBD"""
        el_locator = self.__get_element_loc(el_name, el_type, loc_page)
        el = self.__get_element(*el_locator, wait_time)
        try:
            el.send_keys(value)
        except KeyError:
            raise Exception(
                'WRONG: A problem occurred during send a value to the key: {0}'.format(value))

    def element_is_not_displayed(self, el_name, el_type, wait_time=0):
        """Find a locator and return True if the same is not displayed"""
        el_locator = self.__get_element_loc(el_name, el_type)
        try:
            self.__get_element(*el_locator, wait_time)
        except TimeoutException:
            return True

    def element_tap(self, el_name, el_type, wait_time, loc_page=None):
        """Find a locator and tap on it"""
        el_locator = self.__get_element_loc(el_name, el_type, loc_page)
        el = self.__get_element(*el_locator, wait_time)
        el.click()

    def select(self, el_name, el_type, option, wait_time, loc_page=None):
        """Sends a value to a component"""
        el_locator = self.__get_element_loc(el_name, el_type, loc_page)
        el = self.__get_element(*el_locator, wait_time)
        try:
            Select(el).select_by_value(option)
        except KeyError:
            raise Exception(
                'WRONG: A problem occurred during select the option: {0}'.format(option))
