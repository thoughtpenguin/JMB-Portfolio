from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import pytest

BASE_URL = "https://the-internet.herokuapp.com" 
URL = BASE_URL + "/broken_images"

@pytest.fixture
def driver() -> webdriver.Remote:
    return webdriver.Firefox()

@pytest.fixture
def load_page(driver:webdriver.Remote):
    driver.get(URL)
    return

@pytest.fixture
def downloadable_files(driver:webdriver.Remote, load_page):
    return driver.get_downloadable_files()

@pytest.fixture
def get_images_in_content_div(driver:webdriver.Remote, load_page):
    return driver.find_elements(By.XPATH, "//div[@id='content']//img")

def image_exists(driver:webdriver.Remote, url):
    driver.get(url)
    #h1 element will be present if page is "Not Found"
    h1 = driver.find_elements(By.TAG_NAME, "h1")
    return len(h1) == 0

class TestBrokenImages:
    def test_three_image_tags_in_content_div(self, driver:webdriver.Remote, get_images_in_content_div):
        assert len(get_images_in_content_div) == 3
        driver.quit()
        return
    def test_first_image(self, driver:webdriver.Remote, get_images_in_content_div:list[WebElement]):
        url = get_images_in_content_div[0].get_attribute("src")
        assert image_exists(driver, url)
        driver.quit()
        return
    def test_second_image(self, driver:webdriver.Remote, get_images_in_content_div:list[WebElement]):
        url = get_images_in_content_div[1].get_attribute("src")
        assert image_exists(driver, url)
        driver.quit()
        return
    def test_third_image(self, driver:webdriver.Remote, get_images_in_content_div:list[WebElement]):
        url = get_images_in_content_div[2].get_attribute("src")
        assert image_exists(driver, url)
        driver.quit()


        

