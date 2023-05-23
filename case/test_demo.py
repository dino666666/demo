from lib.share.adb import Adb
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

class TestDemo:

    def test_a(self):
        a = Adb()
        a.connect()
        a.disconnect()

    def test_b(self):
        print("用例2执行了")
