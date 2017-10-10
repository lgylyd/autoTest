# coding=utf-8
import login,B2bOrders
from selenium import webdriver
import unittest
import ConfigParser
import os,time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir_path = BASE_DIR + "\\case_config"
data_login = ConfigParser.SafeConfigParser()
data_login.read(dir_path+"\\login_case.conf")
data_B2bOrders = ConfigParser.SafeConfigParser()
data_B2bOrders.read(dir_path+"\\B2bOrders_case.conf")
#登录参数位置
usr_1 = data_login.get("case","case_0")
usr_name_1 = eval(usr_1)["usr_name"]
usr_pwd_1 = eval(usr_1)["usr_pwd"]
result_1 = eval(usr_1)["result"]
#测试用例
parameter_0 = {}
parameter_1 = {}
parameter_2 = {}
parameter_3 = {}
parameter_4 = {}
parameter_5 = {}
parameter_6 = {}
parameter_7 = {}
parameter_8 = {}
parameter_9 = {}
parameter_10 = {}
parameter_11 = {}
for i in range(12):
    parameter_0.update(eval(data_B2bOrders.get("case_0","data_%d"%i)))
    parameter_1.update(eval(data_B2bOrders.get("case_1","data_%d"%i)))
    parameter_2.update(eval(data_B2bOrders.get("case_2","data_%d"%i)))
    parameter_3.update(eval(data_B2bOrders.get("case_3","data_%d"%i)))
    parameter_4.update(eval(data_B2bOrders.get("case_4","data_%d"%i)))
    parameter_5.update(eval(data_B2bOrders.get("case_5","data_%d"%i)))
    parameter_6.update(eval(data_B2bOrders.get("case_6","data_%d"%i)))
    parameter_7.update(eval(data_B2bOrders.get("case_7","data_%d"%i)))
    parameter_8.update(eval(data_B2bOrders.get("case_8","data_%d"%i)))
    parameter_9.update(eval(data_B2bOrders.get("case_9","data_%d"%i)))
    parameter_10.update(eval(data_B2bOrders.get("case_10","data_%d"%i)))
    parameter_11.update(eval(data_B2bOrders.get("case_11", "data_%d"%i)))

class B2bOrdersTest(unittest.TestCase):

    u"""创建bb销售订单测试"""

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        login.login(self.driver, usr_name_1, usr_pwd_1)
    def test_B2bOrders(self):
        u"""输入符合要求的bb订单数据"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_0)
        result = driver.current_url
        self.assertEqual(result, parameter_0["result_0"])

    def test_B2bOrders_noorders(self):
        u"""不输入平台订单号，创建bb单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_1)
        result = driver.current_url
        self.assertEqual(result, parameter_1["result_0"])
    def test_B2bOrders_noconsignee(self):
        u"""必填字段收货人姓名不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_2)
        result = driver.current_url
        self.assertEqual(result, parameter_2["result_0"])
    def test_B2bOrders_notelphone(self):
        u"""必填字段手机号码不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_3)
        result = driver.current_url
        self.assertEqual(result, parameter_3["result_0"])
    def test_B2bOrders_noprovince(self):
        u"""必填字段收货省份不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_4)
        result = driver.current_url
        self.assertEqual(result, parameter_4["result_0"])
    def test_B2bOrders_nocity(self):
        u"""必填字段收货人城市不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_5)
        result = driver.current_url
        self.assertEqual(result, parameter_5["result_0"])
    def test_B2bOrders_nodistrict(self):
        u"""必填字段收货人地区不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_6)
        result = driver.current_url
        self.assertEqual(result, parameter_6["result_0"])
    def test_B2bOrders_noaddress(self):
        u"""必填字段收货人详细地区不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_7)
        result = driver.current_url
        self.assertEqual(result, parameter_7["result_0"])
    def test_B2bOrders_noidentification(self):
        u"""必填字段收货人身份证信息不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_8)
        result = driver.current_url
        self.assertEqual(result, parameter_8["result_0"])
    def test_B2bOrders_nosku(self):
        u"""必填字段商品信息不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_9)
        result = driver.current_url
        self.assertEqual(result, parameter_9["result_0"])
    def test_B2bOrders_noprice(self):
        u"""必填字段商品价格不填写，创建订单失败"""
        driver=self.driver
        B2bOrders.BbSellOrder(driver,**parameter_10)
        result = driver.current_url
        self.assertEqual(result, parameter_10["result_0"])
    def test_B2bOrders_reorders(self):
        u"""填入重复的平台订单号，创建订单失败"""
        driver=self.driver
        parameter_11["orders"]="test%s"%time.strftime("%Y-%m-%d_%H:%M:%S")
        B2bOrders.BbSellOrder(driver,**parameter_11)
        result = driver.current_url
        self.assertEqual(result, parameter_0["result_0"])
        B2bOrders.BbSellOrder(driver, **parameter_11)
        result = driver.current_url
        self.assertEqual(result, parameter_11["result_0"])

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.makeSuite(B2bOrdersTest)
