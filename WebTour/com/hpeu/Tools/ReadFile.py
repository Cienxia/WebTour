# coding=utf-8


import os
import configparser

class ReadFile():
    def getURL(self,section, option):
        root_dir=os.path.dirname(os.path.abspath('.'))
        
        #result is WebTours\com\hpeu
        
        #print("!!!!")
        config = configparser.ConfigParser()
        file_path = root_dir + '\\..\\..\\resources\\Configuration.properties'
        
       
        config.read(file_path)
        
        #print(config.sections())
        #print(config.options(config.sections))
        
        URL = config.get(section, option)
        return URL
    
    def getElement(self,section,option):
        root_dir=os.path.dirname(os.path.abspath('.'))
        file_path = root_dir + '\\..\\..\\resources\\PageElement.properties'
        #result is WebTours\com\hpeu
        
        #print("!!!!")
        config = configparser.ConfigParser()

        config.read(file_path)
        
        #print(config.sections())
        #print(config.options(config.sections))
        
        Element = config.get(section, option)
        return Element
    
    def getInputValue(self,section,option): 
        curpath = os.path.dirname(os.path.abspath("."))
        file_path = curpath + "\\..\\..\\resources\\Inputdata.properties"
        config = configparser.ConfigParser()
        config.read(file_path)
        InputElement = config.get(section, option)
        return InputElement
    
    def getExistElement(self,section,option):
        curpath = os.path.dirname(os.path.abspath("."))
        file_path = curpath + "\\..\\..\\resources\\ExistElement.properties"
        config = configparser.ConfigParser()
        config.read(file_path)
        ExistElement = config.get(section, option)
        return ExistElement
    
        