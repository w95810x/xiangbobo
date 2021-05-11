from time import sleep
from pages.darenzhongxin import Darenzx
from selenium.webdriver import ActionChains
from pages.shangjiazhongxin import Sjzx
from pages.zhaosp import ZSP
from pages.basepage import BasePage
from pages.weblogin import LoginPage
from pages.xuanpinku import Xpk
from pages.yunying import Yunyinght
from common.send_email import Email
from cases import daren
from cases import shangjia
import unittest,time,re,os
from PIL import Image, ImageEnhance
from selenium import webdriver
from common.logger import Log
from HTMLTestRunner import HTMLTestRunner



class Testcase(unittest.TestCase):
    logger = Log(logger='TestLogin').get_log()

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument(r"user-data-dir=C:\Users\EDZ\AppData\Local\Google\Chrome\User Data1")
        self.logger.info('------开始执行测试用例------')
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()


    #达人登录
    def test_login(self):
        '''达人登录，并校验登录后的账户名称'''
        data = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\login.csv')
        name = data[0][0]
        pwd = data[0][1]
        exp = data[0][2]
        name = LoginPage(self.driver).darenlogin(name,pwd)
        self.assertEqual(name,exp)

    def test_login_namenull(self):
        '''账号为空登录name:取得是testdatalogin里的用户名，pwd:同名字，exp：取得也是logintata里的预期结果'''
        data = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\login.csv')
        name = data[1][0]
        pwd = data[1][1]
        exp = data[1][2]
        text = LoginPage(self.driver).login_namenull(name,pwd)
        self.assertEqual(text,exp)

    def test_login_nameerror(self):
        '''用户名错误登录'''
        data = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\login.csv')
        name = data[2][0]
        pwd = data[2][1]
        exp = data[2][2]
        text = LoginPage(self.driver).login_nameerror(name, pwd)
        self.assertEqual(text,exp)

    def test_login_pwderror(self):
        '''密码错误登录'''
        data = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\login.csv')
        name = data[3][0]
        pwd = data[3][1]
        exp = data[3][2]
        text = LoginPage(self.driver).login_pwderror(name,pwd)
        self.assertEqual(text,exp)

    def test_login_swipetips(self):
        '''密码为空登录验证滑块提示'''
        data = BasePage(self.driver).getCsvData(r'D:\test\xiangbobo\testdata\login.csv')
        name = data[4][0]
        pwd = data[4][1]
        exp = data[4][2]
        text = LoginPage(self.driver).login_swipeTips(name,pwd)
        self.assertEqual(text,exp)

    def test_jiyang_xianshangzhifu(self):
        '''支付宝支付'''
        LoginPage(self.driver).darenlogin('xxx','xxx')
        sleep(3)
        LoginPage(self.driver).xuanpk_click()
        LoginPage(self.driver).zhaosp_click()
        text = ZSP(self.driver).zsp_sssp('板砖')
        self.assertEqual(text,'板砖')
        ZSP(self.driver).zsp_click_jysq()
        ZSP(self.driver).zsp_tjjysq()
        self.assertEqual(ZSP(self.driver).zsp_xianshangzhifu_zfb(),'1 元')
        # ZSP(self.driver).zsp_input_fkxx()

    def test_jiyang_xianxiazhifu(self):
        '''线下支付'''
        exp = '''已收到您的汇款，请等待反馈结果
付款成功后合作自动执行'''
        LoginPage(self.driver).darenlogin('xxx', 'xxx')
        sleep(3)
        LoginPage(self.driver).xuanpk_click()
        LoginPage(self.driver).zhaosp_click()
        text = ZSP(self.driver).zsp_sssp('板砖')
        self.assertEqual(text,'板砖')
        ZSP(self.driver).zsp_click_jysq()
        ZSP(self.driver).zsp_tjjysq()
        self.assertEqual(ZSP(self.driver).zsp_input_fkxx(),exp)
        Darenzx(self.driver).drzx_getjiyangbianhao()

    def test_houtai_querenfukuan(self):
        # data = BasePage(self.driver).getCsvData(r'D:\xiangbobo\testdata)
        # data = data[1]
        Yunyinght(self.driver).yyht_login()
        sleep(2)
        Yunyinght(self.driver).yyht_caiwuguanli()
        sleep(2)
        Yunyinght(self.driver).yyht_getspbh()
        self.assertEqual(Yunyinght(self.driver).yyht_querenfukuan(),'已到账')

    def test_shangjia_querenshouhuo(self):
        LoginPage(self.driver).shangjialogin('xxx','xxx')
        LoginPage(self.driver).sjzx_click_jygl()
        LoginPage(self.driver).qiehuannew()
        Sjzx(self.driver).sjzx_click_querenfahuo()
        self.assertEqual(Sjzx(self.driver).sjzx_fahuotanchuang(),'待收货')

    def test_darenshouhuo(self):
        Darenzx(self.driver).drzx_clickjiyangguanli()
        self.assertEqual(Darenzx(self.driver).drzx_querenshouhuo(),'已完成')
    #商家确认订单状态
    def test_shangjia_dingdanzhaugntai(self):
        LoginPage(self.driver).shangjialogin('xxx','xxx')
        LoginPage(self.driver).sjzx_click_jygl()
        LoginPage(self.driver).qiehuannew()
        LoginPage(self.driver).swipe_youohua()
        self.assertEqual(Sjzx(self.driver).sjzx_dingdanzhuangtai(),'已完成')



    def tearDown(self):
        self.logger.info('------测试用例执行完毕------')
        self.driver.quit()
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Testcase("test_login"))
    testunit.addTest(Testcase("test_login_namenull"))
    testunit.addTest(Testcase("test_login_pwderror"))
    testunit.addTest(Testcase("test_login_nameerror"))
    testunit.addTest(Testcase("test_login_pwderror"))
    testunit.addTest(Testcase("test_login_swipetips"))
    testunit.addTest(Testcase("test_jiyang_xianshangzhifu"))
    testunit.addTest(Testcase("test_jiyang_xianxiazhifu"))
    testunit.addTest(Testcase("test_houtai_querenfukuan"))
    testunit.addTest(Testcase("test_shangjia_querenshouhuo"))
    testunit.addTest(Testcase("test_darenshouhuo"))
    testunit.addTest(Testcase("test_shangjia_dingdanzhaugntai"))
    test_report = r'D:\test\xiangbobo\resuit\resuit'
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    fp = open(test_report + now + '.html','wb')
    runner = HTMLTestRunner(stream=fp, title='香88测试报告', description='用例执行情况：')
    runner.run(testunit)  # 运行测试用例
    fp.close()  # 关闭报告文件
    Email(BasePage).sendemail()