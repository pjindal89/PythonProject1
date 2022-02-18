import subprocess

import pytest

from action.ActionBase import ActionBase
from action.Commons import Commons


@pytest.fixture(scope="class")
# def onettimeexecution(request):
    print("inside fixture")
    # subprocess.call("TASKKILL /f /IM CHROME.EXE")
    wd = ActionBase("chrome")
    request.cls.driver = wd.initializewebdriver()
    ss = Commons(request.cls.driver)
    print("Starting execution of test now")
    yield
    print("Closing browser sessions")
    request.cls.driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")