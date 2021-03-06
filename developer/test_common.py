import sys
import unittest

import allure
import pytest
import logging

from action.ActionBase import ActionBase
from action.Commons import Commons
import utilities.custom_logger as cl


@pytest.mark.usefixtures("onettimeexecution")
class TestCommons(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    def test_zcommons(self):
        # print("inside fixture")
        # # subprocess.call("TASKKILL /f /IM CHROME.EXE")
        wd = ActionBase("chrome")
        driver = wd.initializewebdriver()
        # print("Starting execution of test now")
        self.log.debug("inside test1")
        sys.stdout.flush()
        ss=Commons(driver)

        # ss.screenShot()
        allure.attach(driver.get_screenshot_as_png(),name="commons file",attachment_type=allure.attachment_type.PNG)

    @allure.step("Just printing")
    def test_commons(self):
        print("inside test2")
