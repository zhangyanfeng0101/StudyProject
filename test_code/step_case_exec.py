#-*- coding: utf-8 -*-
__author__ = 'tsbc'
import sys
import unittest
import sys, time, os
from test_code import caseLogin126mail_PO
from test_code import caseCreateContacts
from test_code import case_Login126mail
from test_code import caseSearchBaidu
from test_code import caseSearchBaiduAction

sys.path.append("test_code")
from test_code.public import HTMLTestRunner_cn

#定义单元测试容器
testunit = unittest.TestSuite()


#将测试用例加入测试容器中
#testunit.addTest(unittest.makeSuite(caseLogin126mail_PO.Caselogin126mail))
#testunit.addTest(unittest.makeSuite(caseCreateContacts.CaseContact126mail))
testunit.addTest(unittest.makeSuite(case_Login126mail.Login126Mail))
#testunit.addTest(unittest.makeSuite(caseSearchBaidu.Baidu))
#testunit.addTest(unittest.makeSuite(caseSearchBaiduAction.CaseSearchbaidu))

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径。。。
result = "..\\result\\"

tdresult = result + day
if os.path.exists(tdresult):
	filename = tdresult + "\\" + now + "_result.html"
	fp = open(filename, 'wb')
	#定义测试报告
	runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

	#运行测试用例
	runner.run(testunit)
	fp.close()  #关闭报告文件
else:
	os.mkdir(tdresult)
	#os.mkdir(tdresult+"\\image")
	filename = tdresult + "\\" + now + "_result.html"
	fp = open(filename, 'wb')
	#定义测试报告
	runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')

	#运行测试用例
	runner.run(testunit)
	fp.close()  #关闭报告文件