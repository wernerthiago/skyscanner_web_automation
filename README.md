# Python Automation (Python + Selenium + Behave)

This is a project created to show a automation project example using Python 3. The project uses the following dependencies:

[Behave](https://github.com/behave/behave): Cucumber implementation in python

[Python Appium Client](https://github.com/appium/python-client): Appium client implementation in python. Even using Selenium, we'll install Appium to have all the packages installed properly.

[Paver](https://paver.readthedocs.io/en/almad-rtdfixes/index.html): Parallel way to run Behave

# Installation

* [Automatically](.#Automatically)

* [Manually](.#Manually)

# Manually
## Setup

### Python Setup

#### Python

First, you'll need Python 3 to use this project. You can get it easily with brew:

```brew install python3```

Depending on your environment, the symlinks ```brew``` creates can be different. It's commonly `python` or `python3`. To know which one is the correct one, just run these commands followed by ```--version```, and check if the version is > 3.6. Then just use the one that has a 3.x as your default one.

```python --version```

```python3 --version```

In case your version is 2.7, that's the default MacOS version, and it WON'T RUN the automation. In this case, try going to the [python official download page](https://www.python.org/downloads/) and follow the tutorial there.

#### pip

Just follow the instructions on this link https://pip.pypa.io/en/stable/installing/

### Dependencies Setup

#### Dependencies

To install the dependencies, just run:

```pip install -r requirements.txt```

If you created a virtualenv, it will install only on it. Otherwise, it will install in your system. In some cases, the installation may fail, recomending you to run with `--user`. Just run `pip install --user -r requirements.txt`.

### Appium Server Setup

This project needs a running ```appium``` server to run, which you can install it on your computer and run it locally. To install it, you'll need ```npm```, which comes with the ```node``` brew package:

```brew install node```

After that run:

```npm install -g appium```

#### Appium Doctor

Appium also needs some dependencies to work. I won't cover all of them (since there are a lot of dependencies), but to see if you have any environments issues, you just need to run ```appium-doctor```, which you can get with:

```npm install -g appium-doctor```

"The text above was wrote by João Carneiro Haas""

# Automatically
```sh install.sh```

## Tech Details

### Pages

Every page object **must have** the following pre-requisites:

- Must inherit the [`BasePage`](core_files/support/pages/base.py) class before any other class.
- Must inherit the [element classes](core_files/support/elements/) that the page is gonna use, otherwise it won't have valid methods to execute on the steps.
- Should call `super().__init__(context)` on it's constructor.
- Should define a `locator` object on it's constructor, and it should have valid locator dictionaries.
- Should have a `navigate()` method defined, which will execute actions on other pages to reach your page.
- Should have a `page_is_displayed()` method defined, and the same should verify that a unique element is appearing on the screen.

### Locators

Locators should always have a dictionary of locators for each element you're testing. The keys of this dict should be the name
that will match the step call, and the value should be another dictionary, with `'chrome'` and `'firefox'` as keys, and each of
them should have a locator tuple, which is composed of a `By.SOMETHING` and a querry.

Example:

```python
locator.buttons = {
  'Accept': {
    'chrome': (By.NAME, 'Accept'),
    'firefox': (By.ID, 'accept_button_id')
  },
  'Decline': {
    'chrome': (By.NAME, 'Decline'),
    'firefox': (By.ID, 'decline_button_id')
  }
}
```

### Run the automation code
To run paralleling, you should run the follow command:
`paver run parallel {browser1, browser2, ...}`

To run single, you should run the follow command:
`paver run parallel browser1`

### Configuring the devices
Firstly, you should configure the browsers that are allowed to run this automation code. You can configure the browsers and their capabilities at [`device_config.json`](core_files/resources/)

### Setup Selenium to run the tests in parallel
Initial bibliography: [Appium Pro: Running Multiple Appium Tests in Parallel](https://appiumpro.com/editions/28)

To make these things easier to visualize, we need to understand that Appium creates a local server in the machine. This local server has by default a hostname (localhost/127.0.0.1) and port (8200 named as `systemPort`). You definitely can't power up two servers at the same port. To run Appium parallelly, we need to define one port to each Appium instance. Also, Appium has another port that is provided to listen to the code. So, you should create different `ports` and `systemPorts` to use Appium parallelly.

The [`environment`](core_files/features/environment.py) file does this logic. You should pay attention to match the `systemPort` and `port` of the information described in the code.