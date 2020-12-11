import os
import configparser

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
configPath=os.path.join(rootPath+'\\'+'config','config.ini')
# print(rootPath)
# print(configPath)

class LoglinData:
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(configPath)

        self.Phone=self.cf['basedata']['phone']
        self.Code=self.cf['basedata']['code']
        self.Url=self.cf['baseurl']['url']

    def phone(self):
        return self.Phone

    def code(self):
        return self.Code

    def url(self):
        return self.Url

if __name__=='__main__':
    # s=LoglinData()
    # print(s.phone())
    pass


