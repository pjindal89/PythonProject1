import pytest

from developer import HTMLTestRunner
from pages.homePage import HomePage
from action.ActionBase import ActionBase


@pytest.mark.usefixtures("onettimeexecution")
class TestHomePage():

    @pytest.fixture(autouse=True)
    def objectSetup(self,onettimeexecution):
        self.searchObj = HomePage(self.driver)


    def test_searchProduct(self):
        self.searchObj.searchProduct("iphone")
        self.searchObj.clickSearch()
        if __name__ == "__main__":
            HTMLTestRunner.main()
        # self.ss.screenShot(self.driver)

