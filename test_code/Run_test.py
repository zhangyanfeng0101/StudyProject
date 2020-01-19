#-*- coding: utf-8 -*-
__author__ = 'tsbc'
import unittest
import sys,time, os
sys.path.append("D:\\Web_Project")
from test_code.public import HTMLTestRunner_cn
from test_code.public.send_mail import send_mail
from test_code.test_case import case_Login126mail
from test_code.test_case import Case_Login_PO
from test_code.test_case import caseCreateContacts
from test_code.test_case import caseSearchBaidu
from test_code.test_case import caseSearchBaiduAction
result = "..\\result\\"


#定义单元测试容器
testunit = unittest.TestSuite()
#将测试用例加入测试容器中
# testunit.addTest(unittest.makeSuite(case_Login126mail.Login126Mail))
testunit.addTest(unittest.makeSuite(Case_Login_PO.Case_Login))
# testunit.addTest(unittest.makeSuite(caseCreateContacts.CaseContact126mail))
# testunit.addTest(unittest.makeSuite(caseSearchBaidu.Demo))
# testunit.addTest(unittest.makeSuite(caseSearchBaiduAction.CaseSearchbaidu))

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
    runner.run( testunit )
    fp.close()  # 关闭报告文件
else:
    os.mkdir( tdresult )
    filename = tdresult + "/" + now + "_result.html"
    fp = open( filename, 'wb' )
    # 定义测试报告     加入retry=1参数，表示用例失败重跑次数
    runner = HTMLTestRunner_cn.HTMLTestRunner( stream=fp, retry=1, save_last_try=False, verbosity=2, title='自动化测试报告',
                                               description='用例执行情况：' )

    # 运行测试用例
    runner.run( testunit )
    # 关闭报告文件
    fp.close()


#发送邮件
send_mail()

