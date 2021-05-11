import csv,re,unittest,pytesseract,sys,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from common.logger import Log
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack
from PIL import Image, ImageEnhance
from time import sleep

class BasePage():
    logger = Log(logger='BasePage').get_log()

    def __init__(self,driver):
        self.driver = driver

    # *loc 代表任意数量的位置参数
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            self.logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            self.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_element(*loc)

    def getValue(self, *loc):
        element = self.find_element(*loc)
        try:
            value = element.text
        except Exception:
            value = element.get_attribute('value')
            self.logger.info('reading the element [%s] value [%s]' % (loc, value))
            return value
        except:
            self.logger.exception('read value failed', exc_info=True)
            raise Exception
        else:
            self.logger.info('reading the element [%s] value [%s]' % (loc, value))
            return value

    #查找一组元素
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            self.logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            self.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_elements(*loc)

    def get_values(self,*loc):
        value_list = []
        try:
            for element in self.find_elements(*loc):
                value = element.text
                value_list.append(value)
        except Exception as e:
            self.logger.exception('read value failed', exc_info=True)
            raise e
        else:
            self.logger.info('reading the element [%s] value [%s]' % (loc, value_list))
            return value_list

    def isElementExist(self, element):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
        except:
            return False
        else:
            return True

    def clear_key(self,*loc):
        """重写清空文本框"""
        sleep(3)
        self.find_element(*loc).clear()


    def send_keys(self,loc,value):
        inputB = self.find_element(*loc)
        try:
            inputB.clear()
            inputB.send_keys(value)
        except Exception as e:
            self.logger.exception('typing value error!', exc_info=True)
            raise e
        else:
            self.logger.info('inputValue:[%s] is receiveing value [%s]' % (loc,value))


    def click_button(self,*loc):
        """点击按钮"""
        self.find_element(*loc).click()

    def open_url(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            self.logger.exception(e, exc_info=True)
            raise ValueError('%s address access error, please check！' % url)

        # 下拉列表选择
    def select_term(self, *loc, index):
        # 实例化Select
        Select(self.find_element(*loc)).select_by_index(int(index))
        # s1.select_by_index(1)  # 选择第二项选项：o1
        # s1.select_by_value("o2")  # 选择value="o2"的项
        # s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本

        # 鼠标悬浮
    def mouse_hover(self,*loc):
        self.logger.info('鼠标悬浮')
        try:
            move = self.find_element(*loc)
            ActionChains(self.driver).move_to_element(move).perform()
        except Exception as e:
            self.logger.info(e)
            self.logger.info('悬浮失败')

    #自左向右滑动
    def swipe_youohua(self):
        js = "var q=document.documentElement.scrollLeft=10000"
        self.driver.execute_script(js)
        sleep(1)

        # 获取title

    def get_title(self):
        return self.driver.title

        # 获取文本信息
    def get_txt(self,*loc):
        return self.find_element(*loc).text

    # 页面滑动到底部
    def swip_di(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    #滑动到页面指定元素位置
    def swip_zhidingwz(self,*loc):
        target = self.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #按照输入参数滑动
    def swip_input(self,index,index1):
        self.driver.execute_script('window.scrollBy(index,index1)')

    # 获取当前页面url
    def get_page_url(self):
        return self.driver.current_url

    # 清除cookies
    def delete_cookies(self):
        self.driver.delete_all_cookies()
    #切换到最新打开的窗口
    def qiehuannew(self):
        sleep(1)
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

    def getCsvData(self,file):
        # 读取CSV文件
        value_rows = []
        with open(file, encoding='UTF-8') as f:
            f_csv = csv.reader(f)
            next(f_csv)
            for r in f_csv:
                value_rows.append(r)
        return value_rows

    #获取当前日期
    def get_time(self):
        return time.strftime("%Y-%m-%d", time.localtime())



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
