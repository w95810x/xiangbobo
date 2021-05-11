from time import sleep
from pages.zhaosp import ZSP
from pages.basepage import BasePage
from pages.weblogin import LoginPage
from pages.xuanpinku import Xpk
from pages.yunying import Yunyinght
import unittest
import time
import re
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver
from common.logger import Log
class Screen(object):
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                now_time = time.strftime('%Y_%m_%d_%H_%M_%S')   # 异常时，截图
                self.driver.get_screenshot_as_file(f'{now_time}.png')
                raise   # 抛出异常，不然会认为测试用例执行通过
        return inner