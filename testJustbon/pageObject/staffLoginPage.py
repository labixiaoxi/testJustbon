# -*-coding:utf-8 -*-
#__author__ = '廖磊'
# Time:2019/5/28 17:18
from selenium.webdriver.common.by import By
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
from config import getLoginElement as element
log = PublicLogs()

#登录
class StaffLoginPage(BasePage):
    def input_username(self,username):
        self.send_keys("id=>com.justbon.oa:id/user_name",username)
        log.info("登录页面---输入账号%s"%username)

    def input_password(self,password):
        self.send_keys("id=>com.justbon.oa:id/user_pwd",password)
        log.info("登录页面---输入密码%s"%password)

    def click_login(self):
        self.click("id=>com.justbon.oa:id/login")
        log.info(u"登录页面---点击登录")









