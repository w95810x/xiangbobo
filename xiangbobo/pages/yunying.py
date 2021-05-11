from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

from pages.basepage import BasePage
from selenium.webdriver.common.by import By
class Yunyinght(BasePage):
    ht_loninname = (By.XPATH,'//*[@id="app"]/div/div/form/div[1]/div/div[1]/input')
    ht_loginpwd = (By.XPATH,'//*[@id="app"]/div/div/form/div[2]/div/div[1]/input')
    ht_caiwuguanli_loc = (By.CLASS_NAME,'el-icon-shopping-cart-full')
    ht_xianxiashoukuan_loc = (By.XPATH, "//*[contains(text(),'线下收款明细')]")
    ht_spbh_loc = (By.CLASS_NAME,'cell')
    ht_caozuo_loc = (By.CLASS_NAME,'cell')
    ht_caozuo_querenshoukuan_loc = (By.XPATH,'/html/body/ul/li')
    ht_caozuo_querenskshurukuang_loc = (By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/form/div/div/div[1]/input')
    ht_querentachaun_queren_loc = (By.XPATH,"//*[contains(text(),'提交')]")
    def yyht_login(self):
        try:
            self.open_url('http://xxxxx#')
        except Exception as e:
            self.logger.info(e)
    def yyht_caiwuguanli(self):
        try:
            self.logger.info("点击财务管理")
            self.click_button(*self.ht_caiwuguanli_loc)
            sleep(2)
            self.click_button(*self.ht_xianxiashoukuan_loc)
        except Exception as e:
            self.logger.info(e)

    def yyht_getspbh(self):
        spbhs = self.find_elements(*self.ht_spbh_loc)
        print(spbhs[15].text)

    #最后一个订单确认付款
    def yyht_querenfukuan(self):
        # je = self.find_elements(*self.ht_spbh_loc)
        # jine = je[19].text
        caozuos = self.find_elements(*self.ht_caozuo_loc)
        caozuo = caozuos[23]
        ActionChains(self.driver).move_to_element(caozuo).perform()
        sleep(1)
        self.click_button(*self.ht_caozuo_querenshoukuan_loc)
        sleep(1)
        self.send_keys(self.ht_caozuo_querenskshurukuang_loc,1)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[3]/span/button[2]/span').click()
        sleep(1)
        self.logger.info("寻找状态")
        zt = self.find_elements(*self.ht_spbh_loc)
        zhuangtai = zt[21]
        print(zhuangtai.text)
        return zt[21].text






