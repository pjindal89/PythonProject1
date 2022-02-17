import unittest
import HTMLTestRunner
import pytest

from action.ActionBase import ActionBase


@pytest.mark.usefixtures("onettimeexecution")
class TestPractise(unittest.TestCase):

    def test_practise(self):
        print("inside test class")
        if __name__ == '__main__':
            unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='example_dir'))
