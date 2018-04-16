# coding =utf-8

import os
import time

'''
class GetScreenshot(object):
    def __init__(self,driver):
        self.driver= driver
        
    def screenshot(self, testcasename, name):
        root_dir = os.path.dirname(os.path.abspath('.'))
        
        
        screenfolder_path = root_dir + "\\..\\..\\screenshots\\" + testcasename
        if not os.path.exists(screenfolder_path):
            os.mkdir(screenfolder_path)
                   
        
        file_name = screenfolder_path + '\\' + name + '_' + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) +'.png'
        self.driver.get_screenshot_as_file(file_name)
'''

class GetScreenshot(object):
    def __init__(self,driver):
        self.driver= driver
        
    def screenshot(self, name):
        root_dir = os.path.dirname(os.path.abspath('.'))
        
        
        screenfolder_path = root_dir + "\\..\\..\\screenshot\\"         
        file_name = screenfolder_path + name + '_' + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) +'.png'
        self.driver.get_screenshot_as_file(file_name)
        
        