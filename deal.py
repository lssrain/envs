import os
import sys
# reportpath=os.path.split(os.path.realpath(os.getcwd()))[0]
# reportdir=os.path.join(reportpath+'\\'+'report','report.html')
# print(reportdir)

# reportpath=os.path.split(os.path.realpath(os.getcwd()))[0]
# sys.path.append(reportpath)
# print(reportpath)

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

print(curPath)

#
# import sys
# import os
# base_path = os.getcwd()
# sys.path.append(base_path)
# print(base_path)



