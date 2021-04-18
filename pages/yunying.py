from time import sleep
from selenium import webdriver
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
class Yunyinght(BasePage):
    ht_loninname = (By.XPATH,'//*[@id="app"]/div/div/form/div[1]/div/div[1]/input')
    ht_loginpwd = (By.XPATH,'//*[@id="app"]/div/div/form/div[2]/div/div[1]/input')
    def ht_login(self):
        self.open_url('xxxxxxxxxxxx')
        sleep(5)
        self.send_keys(self.ht_loninname,'xxxxxxx')
        self.send_keys(self.ht_loginpwd,'xxxxx')


