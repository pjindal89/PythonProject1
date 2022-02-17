import os
import unittest

import HTMLTestRunner
from Demos.BackupRead_BackupWrite import outfile

# from developer.HTMLTestRunner import Test_HTMLTestRunner
from developer.test_common import TestCommons
from developer.test_practise import TestPractise

def runAll():

    # Get all tests from the test classes
    tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCommons)
    tc2 = unittest.TestLoader().loadTestsFromTestCase(TestPractise)

    # Create a test suite combining all test classes
    smokeTest = unittest.TestSuite([tc1, tc2])

    # unittest.TextTestRunner(verbosity=2).run(smokeTest)
    outfile = open('SmokeTestReport.html', 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        output="\\repots",
        title='Test Report',
        description='This demonstrates the report output by Prasanna.Yelsangikar.'
    )
    # run the suite using HTMLTestRunner
    runner.run(smokeTest)