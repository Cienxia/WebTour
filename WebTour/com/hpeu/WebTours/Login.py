
import time
import unittest
from selenium import webdriver
from com.hpeu.Tools.ReadFile import ReadFile
from com.hpeu.Tools.GetScreenshot import GetScreenshot


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #driver = webdriver.Ie()
        self.GetVule = ReadFile()
        self.getScreenTest = GetScreenshot(self.driver)

    
    def test_Login(self):
        mydriver = self.driver
        #login page
        SystemURL =self.GetVule.getURL('WebToursSystem', 'SystemURL')
        mydriver.get(SystemURL)
        time.sleep(5)
        
        userName = self.GetVule.getElement('XPATH', 'UsernameInputBox')
        password = self.GetVule.getElement('XPATH', 'PasswordInputBox')
        login = self.GetVule.getElement('XPATH', 'LoginBtn')
        
        Inputname = self.GetVule.getInputValue('Login', 'name')
        Inputpassword = self.GetVule.getInputValue('Login', 'password')
        
        mydriver.find_element_by_xpath(userName).send_keys(Inputname)
        mydriver.find_element_by_xpath(password).send_keys(Inputpassword)
        mydriver.find_element_by_xpath(login).click()
        
        check1 = self.GetVule.getExistElement('CheckPointXpath', 'CheckPoint_SIGN')
        check2 = self.GetVule.getExistElement('CheckPointXpath', 'CheckPoint_Filght')
        
        checkexist1 =self.GetVule.getExistElement('LoignCheckPoint', 'CheckElement1')
        checkexist2 =self.GetVule.getExistElement('LoignCheckPoint', 'CheckElement2')
        
        self.assertEqual(mydriver.find_element_by_xpath(check1).text,checkexist1)
        self.assertEqual(mydriver.find_element_by_xpath(check2).text,checkexist2)

        self.getScreenTest.screenshot("Login")

        #assert 'Register here to join Mercury Tours!' in mydriver.page_source
    
        
        #assert 'Use our Flight Finder to search for the lowest fare on participating airlines' in mydriver.page_source
        
        time.sleep(5)
        
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
'''     
if __name__ == '__main__':
    unittest.main()
'''        