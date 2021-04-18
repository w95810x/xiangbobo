from pages.basepage import BasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    loginbut_loc = (By.CLASS_NAME,'login__btn')#首页登录按钮
    username_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[1]/div/div/input')#登录用户名输入框
    pwd_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[2]/div/div/input')#登录密码输入昂
    swichbut_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[3]/div/div/div[3]/div')#登录滑动按钮
    login_loc = (By.XPATH,'//*[@id="pane-1"]/div[1]/button/span')#登录弹窗底部登录按钮
    xuanpk_loc = (By.CLASS_NAME,'text')#首页选品库tab
    zhaosp_loc = (By.XPATH,'//*[@id="app"]/section/div/div/div[2]/div[2]/span')#首页找商品tab


    def darenlogin(self,name,pwd):
        self.openpage()
        sleep(8)
        self.login_click()
        sleep(5)
        self.send_user_name(name)
        self.send_user_pwd(pwd)
        sleep(1)
        self.swich_btn()
        sleep(2)
        #滑动至底部
        self.swip_di()
        sleep(3)
        self.click_login_btn()
        sleep(5)


    def shangjialogin(self,name,pwd):
        self.openpage()
        self.login_click()
        sleep(3)
        self.send_user_name(name)
        self.send_user_pwd(pwd)
        self.swich_btn()
        sleep(2)
        #滑动至底部
        self.swip_di()
        sleep(5)
        self.click_login_btn()
        sleep(2)

    def openpage(self,url):
        self.open_url(url)

    #首页点击登录
    def login_click(self):
        self.click_button(self.loginbut_loc)

    def send_user_name(self, username):
        name_input = '//*[@id="pane-1"]/form/div[1]/div/div/input'
        self.send_keys(self.username_loc,username)

    def send_user_pwd(self, userpwd):
        self.send_keys(self.pwd_loc, userpwd)

    #滑动校验按钮
    def swich_btn(self):
        button = self.find_element(self.swichbut_loc)
        action = ActionChains(self.driver)
        action.click_and_hold(button).perform()
        sleep(1)
        action.move_by_offset(400, 0).perform()
        action.reset_actions()
    # 点击 登录按钮
    def click_login_btn(self):
        login_btn = '//*[@id="pane-1"]/div[1]/button/span'
        self.click_button(self.login_loc)
        sleep(2)

    #点击选品库
    def xuanpk_click(self):
        self.click_button(self.xuanpk_loc)

    #点击找商品
    def zhaosp_click(self):
        self.click_button(self.zhaosp_loc)
        sleep(5)

