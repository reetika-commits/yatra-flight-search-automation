from email import utils

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.yatra_launch_page import LaunchPage
import pytest
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchAndVerfyFilter:
    @pytest.fixture(autouse=True)
    def class_setup(self):    
        self.lp= LaunchPage(self.driver)
        self.utils=Utils()

    test_data=Utils.read_yaml()['search_data']
    print(f"Test data directory: {test_data}")
    @pytest.mark.parametrize("data",test_data)
    def test_search_flight(self, data):  
        print(f"Test data: {data}")
        search_flight_result=self.lp.searchflight(data["depart_from"], data["going_to"], data["travel_date"])
        search_flight_result.click_stop_flight(data["stops"])
        search_flight_result.page_scroll() 
        list_of_flight=search_flight_result.verify_stops()
        self.utils.assertListItemtext(list_of_flight,data["stops"])