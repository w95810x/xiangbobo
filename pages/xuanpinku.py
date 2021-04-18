from pages.basepage import BasePage
from pages.zhaosp import ZSP
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Xpk(BasePage):
    sqjybut_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span')#选品库商品详情申请寄样按钮
    tjjysq_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/span[3]')#选品库商品详情提交寄样按钮
    xxfk_loc = (By.XPATH,'/html/body/div[2]/div/div[3]/div/button[3]/span')#选品库商品详情付款弹窗-线下付款

    def xunzhaosp(self,text):
        texts = self.driver.find_elements_by_class_name('info-name')
        sleep(2)
        for i in texts:
            if i.text == "铁树10":
                self.driver.find_element_by_xpath("(//*[text()='铁树10']").click()
            else:
                self.driver.execute_script('window.scrollBy(0,200)')
                print("没有找到商品")

    def shenqingjy(self):
        sleep(2)
        #滑动到底部
        self.swip_di()
        sleep(2)
        #点击申请寄样按钮
        self.click_button(self.sqjybut_loc)

    #点击提交寄样申请
    def tijiaojysq(self):
        sleep(2)
        #切换到新打开的窗口
        self.qiehuannew()
        sleep(2)
        #滑动到底部
        self.swip_di()
        sleep(3)
        #点击提交寄样申请按钮
        self.click_button(self.tjjysq_loc)
        sleep(2)
    #付款方式-线下付款
    def xianxia(self):
        self.click_button(self.xxfk_loc)

    #线下付款
    def xianxiafk(self):
        # 线下付款页面滑动到底部
        target = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/form[2]/div[1]/div')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)







