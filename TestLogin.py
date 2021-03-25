import pytest
import softest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(softest.TestCase):

    @pytest.fixture(scope="class", autouse=True)
    def init_driver(self):
        driver = webdriver.Chrome()
        driver.wait = WebDriverWait(driver, 5)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=500x500")

        driver.set_window_size(200, 100)
        driver.get("https://tt-develop.quality-lab.ru")
        driver.maximize_window()
        yield
        driver.quit()

    def test_incorrectUserNameAndPassword(self):
        print("Hello TT")