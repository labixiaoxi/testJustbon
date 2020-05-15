# -*-coding:utf-8 -*-
#__author__ = '廖磊'
# Time:2019/5/28 17:18



from selenium.webdriver.common.by import By
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
from config import getLoginElement as element
log = PublicLogs()

#登录
class JbLoginPage(BasePage):
    def input_username(self):
        self.send_keys("id=>abcd","13683450124")

    def input_password(self):
        self.send_keys()

    def click_login(self):
        self.click()





