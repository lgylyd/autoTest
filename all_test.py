# coding=utf-8
#import sys
#sys.path.append("G:\\python\\new_haitun\\")
import unittest,HTMLTestRunner,time,os
import all_case_list
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_path = BASE_DIR + "\\test_result\\"

# 创建测试套件

test_unit = unittest.TestSuite()

# 读取需要测试的用例名

all_case_names = all_case_list.caseList()

# 循环读取用例加入到测试容器中

for test in all_case_names:
    test_unit.addTest(unittest.makeSuite(test))

# 获取当前时间

now_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

# 定义测试报告保存位置

result_report_path = dir_path  + now_time + ".html"

# 打开文件

fp = file(result_report_path, "wb")

# 把测试内容写入html文件中

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u"测试报告",
    description=u"用例执行情况：")

# 执行用例

runner.run(test_unit)
# 关闭文件
fp.close()
