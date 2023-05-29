

import pytest


if __name__ == "__main__":
     pytest.main(['-s', '-v', 'jenkins_study/test_demo.py', '-q', '--alluredir', './report'])
     import os
     _out = os.popen("allure generate report -o allure_reports/ --clean").read()
     print(_out)


