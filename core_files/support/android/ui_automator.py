def get_text(string):
    """Will return the parameter used to search for the specified string"""
    return 'new UiSelector().text(\"{0}\")'.format(string)


def get_description(string):
    """Will return the parameter used to search for the specified content-desc"""
    return 'new UiSelector().description(\"{0}\")'.format(string)
