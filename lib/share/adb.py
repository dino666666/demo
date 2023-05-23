import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class Adb:
    def __init__(self):
        pass

    def connect(self):
        print("已连接")

    def disconnect(self):
        print("断开连接")
