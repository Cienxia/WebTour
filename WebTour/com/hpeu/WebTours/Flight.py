# coding=utf-8

import time
import unittest
from selenium import webdriver
from com.hpeu.WebTours.Login import Login
from com.hpeu.Tools.ReadFile import ReadFile
from com.hpeu.Tools.GetScreenshot import GetScreenshot


class Flight(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #driver = webdriver.Ie()
        self.GetVule = ReadFile()
        self.getScreenTest = GetScreenshot(self.driver)
    
    def test_WebTourFlight(self):
        
        Login.test_Login(self)
        mydriver = self.driver

        fromPort = self.GetVule.getElement('XPATH', 'DepartFrom')
        toPort = self.GetVule.getElement('XPATH', 'ArrivingIn')
        findFlights = self.GetVule.getElement('XPATH', 'Continue')
        reserveFlights = self.GetVule.getElement('XPATH', 'Continue1')
        
        Inputdepart = self.GetVule.getInputValue('Search', 'depart')
        Inputarrive = self.GetVule.getInputValue('Search', 'arrive')
        
        mydriver.find_element_by_xpath(fromPort).send_keys(Inputdepart)
        mydriver.find_element_by_xpath(toPort).send_keys(Inputarrive)
        mydriver.find_element_by_xpath(findFlights).click()
        mydriver.find_element_by_xpath(reserveFlights).click()

        
        self.getScreenTest.screenshot('Search')
    
        time.sleep(5)
        
        
    def tearDown(self):
        Login.tearDown(self)
        
# if __name__ == '__main__':
#     unittest.main()
# '''     
# if __name__ == '__main__':
#     unittest.main()
# '''        