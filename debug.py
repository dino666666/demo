
import sys
print(sys.path)
sys.path.append("/home/zhanghan/.local/lib/python3.10/site-packages")
print(sys.path)

import pytest


if __name__ == "__main__":
     pytest.main(['-s', '-v', 'pipeline-hello-world/test_demo.py', '-q', '--alluredir', './allure-results'])
     # import os

     # _out = os.popen("allure generate allure-results -o allure_reports/ --clean").read()
     # print(_out)
