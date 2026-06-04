from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest

@pytest.fixture(autouse=True)
def setup(request):
    browser=request.config.getoption("--browser")
    if browser.lower()=="edge":
        driver=webdriver.Edge()
    elif browser.lower()=="chrome":
        driver=webdriver.Chrome()
    elif browser.lower()=="opera":
        driver=webdriver.Opera()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver=driver #return the instancec of driver to the requesting class
   
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="edge",help="browser option: edge or chrome")
