
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    return driver
@pytest.fixture
def page_loaded(driver:webdriver.Remote):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

@pytest.fixture
def add_element_button(driver:webdriver.Remote, page_loaded):
    return driver.find_element(By.XPATH, '//button[@onclick="addElement()"]')

class TestAddRemoveElements:
    def test_url_is_expected(self, driver:webdriver.Remote, page_loaded):
        assert driver.current_url == 'https://the-internet.herokuapp.com/add_remove_elements/'
        driver.close()
        return
    def test_no_added_elements_present(self, driver:webdriver.Remote, page_loaded):
        _list = driver.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(_list) == 0
        driver.close()
        return
    def test_add_element_button_presence(self, driver:webdriver.Remote, add_element_button):
        assert add_element_button
        driver.close()
        return
    def test_add_one_element(self, driver:webdriver.Remote, add_element_button:WebElement):
        add_element_button.click()
        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(delete_buttons) == 1
        driver.close()
        return
    def test_add_five_elements(self, driver:webdriver.Remote, add_element_button:WebElement):
        i = 0
        while i < 5:
            add_element_button.click()
            i += 1
        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(delete_buttons) == 5
        driver.close()
        return
    def test_add_two_remove_one(self, driver:webdriver.Remote, add_element_button:WebElement):
        i = 0
        while i < 2:
            add_element_button.click()
            i += 1
        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        delete_buttons[0].click()
        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(delete_buttons) == 1
        driver.close()
        return
    def test_add_five_remove_five(self, driver:webdriver.Remote, add_element_button:WebElement):
        i = 0
        while i < 5:
            add_element_button.click()
            i += 1
        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        for button in delete_buttons:
            button.click()
        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(delete_buttons) == 0
        driver.close()
        return
    def test_refresh_after_add(self, driver:webdriver.Remote, add_element_button:WebElement):
        add_element_button.click()
        driver.refresh()
        delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
        assert len(delete_buttons) == 0
        driver.close()
        return
