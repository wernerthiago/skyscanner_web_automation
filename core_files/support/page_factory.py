import pages as pages
from support.pages import base
from support.constants.navigation import switch


def get_page_object(context, page_name):
    base.BasePage.set_page_name(page_name)
    # base.BasePage.set_mother_page(page_name)
    return f(context, page_name)


def get_page_navigation(context, page_name):
    return f(context, page_name)


def get_page_context():
    return base.BasePage.get_page_name()


def get_scenario_name():
    return base.BasePage.get_scenario_name()


def f(context, page_name):
    return {
        switch.get('NAVIGATION'): pages.NavigationPage(context),
        switch.get('HOME_PAGE'): pages.HomePage(context),
        switch.get('RESULT_PAGE'): pages.ResultPage(context),
        switch.get('IDA_PAGE'): pages.IdaPage(context),
        switch.get('VOLTA_PAGE'): pages.VoltaPage(context)
    }[page_name]
