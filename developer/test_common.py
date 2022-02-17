import unittest

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
        ss=Commons(driver)

        ss.screenShot()


    def test_commons(self):
        print("inside test2")
