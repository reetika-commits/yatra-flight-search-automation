from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from utilities.utils import Utils
import os 
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True)
def setup(request):
    log=Utils.custom_logger()
    browser=request.config.getoption("--browser")
    log.info(f"Browser value is: {browser}")
    if browser.lower()=="edge":
        driver=webdriver.Edge()
    elif browser.lower()=="chrome":
        options=Options()
        if os.getenv("GITHUB_ACTIONS")== "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver=webdriver.Chrome(options=options)
    elif browser.lower()=="opera":
        driver=webdriver.Opera()
    log.info("Launching browser")
    log.info("Maximizing browser")
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    if "This site can't be reach" in driver.page_source:
        driver.save_screenshots(f"Yatra website is not reachable_{datetime.now().strftime('%y%m%d_%H%M%S')}.png")
        log.info("Yatra website is not reachable")
        raise Exception("Yatra website is not reachable")
    else:
        log.info("Driver initialized")
        request.cls.driver=driver #return the instance of driver to the requesting class
   
    yield
    log.info("Browser closing")
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="edge",help="browser option: edge or chrome")
