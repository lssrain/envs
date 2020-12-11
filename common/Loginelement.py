import os
import configparser

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
configPath=os.path.join(rootPath+'\\'+'config','longinelement.ini')
# print(configDir)
# print(configPath)

class Loglinelem:
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(configPath)

        self.Button_Login=self.cf['element']['button_Login']
        self.Input_phone=self.cf['element']['input_phone']
        self.Input_code=self.cf['element']['input_code']
        self.Button_confirm=self.cf['element']#['button_confirm']


    def button_Login(self):
        return self.Button_Login

    def input_phone(self):
        return self.Input_phone

    def input_code(self):
        return self.Input_code

    def button_confirm(self):
        return self.Button_confirm

if __name__=='__main__':
    s=Loglinelem()
    print(s.button_confirm())
    # pass


