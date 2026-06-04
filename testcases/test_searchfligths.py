from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.yatra_launch_page import LaunchPage
import pytest


from pages.yatra_search_filght_result import SearchResultPage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchAndVerfyFilter:
    def test_search_flights(self):
        print(self.driver.title)

    @pytest.fixture(autouse=True)
    def class_setup(self):    
        self.lp= LaunchPage(self.driver)
        self.utils=Utils()

    def test_search_flight(self):   
        print("before depart from")
        # remove airport concept and pass only location name should be airport name in the locators and methods
        search_flight_result=self.lp.searchflight("Mumbai","New york","JFK","24/June/2026")
        search_flight_result.click_stop_flight("1")
        print("before page scroll")
        search_flight_result.page_scroll() 

        ############refactored code for assertion of filter
        list_0f_stops=search_flight_result.wait_presence_of_all_elements_located(By.XPATH,"//span[contains(text(),'1 Stop') or contains(text(),'2') or " \
        "contains(text(),'Non Stop')]")
        print("before assert list item text")
        
        self.utils.assertListItemtext(list_0f_stops,"1 Stop")