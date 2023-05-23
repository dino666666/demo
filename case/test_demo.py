#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.share.adb import Adb


class TestDemo:

    def test_a(self):
        a = Adb()
        a.connect()
        a.disconnect()

    def test_b(self):
        print("用例2执行了")
