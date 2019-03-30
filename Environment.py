from selenium import webdriver
import unittest


class Environment(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                      desired_capabilities={"browserName":"chrome"})
            self.driver.get("http://www.google.com")
            print("initiating driver")

        def tearDown(self):
            print("quitting driver")
            self.driver.quit()

