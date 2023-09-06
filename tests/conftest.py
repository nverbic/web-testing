import pytest
import json
from selenium.webdriver import Chrome, Firefox, Edge
from pages.log_in import LogInPage
from pages.home import HomePage

CONFIG_PATH = 'config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH, encoding="utf-8") as config_file:
        # data = json.load(config_file).encode("latin_1").decode("utf_8")
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config['drivers_config']:
        raise Exception('The config file does not contain "browser"')
    elif config['drivers_config']['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["drivers_config"]["browser"]}" is not a supported browser')
    return config['drivers_config']['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['drivers_config']['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
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


@pytest.fixture
def username(config):
    return config['user_1']['username']


@pytest.fixture
def password(config):
    return config['user_1']['password']


@pytest.fixture
def first_name(config):
    return config['user_1']['first_name']


@pytest.fixture
def last_name(config):
    return config['user_1']['last_name']


@pytest.fixture
def user_url(config):
    return config['user_1']['url']

# TODO: Create the schema with using the dot to access the user details (GPT)

@pytest.fixture
def username_user_2(config):
    return config['user_2']['username']


@pytest.fixture
def password_user_2(config):
    return config['user_2']['password']


@pytest.fixture
def first_name_user_2(config):
    return config['user_2']['first_name']


@pytest.fixture
def last_name_user_2(config):
    return config['user_2']['last_name']


@pytest.fixture
def user_2_url(config):
    return config['user_2']['url']


@pytest.fixture
def home_page(browser):
    return HomePage(browser)


# Accept cookies and sign in before every test
# Return: home_page
@pytest.fixture(autouse=True)
def log_in_and_return_home_page(browser, username, password):
    login_page = LogInPage(browser, username, password)
    home_page = login_page.load(). \
        accept_cookies(). \
        login()
