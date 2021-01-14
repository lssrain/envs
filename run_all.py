import pytest
import os

if __name__ == '__main__':
    # pytest.main(['-q','-v','testcase/','--html=report/report.html', '--self-contained-html'])#运行testcase文件夹下的测试用例
    # pytest.main(['--alluredir', 'report/allure_raw'])
    pytest.main(['-s', '-q', 'testcase/', '--alluredir', './result/allure_xml'])
    os.system(r"allure generate --clean ./result/allure_xml -o ./result/report")
