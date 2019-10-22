from support.constants.navigation import switch as navigation_switch

from support.capabilities import create_capabilities

from selenium import webdriver

from support.pages.base import BasePage

import os

default_port = 4723
system_port = 8200
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0


def before_all(context):
    """Start the appium client and set some env variables"""
    print("BEFORE_ALL")
    input = context.config.userdata['browser'].split(',')
    caps = create_capabilities(input)
    context.browser = caps['browser_name']
    context.address = caps['address']
    port = default_port
    port = port + TASK_ID
    start_driver(context, port, caps)


def start_driver(context, port, caps):
    print("------ INITIALIZING WEBDRIVER ------")
    print("--- CAPABILITIES ---")
    print(caps)
    print("--- PORT ---")
    print(port)
    print("")
    if context.browser == 'chrome':
        context.driver = webdriver.Chrome('support/webdriver/chromedriver')
    elif context.browser == 'firefox':
        context.driver = webdriver.Firefox(executable_path='support/webdriver/firefoxdriver')
    elif context.browser == 'ie':
        context.driver = webdriver.Ie()
    context.driver.get(context.address)


def after_all(context):
    """Closes the appium client"""
    context.driver.close()
    print('AFTER_ALL')
    print(context.browser)
    print("Exiting Main Thread")


def after_scenario(context, scenario):
    """Closes the app after each test"""
    context.driver.get(context.address)


def before_scenario(context, scenario):
    """
    Opens the app before each scenario.
    If it's a new feature, the newfeature tag will reset the app. The newfeature tag is totally optional.
    """
    pass


def before_feature(context, feature):
    BasePage.set_page_name(navigation_switch.get('HOME_PAGE'))


def after_feature(context, feature):
    pass


def before_step(context, step):
    """Before each step, the scenario name is saved"""
    BasePage.set_scenario_name(context.scenario.name)
