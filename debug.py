
import sys
print(sys.path)
import pytest


if __name__ == "__main__":
     pytest.main(['-s', '-v', 'jenkins_study/test_demo.py', '-q', '--alluredir', './allure-results'])
     # import os

     # _out = os.popen("allure generate allure-results -o allure_reports/ --clean").read()
     # print(_out)
