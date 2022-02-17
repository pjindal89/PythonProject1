import logging
import utilities.custom_logger as cl
from action.Commons import Commons

class HomePage(Commons):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #############Locators#####################
    search_box = "twotabsearchtextbox"
    search_btn = "nav-search-submit-button"

    def searchProduct(self,name):
        # self.driver.find_element_by_id(self.search_box).send_keys(name)
        self.sendkeys(name, self.search_box,"id")
        self.log.info("Entered product in search")

    def clickSearch(self):
        # self.driver.find_element_by_id(self.search_btn).click()
        self.clickObj(self.search_btn,"id")
        self.log.info("Clicked on search")


