from telnetlib import EC
import csv

from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.logger import Log

class Sjzx(BasePage):
    sjzx_querenfahuo_loc = (By.XPATH,"//*[contains(text(),'确认发货')]")#寄样列表确认发货
    sjzx_jytc_locs = (By.CLASS_NAME,'el-input el-input--small')#寄样弹窗
    sjzx_jytc_ahouyangdizhi_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/div[4]/div/label')#寄样弹窗收货地址
    sjzx_daishouohuo_loc = (By.XPATH,'/html/body/div[1]/div[2]/section/section/div/div[3]/div[2]/div[1]/div[2]/div[5]/div')#订单列表待收货状态
    sjzx_dingdanzhuangtai_loc = (By.XPATH,"//*[contains(text(),'已完成')]")#订单列表订单状态
    sjzx_shenqingbianhaoshurukuang_loc = (By.CLASS_NAME,'el-input__inner')#申请编号输入框
    sjzx_jygl_chaxun_loc = (By.XPATH,'/html/body/div/div[2]/section/section/div/div[2]/div[1]/div/button[1]/span')  # 寄样管理查询按钮


    def sjzx_click_querenfahuo(self):
        jybh = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\shangpinbinahao.csv')
        bh = jybh[1]
        sleep(3)
        try:
            self.swipe_youohua()
        finally:
            sleep(1)
            texts = self.find_elements(*self.sjzx_shenqingbianhaoshurukuang_loc)
            texts[2].clear()
            texts[2].send_keys(bh)
            sleep(1)
            self.click_button(*self.sjzx_jygl_chaxun_loc)
            sleep(1)
            el = self.find_elements(*self.sjzx_querenfahuo_loc)
            print(el)
            element = el[0]
            element.click()
            sleep(3)
        # try:
        #     self.swipe_youohua()
        # finally:
        #     el = self.find_elements(*self.sjzx_querenfahuo_loc)
        #     print(el)
        #     element = el[0]
        #     element.click()
        #     sleep(3)
    def sjzx_fahuotanchuang(self):
        jybh = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\shangpinbinahao.csv')
        bh = jybh[1]
        self.swip_zhidingwz(*self.sjzx_jytc_ahouyangdizhi_loc)
        #输入寄样数量
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/div[5]/div/div/div[1]/input').send_keys(1)
        sleep(1)
        #输入快递单号
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/div[6]/div/div/div/input').send_keys(12345678)
        sleep(1)
        #是否退还选择否
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/div[7]/div/div/div/label[2]/span[1]/span').click()
        sleep(1)
        #寄样说明
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/div[8]/div/div/div/textarea').send_keys('test')
        sleep(1)
        #点击确定
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[3]/button[2]/span').click()
        sleep(3)
        try:
            self.swipe_youohua()
        finally:
            sleep(1)
            texts = self.find_elements(*self.sjzx_shenqingbianhaoshurukuang_loc)
            texts[2].clear()
            texts[2].send_keys(bh)
            sleep(1)
            self.click_button(*self.sjzx_jygl_chaxun_loc)
            sleep(2)
            text = self.get_txt(*self.sjzx_daishouohuo_loc)
            sleep(2)
            print(text)
        return text

    #获取订单状态
    def sjzx_dingdanzhuangtai(self):
        jybh = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\shangpinbinahao.csv')
        bh = jybh[1]
        texts = self.find_elements(*self.sjzx_shenqingbianhaoshurukuang_loc)
        texts[2].clear()
        texts[2].send_keys(bh)
        sleep(1)
        self.click_button(*self.sjzx_jygl_chaxun_loc)
        sleep(2)
        texts = self.find_elements(*self.sjzx_dingdanzhuangtai_loc)
        sleep(1)
        el = texts[0]
        print(el.text)
        return el.text




