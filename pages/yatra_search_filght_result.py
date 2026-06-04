from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import Base_Driver


class SearchResultPage(Base_Driver):
    def __init__(self,driver:WebDriver):
        super().__init__(driver)
        self.driver=driver
    
    #Locator
    stop_flight_locator="//p[text()='stop']"

    #get
    def get_stop_flight(self,stop):
        stop_flight_xpath=self.stop_flight_locator.replace("stop",stop)
        print("inside get stop flight")
        print(stop_flight_xpath)
        return self.wait_element_to_be_clickable(By.XPATH, stop_flight_xpath)

    def click_stop_flight(self,stop):
        print("inside one stop flight result")
        self.get_stop_flight(stop).click()