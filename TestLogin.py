import time

import pytest
import softest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(softest.TestCase):
    driver = None

    @pytest.fixture(scope="class", autouse=True)
    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.wait = WebDriverWait(self.driver, 5)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=500x500")

        self.driver.get("https://tt-develop.quality-lab.ru")
        self.driver.set_window_size(200, 100)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_incorrectUserNameAndPassword(self):
        name = self.driver.find_element_by_name("_username")
        name.send_keys("TestUser")
        password = self.driver.find_element_by_id("password")
        password.send_keys("Password")
        self.assertEqual(len(self.driver.find_elements_by_xpath("//*[text()='Invalid credentials.']")), 0)

        submit = self.driver.find_element_by_xpath("//input[@value='Войти']")
        submit.click()
        self.assertEqual(len(self.driver.find_elements_by_xpath("//*[text()='Invalid credentials.']")), 1)
