from __future__ import absolute_import

from behave import given, then, when

# To use the constant file, you can import switch
# from support.constants import switch

from support.page_factory import get_page_object, get_page_context, get_page_navigation

# To get the name of the current scenario, you can import get_scenario_name
# from support.page_factory import get_scenario_name


# Given steps
@given(u'the website displays the "{page}" page')
def given_website_displays_page(context, page):
    context.page = get_page_navigation(context, 'Navigation')
    context.page.navigate_to(context, page)
    context.page = get_page_object(context, page)
    context.page.page_is_displayed()


@given(u'the website displays the "{prompt}" prompt')
def given_website_displays_prompt(context, prompt):
    given_website_displays_page(context, prompt)

# When steps
@when(u'the user clicks on the "{button}" button')
def when_user_taps_button(context, button):
    context.page.element_tap(button, 'button', 40)


@when(u'the user types "{value}" on the "{field}" field')
def when_user_types_something(context, value, field):
    context.page.send_value(field, 'label', value, 40)


# Then steps
@then(u'the website should display the "{page}" page')
def then_website_display_screen(context, page):
    context.page = get_page_object(context, page)
    context.page.page_is_displayed()


@then(u'the website should display the "{button}" button')
def then_website_display_button(context, button):
    context.page.element_is_displayed(button, 'button', 40)


@then(u'the website should display the "{field}" field')
def then_website_display_field(context, field):
    context.page.element_is_displayed(field, 'label', 40)


@then(u'the website should display the "{prompt}" prompt')
def then_website_display_prompt(context, prompt):
    then_website_display_screen(context, prompt)


@then(u'the website should dismiss the "{prompt}" prompt')
def then_website_dismiss_prompt(context, prompt):
    context.page.element_is_not_displayed(prompt, 'prompt', 10)
