from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import json

def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='browser: Chrome or Firefox'
    )
    parser.addoption(
        '--headless', action='store', default='True', help='debug: True or False'
    )
    # parser.addoption(
    #     '--test-data', action='store', default='{}', help='test data pass in as a JSON string'
    # )


# @pytest.fixture
# def testdata(request):
#     data = request.path
#     data = json.loads(data)
#     return data

@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture
def headless(request):
    return request.config.getoption('--headless')

@pytest.fixture
def driver(browser, headless):
    
    if browser == 'firefox':
        firefox_options = FirefoxOptions()
        if headless == 'True':
            firefox_options.add_argument('--headless')
        firefox_options.add_argument('--window-size=1920,1080')
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        yield driver
        driver.quit()
    else:
        chrome_options = ChromeOptions()
        if headless == 'True':
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        yield driver
        driver.quit()