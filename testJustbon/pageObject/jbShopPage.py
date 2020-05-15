# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/5/31 15:21
import time
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
from config import getLoginElement as element
log = PublicLogs()
class JbShopPage(BasePage):
    """
    商城
    """
    click_stly_loc='xpath=>/html/body/div/div[2]/ul[1]/li[1]/a/img'
    click_jydq_loc="xpath=>/html/body/div/div[2]/ul[1]/li[2]/a/img"
    click_sgsx_loc="xpath=>/html/body/div/div[2]/ul[1]/li[3]/a/img"
    click_jtry_loc="xpath=>/html/body/div/div[2]/ul[1]/li[4]/a/img"
    click_lbsc_loc="xpath=>/html/body/div/div[2]/ul[1]/li[5]/a/img"
    click_bgsm_loc="xpath=>/html/body/div/div[2]/ul[1]/li[6]/a/img"
    click_my_loc="xpath=>/html/body/div/div[2]/ul[1]/li[7]/a/img"
    click_location_loc='xpath=>/html/body/div[1]/ul[2]/ul[1]/li[2]/a'
    click_product_loc='xpath=>/html/body/div[5]/div[1]/div/ul/li[1]/a/div[1]/img'
    click_purchase_loc='xpath=>/html/body/div[2]/a[2]'
    click_submitOrder_loc='xpath=>//*[@id="os_1561454062"]'

    #生态粮油
    def jbShop_click_stly(self):
        self.click(self.click_stly_loc)
        log.info(u"商城页面---点击蔬果生鲜")
        time.sleep(2)

    #家用电器
    def jbShop_click_jydq(self):
        self.click(self.click_jydq_loc)
        log.info(u"商城页面---点击家用电器")
        time.sleep(2)

    #蔬果生鲜
    def jbShop_click_sgsx(self):
        self.click(self.click_sgsx_loc)
        log.info(u"商城页面---点击蔬果生鲜")
        time.sleep(2)

    #家庭日用
    def jbShop_click_jtry(self):
        self.click(self.click_jtry_loc)
        log.info(u"商城页面---点击家庭日用")
        time.sleep(2)

    #拎包商城
    def jbShop_click_lbsc(self):
        self.click(self.click_lbsc_loc)
        log.info(u"商城页面---点击拎包商城")
        time.sleep(2)

    #办公数码
    def jbShop_click_bgsm(self):
        self.click(self.click_bgsm_loc)
        log.info(u"商城页面---点击办公数码")
        time.sleep(2)

    #母婴
    def jbShop_click_my(self):
        self.click(self.click_my_loc)
        log.info(u"商城页面---点击母婴")
        time.sleep(2)

    #选择小区
    def jbShop_click_location(self):
        self.click(self.click_location_loc)
        log.info(u"商城页面---选择所在的小区")
        time.sleep(2)

    #选择第一个产品
    def jbShop_click_product(self):
        self.click(self.click_product_loc)
        log.info(u"生态粮油页面---选择第一个产品")
        time.sleep(2)

    #立即购买
    def jbShop_click_purchase(self):
        self.click(self.click_purchase_loc)
        log.info(u"商品详情页面---点击立即购买")
        time.sleep(2)

    #提交订单
    def jbShop_click_submitOrder(self):
        self.click(self.click_submitOrder_loc)
        log.info(u"订单确认页面---点击提交订单")
        time.sleep(2)




