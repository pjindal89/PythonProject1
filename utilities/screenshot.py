import os
import time
from traceback import print_stack


def screenShot(self):
    """
    Takes screenshot of the current open web page
    """
    fileName = "abc" + "." + str(round(time.time() * 1000)) + ".png"
    screenshotDirectory = "../screenshots/"
    relativeFileName = screenshotDirectory + fileName
    currentDirectory = os.path.dirname(__file__)
    destinationFile = os.path.join(currentDirectory, relativeFileName)
    destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

    try:
        if not os.path.exists(destinationDirectory):
            os.makedirs(destinationDirectory)
        self.driver.save_screenshot(destinationFile)
        # self.log.info("Screenshot save to directory: " + destinationFile)
    except:
        print("### Exception Occurred when taking screenshot")
        print_stack()