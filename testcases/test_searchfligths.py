from email import utils

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.yatra_launch_page import LaunchPage
import pytest


from pages.yatra_search_filght_result import SearchResultPage
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchAndVerfyFilter:
    
    @pytest.fixture(autouse=True)
    def class_setup(self):    
        self.lp= LaunchPage(self.driver)
        self.utils=Utils()

    def test_search_flight(self):   
        search_flight_result=self.lp.searchflight("Mumbai","JFK","24/June/2026")
        search_flight_result.click_stop_flight("1")
        search_flight_result.page_scroll() 
        list_of_flight=search_flight_result.verify_stops()
        self.utils.assertListItemtext(list_of_flight,"1 Stop")