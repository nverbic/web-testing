import pytest
import json
from selenium.webdriver import Chrome, Firefox, Edge
from pages.log_in import LogInPage

CONFIG_PATH = 'config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']


@pytest.fixture(scope='session')
def config_data():
    with open(CONFIG_PATH, encoding="utf-8") as config_file:
        # data = json.load(config_file).encode("latin_1").decode("utf_8")
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config_data):
    if 'browser' not in config_data['drivers_config']:
        raise Exception('The config file does not contain "browser"')
    elif config_data['drivers_config']['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config_data["drivers_config"]["browser"]}" is not a supported browser')
    return config_data['drivers_config']['browser']


@pytest.fixture(scope='session')
def config_wait_time(config_data):
    return config_data['drivers_config']['wait_time'] if 'wait_time' in config_data else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize driver
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    elif config_browser == 'edge':
        driver = Edge()

    #  Config_browser fixture throws an exception in case browser is not selected
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()


@pytest.fixture
def browser_second(config_browser, config_wait_time):
    # Initialize driver
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    elif config_browser == 'edge':
        driver = Edge()

    #  Config_browser fixture throws and exception in case browser is not selected
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def home_page(browser, config_data):
    users = config_data['users']
    login_page = LogInPage(browser, users[0]['username'], users[0]['password'])
    home_page = login_page.load().\
        accept_cookies().\
        login()
    return home_page


