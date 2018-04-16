import unittest
import time
from com.hpeu.WebTours.Flight import Flight
from selenium import webdriver
from com.hpeu.Tools.ReadFile import ReadFile
from com.hpeu.Tools.GetScreenshot import GetScreenshot
class Order(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue=ReadFile()
        self.getScreenTest = GetScreenshot(self.driver)
    def test_Order(self):
        mydriver = self.driver
        Flight.test_WebTourFlight(self)
        
        passFirst0 = self.getValue.getElement("XPATH", "FirstName")
        passLast0 = self.getValue.getElement("XPATH", "LastName")
        creditnumber = self.getValue.getElement("XPATH", "Number")
        Purchase = self.getValue.getElement("XPATH", "Purchase")
        
        Inputfirstname = self.getValue.getInputValue('Order', 'firstname')
        Inputlastname = self.getValue.getInputValue('Order', 'lastname')
        Inputnumber = self.getValue.getInputValue('Order', 'number')

        mydriver.find_element_by_xpath(passFirst0).send_keys(Inputfirstname)
        mydriver.find_element_by_xpath(passLast0).send_keys(Inputlastname)
        mydriver.find_element_by_xpath(creditnumber).send_keys(Inputnumber)
        mydriver.find_element_by_xpath(Purchase).click()

        time.sleep(5)
        self.getScreenTest.screenshot("Order")
        
    def tearDown(self):
        Flight.tearDown(self)
        
    if __name__ == '__main__':
        unittest.main()