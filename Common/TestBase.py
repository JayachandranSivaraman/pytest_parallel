from Environment import *

class TestBase(Environment):

    def find_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)

        except Exception as e:
            print("Exception occured while finding an element")
            print(e)

    def click_element(self,xpath):
        try:
            self.driver.find_element(xpath).click()

        except Exception as e:
            print("Exception occured while clicking an element")
            print(e)

    def assert_element(self,actual,expected):
        try:
            assert actual == expected

        except Exception as e:
            print("--------------------Assertion Failed--------------------")
            print(e)

    def is_displayed(self,xpath):
        try:
            self.driver.find_element(xpath).is_displayed()

        except Exception as e:
            print("Exeception occured may be")




