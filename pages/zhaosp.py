from pages.basepage import BasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class ZSP(BasePage):
    search_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[2]/div/input')#搜索输入框
    searchbut_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[2]/div/div')#搜索按钮
    spmc_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[7]/ul/li[2]/div[2]/p')#商品名称
    sqjy_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[7]/ul/li[2]/div[1]/div[1]/div/span[1]')#商品“菊花”的xpath地址
    tjjysq_loc = (By.XPATH,"//*[contains(text(),'提交寄样申请')]")#提交寄样申请
    zsp_xxfk_loc = (By.XPATH,"//*[contains(text(),'线下付款')]")#线下付款
    zsp_fktc_username_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[2]/div/div/div/input')#付款弹窗-付款户名
    zsp_fktc_khyh_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[3]/div/div/div/input')  # 付款弹窗-开户银行
    zsp_fktc_fkzh_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[4]/div/div/div/input')  # 付款弹窗-付款账号
    zsp_fktc_fkrq_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[5]/div/div/div/input')  # 付款弹窗-付款日期
    zsp_fktc_clickfkqi_loc = (By.XPATH,"//*[contains(text(),1)]")#付款弹窗选择日期
    zsp_fktc_beizhu_loc = (By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/form[2]/div[6]/div/div/div/textarea')#付款弹窗备注
    zsp_fktc_queding_loc = (By.CLASS_NAME,'el-button el-button--primary el-button--small')  # 付款弹窗-付款方信息
    zsp_fktc_fkfxx_loc = (By.XPATH, "//*[contains(text(),'付款方信息')]")  # 付款弹窗-付款方信息
    zsp_fktc_loc = (By.XPATH,'/html/body/div[5]/div/div[3]/button/span')#反馈弹窗-好的


    #点击搜索按钮
    def zsp_search_click(self):
        self.click_button(self.searchbut_loc)

    def zsp_sssp(self,spname):
        self.send_keys(self.search_loc,spname)
        self.zsp_search_click()
        sleep(5)
        self.driver.execute_script('window.scrollBy(0,500)')
        sleep(3)
        texts = self.driver.find_elements(By.CLASS_NAME,'merchandiseItem__text-name')
        sleep(2)
        for i in texts:
            if i.text == spname:
                self.driver.find_element_by_xpath("//*[contains(text(),spname)]").click()
                break
            # elif i.text != spname:
            #     self.driver.execute_script('window.scrollBy(0,200)')
            #     self.driver.find_element_by_xpath("//*[contains(text(),spname)]").click()
            else:
                print("没有找到商品")

    #点击商品的寄样申请
    def zsp_click_jysq(self):
        self.mouse_hover(self.spmc_loc)
        sleep(3)
        self.click_button(self.sqjy_loc)
        sleep(2)
    #提交寄样申请
    def zsp_tjjysq(self):
        self.swip_di()
        self.click_button(self.tjjysq_loc)
        sleep(3)

    #点击下线付款
    def zsp_click_xianxiafk(self):
        self.click_button(self.zsp_xxfk_loc)

    #付款弹窗填写付款信息-付款用户名
    def zsp_input_username(self,name):
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[2]/div/div/div[1]/input').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[2]/div/div/div[1]/input').send_keys("test")
        sleep(5)
    #付款弹窗填写付款信息-开户银行
    def zsp_input_kaihuyh(self,name):
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[3]/div/div/div[1]/input').send_keys("test123")

    #付款弹窗填写付款信息-付款账号
    def zsp_input_fkzh(self,index):
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[4]/div/div/div/input').send_keys(1234567890123456789)

    #付款弹窗填写付款信息-付款日期
    def zsp_click_fkrq(self):
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[5]/div/div/div/input').send_keys('2021-04-17')

    #选择日期
    def zsp_input_rq(self):
        self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[5]/div/span').click()

    #填写备注
    def zsp_input_beizhu(self,text):
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[6]/div/div/div/textarea').send_keys("test123")


    #点击确定按钮
    def zsp_clickqueding(self):
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/button[2]/span').click()
        sleep(5)

    #付款结反馈弹窗
    def zsp_fktc(self):
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button/span').click()

    #填写付款信息
    def zsp_input_fkxx(self):
        self.zsp_click_xianxiafk()
        sleep(2)
        self.qiehuannew()
        self.swip_zhidingwz(self.zsp_fktc_fkfxx_loc)
        sleep(5)
        self.zsp_input_username("xxxxx")
        self.zsp_input_kaihuyh('xxxxxx')
        self.zsp_input_fkzh(1234567890123456789)
        self.zsp_click_fkrq()
        self.zsp_input_beizhu('testtesttest')
        self.zsp_clickqueding()
        self.zsp_fktc()
        sleep(5)



