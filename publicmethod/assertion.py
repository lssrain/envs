import os
import sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.loggers import Log


class Method:
    def __init__(self,drver):
        self.driver=drver
        self.mylog=Log()

    def swipe(self):
        '''
        1.页面上下滑动
        2.添加断言，判断是否登录成功
        :return:
        '''
        element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'moreGoods')))
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        self.mylog.info('登录成功断言：{}'.format(element.text))
        assert element.text=='+ 推荐更多商品'

        # target = self.driver.find_element_by_class_name('moreGoods')
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        # assert self.driver.find_element_by_class_name('moreGoods').text=='+ 推荐更多商品'

if __name__=='__main__':
    pass
