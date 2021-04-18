import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
# noinspection PyUnresolvedReferences
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.support.wait import WebDriverWait
from common.logger import Log
from selenium.webdriver.common.by import By
import unittest
import pytesseract
from PIL import Image, ImageEnhance

from time import sleep

class BasePage():
    logger = Log(logger='BasePage').get_log()

    def __init__(self,driver):
        self.driver = driver


    def find_element(self, loc):
        return self.driver.find_element(*loc)

    def clear_key(self,loc):
        """重写清空文本框"""
        sleep(3)
        self.find_element(loc).clear()


    def send_keys(self, loc, value):
        """输入内容"""
        self.find_element(loc).send_keys(value)


    def click_button(self,loc):
        """点击按钮"""
        self.find_element(loc).click()

    def open_url(self, url):
        self.driver.get(url)

        # 下拉列表选择
    def select_term(self, loc, index):
        # 实例化Select
        Select(self.find_element(*loc)).select_by_index(int(index))
        # s1.select_by_index(1)  # 选择第二项选项：o1
        # s1.select_by_value("o2")  # 选择value="o2"的项
        # s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本

        # 鼠标悬浮
    def mouse_hover(self, loc):
        move = self.find_element(loc)
        ActionChains(self.driver).move_to_element(move).perform()

            # 获取title

    def get_title(self):
        return self.driver.title

        # 获取文本信息
    def get_txt(self, loc):
        return self.find_element(loc).text

    # 页面滑动到底部
    def swip_di(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    #滑动到页面指定元素位置
    def swip_zhidingwz(self,loc):
        target = self.find_element(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 获取当前页面url
    def get_page_url(self):
        return self.driver.current_url

    # 清除cookies
    def delete_cookies(self):
        self.driver.delete_all_cookies()
    #切换到最新打开的窗口
    def qiehuannew(self):
        handles = self.driver.window_handles
        # 切换到最新打开的窗口
        self.driver.switch_to.window(handles[-1])
    #获取验证码
    def get_yzm(self):
        screenImg = "E:\screenImg.png"
        # 浏览器页面截屏
        self.driver.get_screenshot_as_file(screenImg)
        # 定位验证码位置及大小
        location = self.driver.find_element_by_class_name('codeImage').location
        size = self.driver.find_element_by_class_name('codeImage').size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        # 从文件读取截图，截取验证码位置再次保存
        img = Image.open(screenImg).crop((left, top, right, bottom))
        # 下面对图片做了一些处理，能更好识别一些，相关处理再百度看吧
        img = img.convert('RGBA')  # 转换模式：L | RGB
        img = img.convert('L')  # 转换模式：L | RGB
        img = ImageEnhance.Contrast(img)  # 增强对比度
        img = img.enhance(2.0)  # 增加饱和度
        img.save(screenImg)
        # 再次读取识别验证码
        img = Image.open(screenImg)
        code = pytesseract.image_to_string(img)
        data = pytesseract.image_to_string(img)
        print(data)
        # 打印识别的验证码
        print(code.strip())
        # 识别出来验证码去特殊符号，用到了正则表达式，这是我第一次用，之前也没研究过，所以用的可能粗糙，请见谅
        b = ''
        for i in code.strip():
            pattern = re.compile(r'[a-zA-Z0-9]')
            m = pattern.search(i)
            if m != None:
                b += i
        # 输出去特殊符号以后的验证码
        print(b)






#     def find_element(self, type, position):
#             if type == 'xpath':
#                 element = self.driver.find_element_by_xpath(position)
#                 return element
#             elif type == 'id':
#                 element = self.driver.find_element_by_id(position)
#                 return element
#             elif type == 'name':
#                 element = self.driver.find_element_by_name(position)
#                 return element
#             elif type == 'link_text':
#                 element = self.driver.find_element_by_link_text(position)
#                 return element
#             elif type == 'classname':
#                 element = self.driver.find_element_by_class_name(position)
#                 return element
#             else:
#                 print("不支持的类型")
#
#     def clear_key(self,type,loc):
#         """重写清空文本框"""
#         sleep(3)
#         self.find_element(type,loc).clear()
#
#
#     def send_keys(self,type,loc,v):
#         """输入内容"""
#         self.clear_key(type,loc)
#         self.find_element(type,loc).send_keys(v)
#
#
#     def click_button(self,type,loc):
#         """点击按钮"""
#         self.find_element(type,loc).click()
#
#         # 打开网页
#     def open_url(self, url):
#         self.driver.get(url)
#
#         # 下拉列表选择
#     def select_term(self, loc, index):
#         # 实例化Select
#         Select(self.find_element(*loc)).select_by_index(int(index))
#         # s1.select_by_index(1)  # 选择第二项选项：o1
#         # s1.select_by_value("o2")  # 选择value="o2"的项
#         # s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本
#
#         # 鼠标悬浮
#     def mouse_hover(self,type,loc):
#         move = self.find_element(type,loc)
#         ActionChains(self.driver).move_to_element(move).perform()
#
#         # 获取title
#     def get_title(self):
#         return self.driver.title
#
#         # 获取文本信息
#     def get_txt(self,type,loc):
#         return self.find_element(type,loc).text
#
#     #页面滑动到底部
#     def swip_di(self):
#         js = "var q=document.documentElement.scrollTop=10000"
#         self.driver.execute_script(js)
#
#     # 获取当前页面url
#     def get_page_url(self):
#         return self.driver.current_url
#
#      #清除cookies
#     def delete_cookies(self):
#         self.driver.delete_all_cookies()
#
#
# if __name__ == '__main__':
#     unittest.main()
#
