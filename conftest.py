import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function", autouse=True)
def resource_setup():
    print("Test start")
    yield
    print("Test finished")


@pytest.fixture(scope="class", autouse=True)
def resource_tear_down():
    yield
    print("All tests in TestFirst finished")


@pytest.fixture(scope="function")
def init_web_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=500x500")

    driver.get("https://tt-develop.quality-lab.ru")
    driver.set_window_size(200, 100)
    driver.maximize_window()
    yield driver
    driver.quit()
