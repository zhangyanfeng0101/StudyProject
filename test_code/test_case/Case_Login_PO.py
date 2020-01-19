# -*- coding: utf-8 -*-
import unittest
import time,configparser
from test_code.PO import LoginPage
from selenium import webdriver

#关于所有地方读取文件路径，若使用相对路径，本模块直接运行调试需改成..\\..\\data，在Run_all_tests文件运行需改成..\\data，原因暂时未找到

class Case_Login( unittest.TestCase ):
    """
	126邮箱登录的case
	"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait( 5 )
        # 使用ini配置文件读取要访问的url
        cf = configparser.ConfigParser()
        cf.read( "..\\data\\login_126mail_data.ini" )

        cls.url = cf.get( "urlconf", "url" )

    # 测试用例执行体
    def action(self, case_id, case_summary, username, password):
        login_page = LoginPage.LoginPage( self.driver, self.url, u"网易" )
        login_page.open()
        print( "========【" + case_id + u"】" + case_summary + "=============" )
        print( username )
        print( password )
        # 调用PO组件
        login_page.password_login()
        login_page.login_iframe()
        login_page.input_username( username )
        login_page.input_password( password )
        login_page.click_submit()

        time.sleep( 1 )
        try:
            login_page.show_span()
            print("登录失败，提示语为:",login_page.show_span() )
            login_page.saveScreenshot( self.driver, "Fail" )
        except:
            print( "登录成功，当前网页标题为:", self.driver.title )
            try:
                self.assertTrue( login_page.show_userid() )
                login_page.saveScreenshot( self.driver, "Success" )
            except:
                #触发异常，如果登录成功，但是未成功找到用户名，也判断该用例为失败
                 raise login_page.saveScreenshot( self.driver, "Fail" )

    @staticmethod
    def getTestFunc(case_id, case_summary, username, password):
        def func(self):
            self.action( case_id, case_summary, username, password )

        return func

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()


def __generateTestCases():
    login_page = LoginPage.LoginPage
    table = login_page.casedata( "..\\data\\case_data.xls", 1 )
    for txt in table:
        print( txt )
        setattr( Case_Login, 'test_login_%s_%s' % (txt[0], txt[1]),Case_Login.getTestFunc( *txt ) )


__generateTestCases()

if __name__ == '__main__':
    unittest.main()
