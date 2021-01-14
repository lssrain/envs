import os
import json
import sys

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
jsonPath = os.path.join(rootPath, 'json', 'loginelement.json')
# print(jsonPath)

with open(jsonPath, 'r')as f:
    json_data = dict(json.load(f))

jsonfile = json_data


def xpath():
    return 'xpath_login', jsonfile['xpath_login']


def class_name_phone():
    return 'elements_class_name_phone', jsonfile['elements_class_name_phone']


def class_name_code():
    return 'elements_class_name_code', jsonfile['elements_class_name_code']


def class_name_confirm():
    return 'class_name_confirm', jsonfile['class_name_confirm']


if __name__ == '__main__':
    # print(xpath()[1])
    pass
