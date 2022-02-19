import os
import sys

from nbconvert import export
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
import sys

class ActionBase():
    def __init__(self, browser):
        self.browser = browser
        print("Inside constructor for webdriver")

    def initializewebdriver(self):
        # sys.stdout.flush()

        if self.browser.lower() == "chrome":
            # driver = webdriver.Chrome(ChromeDriverManager().install())
            path=os.getcwd()+"/browserDrivers/chromedriver.exe"
            print("webdriver path"+os.getcwd()+"/browserDrivers/chromedriver.exe")
            driver = webdriver.Chrome(path)
            print("chrome")
        elif self.browser.lower() == "edge":
            driver = webdriver.Ie(IEDriverManager().install())
            print("edge")
            # self.driver=webdriver.Edge()

        else:
            print("error")
            # self.driver = webdriver.Ie()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://www.amazon.com/")
        return driver




