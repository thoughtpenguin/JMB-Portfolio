#region Imports

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest
import json
import os

#endregion

#region Constants

CONFIGURATION_PATH = "configs/test_basic_auth.json"
SUCCESSFUL_LOGIN_MESSAGE = "Congratulations! You must have the proper credentials."
UNSUCCESSFUL_LOGIN_MESSAGE = "Not authorized"
URL_PREFIX = 'https://'
URL_SUFFIX = 'the-internet.herokuapp.com/basic_auth/'


#endregion

#region Fixtures

@pytest.fixture
def alert(driver:webdriver.Remote, browser):
    if browser != 'chrome':
        return driver.switch_to.alert
    return True

@pytest.fixture
def credentials():
    testdata = {}
    with open(CONFIGURATION_PATH) as file:
        testdata = json.load(file)
    return testdata

@pytest.fixture
def invalid_credentials(driver:webdriver.Remote, credentials):
    url = buildURL(credentials["invalid"]["username"], credentials["invalid"]["password"])
    loadPage(driver, url)
    return

@pytest.fixture
def invalid_password(driver:webdriver.Remote, credentials):
    url = buildURL(credentials["valid"]["username"], credentials["invalid"]["password"])
    loadPage(driver, url)
    return

@pytest.fixture
def invalid_user(driver:webdriver.Remote, credentials):
    url = buildURL(credentials["invalid"]["username"], credentials["valid"]["password"])
    loadPage(driver, url)
    return

@pytest.fixture
def no_login(driver:webdriver.Remote):
    loadPage(driver, buildURL())
    return

@pytest.fixture
def successful_login(driver:webdriver.Remote, credentials):
    url = buildURL(credentials["valid"]["username"], credentials["valid"]["password"])
    loadPage(driver, url)
    return

#endregion

#region Functions

def loadPage(driver:webdriver.Remote, url):
    driver.get(url)
    return

def buildURL(username="", password=""):
    if (username == "") & (password == ""):
        return URL_PREFIX + URL_SUFFIX
    return URL_PREFIX + username + ":" + password + "@" + URL_SUFFIX

def unsuccessfulLogin(driver:webdriver.Remote) -> bool:
    result = False
    attempt = 1
    while attempt < 3:
        try:
            body = driver.find_element(By.CSS_SELECTOR, "body")
            result = (body.text == UNSUCCESSFUL_LOGIN_MESSAGE) or (body.text == '')
        except Exception as e:
            continue
        attempt += 1
    return result

def successfulLogin(driver:webdriver.Remote) -> bool:
    element = driver.find_element(By.CSS_SELECTOR, "p")
    return element.text == SUCCESSFUL_LOGIN_MESSAGE

#endregion

#region Tests

class TestBasicAuth:

    def test_cancelled_login(self, driver:webdriver.Remote, no_login, alert:Alert, browser):
        assert alert
        if browser != 'chrome':
            alert.dismiss()
        assert unsuccessfulLogin(driver)
        return

    def test_successful_login(self, driver:webdriver.Remote, successful_login):
        assert successfulLogin(driver)
        return

    def test_invalid_user(self, driver:webdriver.Remote, invalid_user, alert:Alert, browser):
        assert alert
        if browser != 'chrome':
            alert.dismiss()
        assert unsuccessfulLogin(driver)
        return

    def test_invalid_password(self, driver:webdriver.Remote, invalid_password, alert:Alert, browser):
        assert alert
        if browser != 'chrome':
            alert.dismiss()
        assert unsuccessfulLogin(driver)
        return

    def test_invalid_credentials(self, driver:webdriver.Remote, invalid_credentials, alert:Alert, browser):
        assert alert
        if browser != 'chrome':
            alert.dismiss()
        assert unsuccessfulLogin(driver)
        return
    
#endregion



    