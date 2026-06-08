from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from utilities.utils import Utils

@pytest.fixture(autouse=True)
def setup(request):
    log=Utils.custom_logger()
    browser=request.config.getoption("--browser")
    log.info(f"Browser value is: {browser}")
    if browser.lower()=="edge":
        driver=webdriver.Edge()
    elif browser.lower()=="chrome":
        driver=webdriver.Chrome()
    elif browser.lower()=="opera":
        driver=webdriver.Opera()
    log.info("Launching browser")
    driver.get("https://www.yatra.com/")
    log.info("Maximizing browser")
    driver.maximize_window()
    log.info("Driver initialized")
    request.cls.driver=driver #return the instance of driver to the requesting class
   
    yield
    log.info("Browser closing")
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="edge",help="browser option: edge or chrome")
