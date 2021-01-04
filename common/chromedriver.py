import os

def chromedriver():
    '''
    获取驱动路径
    :return:
    '''
    # driverdir=os.path.split(os.path.realpath(os.getcwd()))[0]
    # driverpath=os.path.join(driverdir,'chromedriver','chromedriver.exe')
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    driverpath = os.path.join(rootPath, 'chromedriver', 'chromedriver.exe')
    # print(driverpath)
    return driverpath

if __name__=='__main__':
    chromedriver()
