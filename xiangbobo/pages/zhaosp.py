from telnetlib import EC
import csv
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.logger import Log

class ZSP(BasePage):
    logger = Log(logger='ZSP').get_log()
    search_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[2]/div/input')#搜索输入框
    searchbut_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[2]/div/div')#搜索按钮
    spmc_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[7]/ul/li[1]/div[2]/p')#商品名称
    zsp_spmc_loc = (By.CLASS_NAME,'merchandiseItem__text-name')#商品列表名称
    sqjy_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[7]/ul/li[1]/div[1]/div[1]/div/span[1]')#商品“板砖”的xpath地址
    zsp_baozhengjin_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/span[2]')
    tjjysq_loc = (By.XPATH,"//*[contains(text(),'提交寄样申请')]")#提交寄样申请
    zsp_xxfk_loc = (By.XPATH,"//*[contains(text(),'线下付款')]")#线下付款
    zsp_zfb_loc = (By.XPATH,'//*[@id="app"]/div/div[3]/h3/span')#支付宝付款金额
    zsp_xsfk_loc = (By.XPATH, "//*[contains(text(),'支付宝/微信支付')]")  # 线上付款
    zsp_xxfk_xx = (By.CLASS_NAME,'el-input__inner')#线下付款弹窗输入项elements
    zsp_fktc_username_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[2]/div/div/div')#付款弹窗-付款户名
    zsp_fktc_khyh_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[3]/div/div/div/input')  # 付款弹窗-开户银行
    zsp_fktc_fkzh_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[4]/div/div/div/input')  # 付款弹窗-付款账号
    zsp_fktc_fkrq_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[5]/div/div/div/input')  # 付款弹窗-付款日期
    zsp_fktc_clickfkqi_loc = (By.XPATH,"//*[contains(text(),1)]")#付款弹窗选择日期
    zsp_fktc_beizhu_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[6]/div/div/div/textarea')#付款弹窗备注
    zsp_fktc_queding_loc = (By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/button[2]')  # 付款弹窗-确定
    zsp_fktc_queding1_loc = (By.XPATH,"//*[contains(text(),'确 定')]")  # 付款弹窗-确定
    zsp_fktc_fkfxx_loc = (By.XPATH, "//*[contains(text(),'付款方信息')]")  # 付款弹窗-付款方信息
    zsp_fktc_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div[3]/button[2]')#反馈弹窗-好的
    zsp_cebianlan_loc = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div[2]')  # 招商品页右侧小屏的侧边栏收起按钮
    zsp_fktc_chenggongtanchuangtext_loc = (By.CLASS_NAME,'el-message-box__message')


    #点击搜索按钮
    def zsp_search_click(self):
        self.click_button(*self.searchbut_loc)

    #搜索商品
    def zsp_sssp(self,spname):
        '''搜索商品'''
        try:
            self.click_button(*self.zsp_cebianlan_loc)
        finally:
            self.send_keys(self.search_loc,spname)
            self.zsp_search_click()
            sleep(5)
            self.driver.execute_script('window.scrollBy(0,400)')
            sleep(3)
            self.find_element(*self.spmc_loc)
            return self.get_txt(*self.spmc_loc)

    #点击商品的寄样申请
    def zsp_click_jysq(self):
        sleep(1)
        self.mouse_hover(*self.spmc_loc)
        sleep(3)
        self.click_button(*self.sqjy_loc)
        sleep(2)
    #提交寄样申请
    def zsp_tjjysq(self):
        self.swip_di()
        bzj = self.get_txt(*self.zsp_baozhengjin_loc)
        self.click_button(*self.tjjysq_loc)
        sleep(3)

    #线上上支付
    def zsp_xianshangzhifu_zfb(self):
        self.logger.info('点击线下支付')
        self.click_button(*self.zsp_xsfk_loc)
        sleep(3)
        self.logger.info('切换窗口')
        self.qiehuannew()
        sleep(1)
        self.logger.info('拿出金额')
        return self.get_txt(*self.zsp_zfb_loc)



    #点击下线付款
    def zsp_click_xianxiafk(self):
        self.click_button(*self.zsp_xxfk_loc)

    #付款弹窗填写付款信息-付款用户名
    def zsp_input_username(self,name):
        texts = self.find_elements(*self.zsp_xxfk_xx)
        self.logger.info('点击输入框')
        texts[1].click()
        self.logger.info('输入账户名')
        texts[1].send_keys(name)
        sleep(1)
    #付款弹窗填写付款信息-开户银行
    def zsp_input_kaihuyh(self,name):
        texts = self.find_elements(*self.zsp_xxfk_xx)
        self.logger.info('点击开户银行输入框')
        texts[2].click()
        self.logger.info('输入开户银行')
        texts[2].send_keys(name)
        sleep(1)
    #付款弹窗填写付款信息-付款账号
    def zsp_input_fkzh(self,index):
        texts = self.find_elements(*self.zsp_xxfk_xx)
        self.logger.info('点击付款账号输入框')
        texts[3].click()
        self.logger.info('输入付款账号')
        texts[3].send_keys(index)
        sleep(1)
    #付款弹窗填写付款信息-付款日期
    def zsp_click_fkrq(self,riqi):
        texts = self.find_elements(*self.zsp_xxfk_xx)
        self.logger.info('点击日期')
        texts[4].click()
        self.logger.info('输入日期')
        texts[4].send_keys(riqi)
        sleep(1)
        self.click_button(*self.zsp_fktc_fkfxx_loc)


    #填写备注
    def zsp_input_beizhu(self,text):
        self.driver.find_element(By.CLASS_NAME,'el-textarea__inner').send_keys(text)

    #点击确定按钮
    def zsp_clickqueding(self):
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/button[2]/span').click()


    #付款结反馈弹窗
    def zsp_fktc(self):
        self.qiehuannew()
        sleep(2)
        text1 = self.driver.find_element_by_class_name('el-message-box__content').text
        print(text1)
        # text2 = self.driver.find_element_by_class_name('el-message-box__message').text
        try:
            self.driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button/span').click()
        except:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/button[2]').click()
        return text1



    #填写付款信息
    def zsp_input_fkxx(self):
        self.zsp_click_xianxiafk()
        sleep(1)
        self.swip_zhidingwz(*self.zsp_fktc_fkfxx_loc)
        sleep(3)
        self.logger.info('输入帐户名')
        self.zsp_input_username("xxxxx")
        self.logger.info('输入开户行')
        self.zsp_input_kaihuyh('xxxxxx')
        self.zsp_input_fkzh(1234567890123456789)
        sleep(1)
        tm = self.get_time()
        self.zsp_click_fkrq(tm)
        self.zsp_input_beizhu('testtesttest')
        self.zsp_clickqueding()
        text = self.zsp_fktc()
        sleep(5)
        return text

        # self.driver.execute_script('window.scrollBy(0,300)')
        # #刷新
        # self.driver.refresh()
        # sleep(3)
        # self.logger.info('点击商品名称')
        # names = self.driver.find_elements_by_class_name('cursor')
        # names[0].click()
        # sleep(5)
        # self.qiehuannew()
        # sleep(2)
        # self.driver.execute_script('window.scrollBy(0,500)')
        # sleep(1)
        # texts = self.driver.find_elements_by_class_name('merchandiseBasicInfo__list__item-value')
        # text = texts[12].text
        # f = open(r'D:\xiangbobo\testdata\resuitdata.csv', 'w', encoding='utf-8')
        # csv_writer = csv.writer(f)
        # csv_writer.writerow(["resuitdata"])
        # csv_writer.writerow([text])







