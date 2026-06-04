from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
import time

from base.base_driver import Base_Driver
from pages.yatra_search_filght_result import SearchResultPage

class LaunchPage(Base_Driver):
    def __init__(self,driver:WebDriver):
        super().__init__(driver)
        self.driver=driver
    
    #Locators
    depart_from_field_locator="//*[text()='Departure From']"
    depart_from_location_locator=f"//*[contains(text(),'departairport')]"
    going_to_field_locator="//p[text()='Going To']"
    going_to_location_locator=f"//span[contains(text(),'arrivalairport')]"
    travel_date_field_locator="//span[contains(text(),'Departure Date')]"
    travel_date_locator=f"//*[contains(@aria-label, 'month') and contains(@aria-label, 'day') and contains(@aria-label, 'year')]"
    search_btn_locator="//button[contains(text(),'Search')]" 

    #get 
    def get_depart_from_field(self):
        print("inside get depart from field")
        return self.wait_element_to_be_clickable(By.XPATH, self.depart_from_field_locator)
    
    def get_depart_from_location(self,departairport):
        depart_from_location_xpath=(self.depart_from_location_locator.replace("departairport",departairport))
        print("inside get depart from location")
        print(depart_from_location_xpath)
        return self.wait_element_to_be_clickable(By.XPATH, depart_from_location_xpath)
    
    def get_goin_to_field(self):
        print("inside get going to field")
        return self.wait_element_to_be_clickable(By.XPATH,self.going_to_field_locator)
    
    def get_going_to_location(self,arrivalairport):
        print("inside get going to location")
        print(self.going_to_location_locator)
        return self.wait_element_to_be_clickable(By.XPATH, self.going_to_location_locator.replace("arrivalairport",arrivalairport))
    
    def get_travel_date_field(self):
        print("inside get travel date field")
        return self.wait_element_to_be_clickable(By.XPATH, self.travel_date_field_locator)
    
    def get_travel_date(self,traveldate):
        day=traveldate.split("/")[0]
        month=traveldate.split("/")[1]
        year=traveldate.split("/")[2]
        print(self.travel_date_locator)
        return self.wait_element_to_be_clickable(By.XPATH, self.travel_date_locator.replace("month",month).replace("day",day).replace("year",year))

    def get_search_btn(self):
        print("inside get search btn")
        return self.wait_element_to_be_clickable(By.XPATH, self.search_btn_locator)

    #click
    def click_depart_from_field(self):
        departure_from_text=self.get_depart_from_field()
        departure_from_text.click()
    
    def select_depart_from_location(self,departlocation):
        self.click_depart_from_field()
        self.get_depart_from_location(departlocation).click()
        

    def click_going_to_field(self):
        going_to_text=self.get_goin_to_field()
        going_to_text.click()
        
    
    def select_going_to_location(self,arrivalLocation, airport):
        self.click_going_to_field()
        self.driver.switch_to.active_element.send_keys(arrivalLocation + Keys.RETURN)
        airport=self.get_going_to_location(airport)
        airport.click()
        

    def click_travel_date_field(self):
        self.get_travel_date_field().click()
    
    def select_travel_date(self,traveldate):
        self.click_travel_date_field()
        self.get_travel_date(traveldate).click()
        
    
    def click_search_btn(self):
        self.get_search_btn().click()
       
        

    def searchflight(self,departlocation,arrivalLocation, arrivalairport,traveldate):
        self.select_depart_from_location(departlocation)
        self.select_going_to_location(arrivalLocation, arrivalairport)
        self.select_travel_date(traveldate)
        self.click_search_btn()
        search_flight_result=SearchResultPage(self.driver)
        return search_flight_result