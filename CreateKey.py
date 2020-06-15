# -*- coding: utf-8 -*-

import urllib.request
from selenium import webdriver
import time


class CreateKey(object):
    
    def __init__(self):
        self._result = ''
        self._driver = ''
        
    def get_ipExterno(self):
        site = urllib.request.urlopen('https://icanhazip.com/')
        ip_Number = site.read().decode()
    
        return ip_Number
    
    def login(self):
        browser = webdriver.Chrome()
        browser.get("https://developer.clashroyale.com/") 
        time.sleep(3)
        browser.find_element_by_link_text("Log In").click()
        time.sleep(3)
    
        username = browser.find_element_by_id("email")
        password = browser.find_element_by_id("password")
        username.send_keys("douglas2012.ribeiro@gmail.com")
        password.send_keys("TestePrime")
        login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
    
        self._driver = browser
    
    def SaveKey(self,browser, name, obs):
        ipExt = self.get_ipExterno()
    
        #Acessar menu My Account
        time.sleep(3)
        myAccount = self._driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/header/div/div/div[3]/div/div/ul/li[1]/a")
        self._driver.execute_script("arguments[0].click();", myAccount)
        
        #Clicar Create New Key
        self._driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/section[2]/div/div/div[2]/p/a/span[2]").click()
    
        #Preencher infos
        keyName = self._driver.find_element_by_id("name")
        desc = self._driver.find_element_by_id("description")
        ipField = self._driver.find_element_by_id("range-0")
    
        keyName.send_keys(name)
        desc.send_keys(obs)
        ipField.send_keys(ipExt)
    
        #Criar Chave
        self._driver.find_element_by_xpath("//*[@type='submit']")
        
        #get Key
        time.sleep(1)
        elem = self._driver.find_element_by_xpath("//h4[@class='api-key__name' and text()='" + name + "']")
        self._driver.execute_script("arguments[0].click();", elem)
        time.sleep(1)
        
        strKey = self._driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/section/div/div/div[2]/form/div[1]/div/samp").text
        
        #Salvando Arquivo
        with open("Key_"+ name,'w') as arq:
            arq.write(strKey)
        
        print("Chave gerada com sucesso.")

        self._result = strKey