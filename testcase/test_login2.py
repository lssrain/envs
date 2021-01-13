import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

import pytest
import time
import allure
from publicmethod.elements import *
from common.loginelements import *
from common.configLogin import *
from publicmethod.assertion import *

userinfo=LoglinData()

@allure.epic('超市供应链')
@allure.feature('登录模块')
class Testscmapp:

    @allure.title("登录测试用例")
    @allure.story('登录测试用003')
    def test_login01(self,browser):
        run=TESTelement(browser)
        run.eventclick(xpath()[0],xpath()[1])
        time.sleep(3)
        run.eventsend_keys(class_name_phone()[0],class_name_phone()[1],userinfo.phone(),0)
        run.eventsend_keys(class_name_code()[0],class_name_code()[1],userinfo.code(),1)
        run.eventclick(class_name_confirm()[0],class_name_confirm()[1])

        time.sleep(2)
        Method(browser).swipe()
        time.sleep(3)

    @allure.title("登录测试用例")
    @allure.story('登录测试用004')
    def test_login02(self, browser):
        run = TESTelement(browser)
        run.eventclick(xpath()[0], xpath()[1])
        time.sleep(3)
        run.eventsend_keys(class_name_phone()[0], class_name_phone()[1], userinfo.phone(), 0)
        run.eventsend_keys(class_name_code()[0], class_name_code()[1], userinfo.code(), 1)
        run.eventclick(class_name_confirm()[0], class_name_confirm()[1])

        time.sleep(2)
        Method(browser).swipe()
        time.sleep(3)

        assert 1==2

if __name__=='__main__':
    pytest.main(['-s', '-q', '--alluredir', './result/allure_xml'])
    os.system(r"allure generate --clean ./result/allure_xml -o ./result/report")







