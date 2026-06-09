from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.base_driver import Base_Driver
from utilities.utils import Utils



class SearchResultPage(Base_Driver):
    
    def __init__(self,driver:WebDriver):
        super().__init__(driver)
        self.driver=driver
        self.log=Utils.custom_logger()
    
    #Locator
    stop_flight_locator="//p[text()='stop']"
    verify_stop_locator="//span[contains(text(),'1 Stop') or contains(text(),'2 Stops') or contains(text(),'Non Stop')]"

    #get
    def get_stop_flight(self,stop):
        stop_flight_xpath=self.stop_flight_locator.replace("stop",str(stop))
        return self.wait_element_to_be_clickable(By.XPATH, stop_flight_xpath)
    
    def get_verify_stop(self):
        return self.wait_presence_of_all_elements_located(By.XPATH,self.verify_stop_locator)

    def click_stop_flight(self,stop):
        try:
            self.log.info(f"Click on {stop} stop(s) flight result")
            self.get_stop_flight(stop).click()
        except Exception as e:
            self.take_screenshots("Select_Stop(s).png")
            self.log.info(f"Click on {stop} stop(s) flight result. Exception {e}")
            raise


    def verify_stops(self):
        return self.get_verify_stop()
        
        