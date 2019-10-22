from __future__ import absolute_import

from behave import given, then, when

# To use the constant file, you can import switch
from support.constants.ida import switch as ida_switch
from support.constants.volta import switch as volta_switch
from support.constants.navigation import switch as navigation_switch
# from support.constants.home import switch as home_switch

from pages.ida import locators as IdaPage_locators
from pages.volta import locators as VoltaPage_locators
# from pages.home import locators as HomePage_locators

from support.page_factory import get_page_object, get_page_context, get_page_navigation

# To get the name of the current scenario, you can import get_scenario_name
# from support.page_factory import get_scenario_name


# When steps
@when(u'the user selects "{month}" month')
def when_user_selects_month(context, month):
    current_page = get_page_context()
    if current_page == navigation_switch.get('IDA_PAGE'):
        context.page.select(ida_switch.get('MONTH_BUTTON'), 'button', ida_switch.get(month), 40)
    else:
        context.page.select(volta_switch.get('MONTH_BUTTON'), 'button', volta_switch.get(month), 40)


@when(u'the user selects "{day}" day')
def when_user_selects_day(context, day):
    current_page = get_page_context()
    if current_page == navigation_switch.get('IDA_PAGE'):
        context.page.element_tap(ida_switch.get('DAY_BUTTON'), 'button', 40, IdaPage_locators)
    else:
        context.page.element_tap(volta_switch.get('DAY_BUTTON'), 'button', 40, VoltaPage_locators)


@when(u'the user selects "{month}" month at the "{prompt}" prompt')
def when_user_selects_month_from_home(context, month, prompt):
    current_page = get_page_context()
    context.page = get_page_navigation(context, 'Navigation')
    context.page.navigate_to(context, prompt)
    if prompt == navigation_switch.get('IDA_PAGE'):
        context.page.select(ida_switch.get('MONTH_BUTTON'), 'button', ida_switch.get(month), 40, IdaPage_locators)
    else:
        context.page.select(volta_switch.get('MONTH_BUTTON'), 'button', volta_switch.get(month), 40, VoltaPage_locators)
    context.page.navigate_to(context, current_page)
    context.page = get_page_object(context, current_page)


@when(u'the user selects "{day}" day at the "{prompt}" prompt')
def when_user_selects_day_from_home(context, day, prompt):
    current_page = get_page_context()
    context.page = get_page_navigation(context, 'Navigation')
    context.page.navigate_to(context, prompt)
    if prompt == navigation_switch.get('IDA_PAGE'):
        context.page.element_tap(ida_switch.get('DAY_BUTTON'), 'button', 40, IdaPage_locators)
    else:
        context.page.element_tap(volta_switch.get('DAY_BUTTON'), 'button', 40, VoltaPage_locators)
    context.page.navigate_to(context, current_page)
    context.page = get_page_object(context, current_page)
