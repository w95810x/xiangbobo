from time import sleep
from pages.zhaosp import ZSP
from pages.basepage import BasePage
from pages.weblogin import LoginPage
from pages.xuanpinku import Xpk
from pages.yunying import Yunyinght
from common.send_email import Email
import unittest,time,re,os
from PIL import Image, ImageEnhance
from selenium import webdriver
from common.logger import Log
from HTMLTestRunner import HTMLTestRunner



class Testcase(unittest.TestCase):
    logger = Log(logger='TestLogin').get_log()

    def setUp(self):
        self.logger.info('------开始执行测试用例------')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        LoginPage(self.driver).darenlogin("xxx",'xxx')
    def test_jiyang(self):
        LoginPage(self.driver).darenlogin("xxx",'xxx')
        LoginPage(self.driver).zhaosp_click()
        ZSP(self.driver).zsp_sssp('菊花')
        ZSP(self.driver).zsp_click_jysq()
        ZSP(self.driver).zsp_tjjysq()
        ZSP(self.driver).zsp_input_fkxx()



    def tearDown(self):
        pass
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Testcase("test_login"))
    testunit.addTest(Testcase("test_jiyang"))
    test_report = 'E:\\xiang88\\resuit\\resuit'
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    fp = open(test_report + now + '.html','wb')
    runner = HTMLTestRunner(stream=fp, title='香88测试报告', description='用例执行情况：')
    runner.run(testunit)  # 运行测试用例
    fp.close()  # 关闭报告文件
    Email(BasePage).sendemail()

