# import os
# import sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.loggers import Log


class TESTelement(object):
    def __init__(self, driver):
        self.driver = driver
        self.mylog = Log()

    def elements(self, type, position, *args):
        '''
        元素定位方法
        :param type: 元素类型
        :param position: 定位位置
        :param args: 多个相同位置时 指向具体位置参数
        :return:
        '''
        try:
            if 'xpath' in type.lower():
                return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, position)))

            elif type.lower().startswith('id'):
                return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, position)))

            elif type.lower().startswith('class'):
                return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, position)))

            elif type.lower().startswith('name'):
                return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, position)))

            elif type.lower().startswith('elements_id'):
                return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.ID, position)))[
                    args[0]]

            elif type.lower().startswith('elements_class_name'):
                return \
                WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, position)))[
                    args[0]]

            elif type.lower().startswith('elements_name'):
                return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.NAME, position)))[
                    args[0]]

        except EOFError as e:
            return e

    def eventclick(self, type, position, *args):
        '''
        点击事件
        :param type:
        :param position:
        :param args:
        :return:
        '''
        self.mylog.info('登录点击：{},{}'.format(type, position))
        try:
            if self.elements(type, position, *args):
                return self.elements(type, position, *args).click()
        except Exception as e:
            return e

    def eventsend_keys(self, type, position, value, *args):
        '''
        输入框输入值
        :param type:
        :param position:
        :param args:
        :param value: 输入值字段
        :return:
        '''
        self.mylog.info('登录输入：{},{},{}'.format(type, position, value))
        try:
            if self.elements(type, position, *args):
                return self.elements(type, position, *args).send_keys(value)
        except EOFError as e:
            return e

    def swipe(self, type, position, *args):
        '''
        页面滑动
        :param type:
        :param position:
        :param value:
        :param args:
        :return:
        '''
        self.mylog.info('页面滑动：{},{}'.format(type, position))
        try:
            el = self.elements(type, position, *args)
            if el:
                return self.driver.execute_script("arguments[0].scrollIntoView();", el)
        except EOFError as e:
            return e
