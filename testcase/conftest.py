import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest
import time
import allure
from selenium import webdriver
from common.chromedriver import *
from common.configLogin import *

driver = None
chromedriver=chromedriver()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''

    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

# def get_picture():
#     file_name='{}.png'.format(time.strftime('%Y_%m_%d_%H_%M_%S'))
#     return driver.get_screenshot_as_flie(file_name)

@pytest.fixture(scope='function', autouse=True)
def browser():
    '''
    类中每个方法都会调用这个函数方法
    :return:
    '''
    global driver
    driver=webdriver.Chrome(chromedriver)
    driver.maximize_window()
    driver.get('http://dev.wechat.tianhong.cn/scm-app/')
    time.sleep(2)
    yield driver
    driver.quit()
    return driver


# @pytest.fixture(scope='class', autouse=True)
# def drivers():
#     '''
#     类中只调用这个函数方法1次
#     :return:
#     '''
#     global driver
#     driver=webdriver.Chrome(chromedriver)
#     driver.maximize_window()
#     driver.get('http://dev.wechat.tianhong.cn/scm-app/')
#     yield driver
#     driver.quit()
#     return driver





