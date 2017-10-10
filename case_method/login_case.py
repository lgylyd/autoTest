# coding=utf-8
#import sys
#sys.path.append(r'G:\python\new_haitun\page_opration')
import login
from selenium import webdriver
import unittest
import ConfigParser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR + "\\case_config\\login_case.conf"
data = ConfigParser.SafeConfigParser()
data.read(dir_path)
usr_1 = data.get("case","case_0")
usr_name_1 = eval(usr_1)["usr_name"]
usr_pwd_1 = eval(usr_1)["usr_pwd"]
result_1 = eval(usr_1)["result"]

usr_2 = data.get("case","case_1")
usr_name_2 = eval(usr_2)["usr_name"]
usr_pwd_2 = eval(usr_2)["usr_pwd"]
result_2 = eval(usr_2)["result"]

usr_3 = data.get("case","case_2")
usr_name_3 = eval(usr_3)["usr_name"]
usr_pwd_3 = eval(usr_3)["usr_pwd"]
result_3 = eval(usr_3)["result"]

class LoginTest(unittest.TestCase):

    u"""登录测试"""

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()

    def test_login(self):
        u"""输入正确的账号和密码"""
        driver=self.driver
        login.login(driver,usr_name_1,usr_pwd_1)
        result = driver.current_url
        self.assertEqual(result, result_1)

    def test_login_nopw(self):
        u"""输入正确的账号，密码为空"""
        driver = self.driver
        login.login(driver,usr_name_2,usr_pwd_2)
        result = driver.current_url
        self.assertEqual(result, result_2)

    def test_login_nouser(self):
        u"""输入正确的密码，账号为空"""
        driver = self.driver
        login.login(driver,usr_name_3,usr_pwd_3)
        result = driver.current_url
        self.assertEqual(result, result_3)

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()

