from telnetlib import EC
import csv,re
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.logger import Log
from pages.weblogin import LoginPage

class Darenzx(BasePage):
    shouye_darenzx_loc = (By.XPATH,'//*[@id="app"]/section/div/div/div[3]/div[2]/div/div')  # 首页达人中心
    feishouye_darenzx_loc = (By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div')#非首页的达人中心
    shouye_drzx_jiyangguanli_loc = (By.CLASS_NAME,'el-dropdown-menu__item')#首页达人中心寄样管理
    shouye_shouye_loc = (By.XPATH,'/html/body/div/section/div/div/div[2]/div[1]/span')#首页
    drzx_querenshouhuo_loc = (By.XPATH,"//*[contains(text(),'确认收货')]")#达人中心确认收货
    drzx_querentanchuang_queren_loc = (By.XPATH,"//*[contains(text(),'确认')]")#达人中心确认收货弹窗确认按钮
    drzx_jiyangliebiao_zhuangtai_loc = (By.XPATH,"//*[contains(text(),'已完成')]")#达人中心寄样列表的订单状态
    drzx_jiyangliebiao_dingdanbianhao_loc = (By.CLASS_NAME,'left')  # 达人中心寄样列表的订单编号
    drzx_shenqingbianhaoshurukuang_loc = (By.CLASS_NAME, 'el-input__inner')  # 申请编号输入框
    drzx_jygl_chaxun_loc = (By.XPATH,'//*[@id="app"]/div[2]/section/section/div/div[2]/div/form/span[1]')  # 寄样管理查询按钮



    #点击寄样管理
    def drzx_clickjiyangguanli(self):
        LoginPage(self.driver).darenlogin2('xxx','xxx')
        sleep(2)
        self.mouse_hover(*self.shouye_darenzx_loc)
        sleep(2)
        buts = self.find_elements(*self.shouye_drzx_jiyangguanli_loc)
        sleep(1)
        el = buts[1]
        print(el)
        el.click()
        sleep(5)
    #获取寄样单号
    def drzx_getjiyangbianhao(self):
        self.qiehuannew()
        self.driver.execute_script('window.scrollBy(0,200)')
        sleep(1)
        el = self.find_elements(*self.drzx_jiyangliebiao_dingdanbianhao_loc)
        print(el)
        element = el[8].text
        print(element)
        list = element
        list = list.strip('')
        l = re.findall(r'\d+|[a-z]', list)
        res = ''.join(l)
        #打开csv文件
        self.logger.info('打开csv文件')
        f = open(r'D:\test\xiangbobo\testdata\shangpinbinahao.csv', 'w', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(["bianhao"])
        self.logger.info('写入csv文件')
        csv_writer.writerow([res])

    #确认收货
    def drzx_querenshouhuo(self):
        sleep(1)
        self.qiehuannew()
        sleep(1)
        jybh = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\shangpinbinahao.csv')
        bh = jybh[1]
        sleep(3)
        try:
            self.swipe_youohua()
        finally:
            texts = self.find_elements(*self.drzx_shenqingbianhaoshurukuang_loc)
            texts[2].clear()
            texts[2].send_keys(bh)
            sleep(1)
            self.click_button(*self.drzx_jygl_chaxun_loc)
            sleep(2)
            el = self.find_elements(*self.drzx_querenshouhuo_loc)
            print(el)
            element = el[0]
            element.click()
            sleep(3)
            #确认收货弹窗点击确认
            self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/button[2]/span').click()
            sleep(5)
            texts = self.find_elements(*self.drzx_jiyangliebiao_zhuangtai_loc)
            sleep(1)
            el = texts[0]
            print(el.text)
            return el.text


