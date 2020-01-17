import sys
import unittest
from test_code.public import HTMLTestRunner_cn  # 导入包方式
# import HTMLTestRunner_cn    #用import导入需把HTMLTestRunner_cn文件放到python目录lib下
from test_code.public.send_mail import *
import time
import os

# casepath = "."
casepath = "D:\\Web_Project\\test_code\\test_case\\"
result = "D:\\Web_Project\\result\\"


# result = "../result/"


def Creatsuite():
    # 定义单元测试容器
    testunit = unittest.TestSuite()

    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover( casepath, pattern='Case_Login_PO.py', top_level_dir=None )

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest( casename )
    # print (testunit)
    return testunit


test_case = Creatsuite()

# 获取系统当前时间
now = time.strftime( '%Y-%m-%d-%H_%M_%S', time.localtime( time.time() ) )
day = time.strftime( '%Y-%m-%d', time.localtime( time.time() ) )

# 定义报告存放路径，支持相对路径
tdresult = result + day
if os.path.exists( tdresult ):
    filename = tdresult + "/" + now + "_result.html"
    fp = open( filename, 'wb' )
    # 定义测试报告   加入retry=1参数，表示用例失败重跑次数
    runner = HTMLTestRunner_cn.HTMLTestRunner( stream=fp, retry=1, save_last_try=False, verbosity=2, title='自动化测试报告',
                                               description='用例执行情况：' )

    # 运行测试用例
    runner.run( test_case )
    fp.close()  # 关闭报告文件
else:
    os.mkdir( tdresult )
    filename = tdresult + "/" + now + "_result.html"
    fp = open( filename, 'wb' )
    # 定义测试报告     加入retry=1参数，表示用例失败重跑次数
    runner = HTMLTestRunner_cn.HTMLTestRunner( stream=fp, retry=1, save_last_try=False, verbosity=2, title='自动化测试报告',
                                               description='用例执行情况：' )

    # 运行测试用例
    runner.run( test_case )
    fp.close()  # 关闭报告文件

# 发送邮件
# send_mail()

if __name__ == "__main__":
    unittest.main()
