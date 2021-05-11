from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.logger import Log
from pages.basepage import BasePage
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    logger = Log(logger='weblogiin').get_log()
    loginbut_loc = (By.CLASS_NAME,'login__btn')#首页登录按钮
    username_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[1]/div/div/input')#登录用户名输入框
    pwd_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[2]/div/div/input')#登录密码输入昂
    swichbut_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[3]/div/div/div[3]/div')#登录滑动按钮
    login_loc = (By.XPATH,'//*[@id="pane-1"]/div[1]/button/span')#登录弹窗底部登录按钮
    xuanpk_loc = (By.CLASS_NAME,'text')#首页选品库tab
    zhaosp_loc = (By.XPATH,'//*[@id="app"]/section/div/div/div[2]/div[2]/span')#首页找商品tab
    LG_darenzx_loc = (By.XPATH,'//*[@id="app"]/section/div/div/div[3]/div[2]/div/div')#首页达人中心
    LG_drzx_zhgl_loc = (By.CLASS_NAME,'el-dropdown-menu__item')#首页达人中心账户管理
    drzx_username_loc = (By.XPATH,'//*[@id="app"]/div[2]/section/section/div/div[1]/div[2]/div[4]')#达人中心-账户管理-用户名称
    loginmame_error_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[1]/div/div[2]')#登录页-用户名错误提示
    loginpwd_error_loc = (By.XPATH, '//*[@id="pane-1"]/form/div[2]/div/div[2]')# 登录页-密码错误提示
    loginswipe_error_loc = (By.XPATH,'//*[@id="pane-1"]/form/div[3]/div/div[2]')  # 登录页-滑动校验错误提示
    login_touxiang_loc = (By.CLASS_NAME,'el-image')
    login_tuchudenglu_loc = (By.XPATH,'/html/body/div[2]/div[1]/span')
    login_tuchutanchuang_queren_loc = (By.XPATH,'/html/body/div[3]/div/div[3]/div/button[2]/span')
    login_shangjiazhongxin_loc = (By.XPATH,'/html/body/div[1]/section/div/div/div[3]/div[1]/div/div')
    url = r"http://xxxxxx"

    #达人登录
    def darenlogin(self,name,pwd):
        self.logger.info('打开网址')
        self.openurl(self.url)
        sleep(8)
        try:
            touxiangs = self.find_elements(*self.login_touxiang_loc)
            print(touxiangs)
            touxiang = touxiangs[0]
            ActionChains(self.driver).move_to_element(touxiang).perform()
            sleep(2)
            self.click_button(*self.login_tuchudenglu_loc)
            sleep(1)
            self.click_button(*self.login_tuchutanchuang_queren_loc)
            sleep(1)
        finally:
            self.logger.info('点击登录按钮')
            #点击首页登录按钮
            self.login_click()
            sleep(8)
            self.logger.info('输入用户名')
            #输入用户名
            self.send_user_name(name)
            self.logger.info('输入密码')
            #输入密码
            self.send_user_pwd(pwd)
            sleep(1)
            self.logger.info('滑动验证按钮')
            #滑动验证按钮
            self.swipe_btn()
            sleep(2)
            #滑动至底部
            self.swip_di()
            sleep(3)
            self.logger.info('点击登录按钮')
            #点击登录页登录按钮
            self.click_login_btn()
            sleep(5)
            self.mouse_hover(*self.LG_darenzx_loc)
            sleep(3)
            el = self.find_elements(*self.LG_drzx_zhgl_loc)
            print(el)
            sleep(1)
            el[0].click()
            # try:
            #     el = self.driver.find_elements_by_class_name('el-dropdown-menu__itm')
            #     el[0].click()
            # except Exception as e:
            #     self.logger.info(e)
            sleep(3)
            self.qiehuannew()
            sleep(1)
            print(self.get_txt(*self.drzx_username_loc))
            return self.get_txt(*self.drzx_username_loc)

    def darenlogin2(self, name, pwd):
        self.logger.info('打开网址')
        self.openurl(self.url)
        sleep(8)
        try:
            touxiangs = self.find_elements(*self.login_touxiang_loc)
            print(touxiangs)
            touxiang = touxiangs[0]
            ActionChains(self.driver).move_to_element(touxiang).perform()
            sleep(2)
            self.click_button(*self.login_tuchudenglu_loc)
            sleep(1)
            self.click_button(*self.login_tuchutanchuang_queren_loc)
            sleep(1)
        finally:
            self.logger.info('点击登录按钮')
            # 点击首页登录按钮
            self.login_click()
            sleep(8)
            self.logger.info('输入用户名')
            # 输入用户名
            self.send_user_name(name)
            self.logger.info('输入密码')
            # 输入密码
            self.send_user_pwd(pwd)
            sleep(1)
            self.logger.info('滑动验证按钮')
            # 滑动验证按钮
            self.swipe_btn()
            sleep(2)
            # 滑动至底部
            self.swip_di()
            sleep(3)
            self.logger.info('点击登录按钮')
            # 点击登录页登录按钮
            self.click_login_btn()
            sleep(5)
    #用户名为空
    def login_namenull(self,name,pwd):
        self.openurl(self.url)
        sleep(8)
        try:
            touxiangs = self.find_elements(*self.login_touxiang_loc)
            print(touxiangs)
            touxiang = touxiangs[0]
            ActionChains(self.driver).move_to_element(touxiang).perform()
            sleep(2)
            self.click_button(*self.login_tuchudenglu_loc)
            sleep(1)
            self.click_button(*self.login_tuchutanchuang_queren_loc)
            sleep(1)
        finally:
            #点击首页登录按钮
            self.login_click()
            sleep(8)
            #输入验证码
            self.send_user_name(name)
            #输入密码
            self.send_user_pwd(pwd)
            sleep(1)
            #滑动验证按钮
            self.swipe_btn()
            sleep(2)
            #滑动至底部
            self.swip_di()
            sleep(3)
            #点击登录页登录按钮
            self.click_login_btn()
            sleep(5)
            print(self.get_txt(*self.loginmame_error_loc))
            return self.get_txt(*self.loginmame_error_loc)

    def login_nameerror(self,name,pwd):
        self.openurl(self.url)
        sleep(8)
        try:
            touxiangs = self.find_elements(*self.login_touxiang_loc)
            print(touxiangs)
            touxiang = touxiangs[0]
            ActionChains(self.driver).move_to_element(touxiang).perform()
            sleep(2)
            self.click_button(*self.login_tuchudenglu_loc)
            sleep(1)
            self.click_button(*self.login_tuchutanchuang_queren_loc)
            sleep(1)
        finally:
            #点击首页登录按钮
            self.login_click()
            sleep(8)
            #输入验证码
            self.send_user_name(name)
            #输入密码
            self.send_user_pwd(pwd)
            sleep(1)
            #滑动验证按钮
            self.swipe_btn()
            sleep(2)
            #滑动至底部
            self.swip_di()
            sleep(3)
            #点击登录页登录按钮
            self.click_login_btn()
            locator = (By.XPATH,'/html/body/div[2]/p')
            # 显示等待获取元素
            WebDriverWait(self.driver,1,0.2).until(EC.presence_of_element_located(locator))
            # 获取toast
            t = self.find_element(*locator).text
            print(t)
            return t

    def login_pwderror(self,name,pwd):
        self.openurl(self.url)
        sleep(8)
        try:
            touxiangs = self.find_elements(*self.login_touxiang_loc)
            print(touxiangs)
            touxiang = touxiangs[0]
            ActionChains(self.driver).move_to_element(touxiang).perform()
            sleep(2)
            self.click_button(*self.login_tuchudenglu_loc)
            sleep(1)
            self.click_button(*self.login_tuchutanchuang_queren_loc)
            sleep(1)
        finally:
            #点击首页登录按钮
            self.login_click()
            sleep(8)
            #输入验证码
            self.send_user_name(name)
            #输入密码
            self.send_user_pwd(pwd)
            sleep(1)
            #滑动验证按钮
            self.swipe_btn()
            sleep(2)
            #滑动至底部
            self.swip_di()
            sleep(3)
            #点击登录页登录按钮
            self.click_login_btn()
            sleep(5)
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.loginpwd_error_loc))
            print(self.get_txt(*self.loginpwd_error_loc))
            return self.get_txt(*self.loginpwd_error_loc)
    #滑动按钮提示
    def login_swipeTips(self,name,pwd):
        self.openurl(self.url)
        sleep(8)
        try:
            touxiangs = self.find_elements(*self.login_touxiang_loc)
            print(touxiangs)
            touxiang = touxiangs[0]
            ActionChains(self.driver).move_to_element(touxiang).perform()
            sleep(2)
            self.click_button(*self.login_tuchudenglu_loc)
            sleep(1)
            self.click_button(*self.login_tuchutanchuang_queren_loc)
            sleep(1)
        finally:
            #点击首页登录按钮
            self.login_click()
            sleep(8)
            #输入验证码
            self.send_user_name(name)
            #输入密码
            self.send_user_pwd(pwd)
            sleep(1)
            #滑动验证按钮
            self.swipe_btn()
            sleep(2)
            #滑动至底部
            self.swip_di()
            sleep(3)
            #点击登录页登录按钮
            self.click_login_btn()
            sleep(5)
            print(self.get_txt(*self.loginswipe_error_loc))
            return self.get_txt(*self.loginswipe_error_loc)


    def shangjialogin(self,name,pwd):
        self.openurl(self.url)
        sleep(8)
        try:
            touxiangs = self.find_elements(*self.login_touxiang_loc)
            print(touxiangs)
            touxiang = touxiangs[0]
            ActionChains(self.driver).move_to_element(touxiang).perform()
            sleep(2)
            self.click_button(*self.login_tuchudenglu_loc)
            sleep(1)
            self.click_button(*self.login_tuchutanchuang_queren_loc)
            sleep(1)
        finally:
            self.login_click()
            sleep(3)
            self.send_user_name(name)
            self.send_user_pwd(pwd)
            self.swipe_btn()
            sleep(2)
            #滑动至底部
            self.swip_di()
            sleep(5)
            self.click_login_btn()
            sleep(2)
    #商家中心点击寄样管理
    def sjzx_click_jygl(self):
        sleep(2)
        self.mouse_hover(*self.login_shangjiazhongxin_loc)
        sleep(1)
        el = self.find_elements(*self.LG_drzx_zhgl_loc)
        print(el)
        sleep(1)
        el[2].click()
        sleep(5)


    def openurl(self,url):
        self.open_url(url)

    #首页点击登录
    def login_click(self):
        self.click_button(*self.loginbut_loc)

    def send_user_name(self,username):
        name_input = '//*[@id="pane-1"]/form/div[1]/div/div/input'
        self.send_keys(self.username_loc,username)

    def send_user_pwd(self,userpwd):
        self.send_keys(self.pwd_loc,userpwd)

    #滑动校验按钮
    def swipe_btn(self):
        button = self.find_element(*self.swichbut_loc)
        action = ActionChains(self.driver)
        action.click_and_hold(button).perform()
        sleep(1)
        action.move_by_offset(400, 0).perform()
        action.reset_actions()
    # 点击 登录按钮
    def click_login_btn(self):
        login_btn = '//*[@id="pane-1"]/div[1]/button/span'
        self.click_button(*self.login_loc)
        sleep(2)

    #点击选品库
    def xuanpk_click(self):
        self.click_button(*self.xuanpk_loc)

    #点击找商品
    def zhaosp_click(self):
        sleep(2)
        self.click_button(*self.zhaosp_loc)
        sleep(3)

