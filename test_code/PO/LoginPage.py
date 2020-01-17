#-*- coding: utf-8 -*-

from test_code.PO.BasePage import *
from selenium.webdriver.common.by import By
import xlrd
import sys, os
#继承BasePage类
class LoginPage(Action):
    """
    LoginPage 对象库组件
    """
    login_iframe_loc = (By.XPATH, "//*[@id='loginDiv']/iframe")
    #切换登录模式为动态密码登录（IE下有效）
    dynpw_loc = (By.ID, "lbDynPw")
    #使用密码方式登录
    password_login_loc = (By.ID, "switchAccountLogin")
    #读取测试数据的路径
    fpath = "D:\\StudyProject\\data\\case_data.xls"

    #登录页面元素读取两种方式：1、直接赋值 2、读取excel表里的元素
    #1、定位器，通过元素属性定位元素对象
    username_loc = (By.NAME, "email")
    password_loc = (By.NAME, "password")
    submit_loc = (By.ID, "dologin")
    span_loc = (By.CLASS_NAME, "ferrorhead")
    userid_loc = (By.ID, "spnUid")

    # 2、通过读取excel表里元素属性定位元素对象
    # loc = Action
    # username_loc = loc.locate("ele_0001")
    # password_loc = loc.locate("ele_0002")
    # submit_loc = loc.locate("ele_0003")
    # span_loc = loc.locate("ele_0004")
    # userid_loc = loc.locate("ele_0005")


    # 把每一个元素进行封装成一个方法
    def login_iframe(self):
        self.switch_frame( *self.login_iframe_loc )

    #密码方式登录按钮
    def password_login(self):
        self.find_element(*self.password_login_loc).click()

    def open(self):
        #调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    #调用send_keys，输入用户名
    def input_username(self, username):
        #print self.username_loc
        self.send_keys(self.username_loc, username)
    #调用send_keys，输入密码
    def input_password(self, password):
        self.send_keys(self.password_loc, password)

    # 登录按钮
    def login_button(self):
        self.find_element( *self.submit_loc )

    #调用click，点击登录
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    #用户名或密码不合理Tip框内容展示
    def show_span(self):
         return self.find_element(*self.span_loc).text

    #切换登录模式为动态密码登录（IE下有效）
    def swich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()

    #登录成功页面中的用户ID查找
    def show_userid(self):
        return self.find_element(*self.userid_loc).text

    #获取Excel中Sheet表格对象
    @staticmethod
    def casedata(filepath, sheetno):
        return LoginPage.readxls(filepath, sheetno)