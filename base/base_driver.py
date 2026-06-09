from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utils import Utils

#reusable methods depends on driver
class Base_Driver:
    def __init__(self,driver):
        self.driver=driver
        self.log=Utils.custom_logger()
        wait= WebDriverWait(driver,20)

    def page_scroll(self):
        self.log.info("inside page scroll")
        while True:
            old_count = self.driver.execute_script("return document.body.scrollHeight")
            self.log.info(f"length before scroll: {old_count}")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            try:
                self.log.info("compairing length and scrolling")
                WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return document.body.scrollHeight") > old_count)
            except:
                break

    def take_screenshots(self,test_name):
        self.driver.save_screenshot(f"screenshots/{test_name}")

    def wait_presence_of_element_located(self,locator_type,locator):
        implicitly_wait= WebDriverWait(self.driver,20)
        return WebDriverWait(self.driver,30).until(EC.presence_of_element_located((locator_type, locator)))
    
    def wait_presence_of_all_elements_located(self,locator_type,locator):
        implicitly_wait= WebDriverWait(self.driver,20)
        return WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located((locator_type, locator)))
   
    def wait_element_to_be_clickable(self,locator_type,locator):
        implicitly_wait= WebDriverWait(self.driver,20)
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((locator_type, locator)))