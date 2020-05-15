# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 15:55
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
from config import getHomeElement as element
log = PublicLogs()

#首页下面的功能切换
class JbHomePage(BasePage):
    """
    主页面
    """

    def home_click_home(self):
        self.click(element.home_loc)
        log.info(u"首页页面---点击首页")

    def home_click_security(self):
        self.click(element.security_loc)
        log.info(u"首页页面---点击安防")

    def home_click_shopping(self):
        self.click(element.shopping_loc)
        log.info(u"首页页面---点击商城")

    def home_click_neighbor(self):
        self.click(element.neighbor_loc)
        log.info(u"首页页面---点击邻里")

    def home_click_me(self):
        self.click(element.me_loc)
        log.info(u"首页页面---点击我的")






