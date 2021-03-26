import pytest
from selenium.common.exceptions import NoSuchElementException


class TestLoginNegative:

    def test_incorrectUserNameAndPassword(self, init_web_driver):
        name = init_web_driver.find_element_by_name("_username")
        name.send_keys("TestUser")
        password = init_web_driver.find_element_by_id("password")
        password.send_keys("Password")

        element = lambda: init_web_driver.find_element_by_xpath("//*[text()='Invalid credentials.']")
        with pytest.raises(NoSuchElementException):
            element().click()

        submit = init_web_driver.find_element_by_xpath("//input[@value='Войти']")
        submit.click()
        assert element().is_displayed() is True
