import sys
import os

import allure
import pytest
sys.path.append(os.getcwd())
class TestAllure:
    #修饰步骤
    @allure.step("新增方法被执行")
    @allure.severity("blocker")
    def test01(self):
        #修饰描述
        allure.attach("步骤一","")
        allure.attach("步骤二", "")
        allure.attach("步骤三", "")
        allure.attach("步骤四", "")
        allure.attach("步骤五", "")

        print("test01被执行")
    @allure.step("新增地址被执行")
    @allure.severity("critical")
    def test02(self):
        print("test02被执行")
    @allure.step("新增用户被执行")
    @allure.severity("normal")
    def test03(self):
        print("test03被执行")

    #失败截图并写入报告
    @allure.severity("minor")
    def test04(self):
        print("断言失败，截图并写入报告")
        with open("./image/faile.png","rb")as f:
            allure.attach("失败原因：",f.read(),allure.attach_type.PNG)

    @allure.severity("trivial")
    def test05(self):
        print("test05被执行")