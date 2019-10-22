import json

# List of valid values in config.json for verification
# Add more values if needed
valid_keys = ('platformName', 'platformVersion', 'deviceName',
              'automationName', 'app', 'newCommandTimeout', 'udid',
              'appActivity', 'appPackage', 'bundleId', 'appName',
              'xcodeOrgId', 'xcodeSigningId')


def create_capabilities(browser_name):
    """Parses the "device_config.json" file to a valid dict object

    Creates a dict with the specified broswer_name, if the same is specified on
    the "device_config.json" file.

    It will always use a property specified in the device object with higher
    priority than the properties outside of it. This makes it really easy to
    set different app locations for devices that need different binaries, for
    example a simulator.
    """
    with open('resources/device_config.json', 'r') as f:
        config = json.load(f)

    for index in range(len(browser_name)):
        for platform in config:
            if platform == browser_name[index]:
                for browser in config[platform]['devices']:
                    browser['browser_name'] = platform
                    browser['path'] = browser.get('path')
                    browser['log_path'] = browser.get('log_path')
        # if browser.get(browser_name[key]) is None:
        #     raise Exception(
        #         'couldn\'t find a valid device in devices.json with name: {0}'
        #         .format(browser_name[key]))
    browser['address'] = config.get('address')
    return browser
