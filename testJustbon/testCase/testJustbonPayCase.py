# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 16:03
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest, time, HTMLTestRunner, datetime
from public.publicDriver import publicDrivers
from public.publicYaml import PublicGetYaml
from public.publicExcel import PublicExcel
from public.publicOperate import PublicOperate
from public import publicSql
from pageObject.jbLoginPage import *
from pageObject.jbHomePage import JbHomePage
from pageObject.jbHomeHeadersPage import JbHomeHeadersPage
from pageObject.jbHomeFunctionPage import *
from pageObject.jbHomeLivePage import *
from pageObject.jbShopPage import *
from pageObject.jbNeighborPage import *
from ddt import ddt, data, unpack
from public.publicPhone import PublicPhone

@ddt
class TestLoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = publicDrivers()
        cls.home = JbHomePage(cls.driver)
        cls.login = JbLoginPage(cls.driver)
        cls.loginYaml = PublicGetYaml('../config/login.yaml').get_Yaml()['loginCase']
        cls.operate = PublicOperate(cls.driver)
        cls.homeHeaders = JbHomeHeadersPage(cls.driver)
        cls.homeNotice = JbHomeNoticePage(cls.driver)
        cls.homeHousekeeper = JbHomeHousekeeperPage(cls.driver)
        cls.homePay = JbhomePayPage(cls.driver)
        cls.homeGuarantee = JbhomeGuaranteePage(cls.driver)
        cls.homeComplaint = JbHomeComplaintPage(cls.driver)
        cls.homeVisitor = JbHomeVisitorPage(cls.driver)
        cls.homeCheckIn = JbHomeCheckInPage(cls.driver)
        cls.homeHouse = JbHomeHousePage(cls.driver)
        cls.homeParcel = JbHomeParcelPage(cls.driver)
        cls.homePeriphery = JbHomePeripheryPage(cls.driver)
        cls.shop = JbShopPage(cls.driver)
        cls.homeWater = JbHomeWaterPage(cls.driver)
        cls.jiaDou = JbJiaDouPage(cls.driver)
        cls.coupon = JbCouponPage(cls.driver)
        cls.contentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cls.selected = JbHomeSelectedPage(cls.driver)
        cls.openDoor = JbhomeOpenDoorPage(cls.driver)
        cls.homeParcel = JbHomeParcelPage(cls.driver)
        cls.setting = JbSettingPage(cls.driver)
        cls.orders = JbOrdersPage(cls.driver)
        cls.delicous = JbHomeDeliciousPage(cls.driver)
        cls.neighbor = JbNeighborPage(cls.driver)
        PublicPhone().write_excel()
    def setUp(self):
        pass


    def test_c_me_login_002(self):
        """登录---登录成功"""


    def test_g_home_pay_001(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单取消"""
        self.homePay.jbHomePay_click_pay()
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_cancel()
        self.homePay.jbHomePay_click_paymentSlip_cancel_determine()
        self.operate.get_back()

    def test_g_home_pay_002(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择微信,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_pay()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_003(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择支付宝,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_pay()
        self.homePay.jbHomePay_click_zfb()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()


    def test_g_home_pay_004(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择银行卡,点击确认支付---返回---点击取消"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.homePay.jbHomePay_click_go()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_cancel_order()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()

    def test_g_home_pay_005(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择招行一网通,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_pay()
        self.homePay.jbHomePay_click_zh()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_006(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择微信,点击确认支付---返回到物业缴费页面---缴费单取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_pay()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        for i in range(2):
            self.operate.get_back()
        self.homePay.jbHomePay_click_paymentSlip()
        self.homePay.jbHomePay_click_paymentSlip_cancel()
        self.homePay.jbHomePay_click_paymentSlip_cancel_determine()
        self.operate.get_back()


    def test_g_home_pay_007(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择支付宝,点击确认支付---返回到物业缴费页面---缴费单取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_pay()
        self.homePay.jbHomePay_click_zfb()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        for i in range(2):
            self.operate.get_back()
        self.homePay.jbHomePay_click_paymentSlip()
        self.homePay.jbHomePay_click_paymentSlip_cancel()
        self.homePay.jbHomePay_click_paymentSlip_cancel_determine()
        self.operate.get_back()

    def test_g_home_pay_008(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择银行卡,点击确认支付---返回到物业缴费页面---缴费单取消"""

        # self.homePay.jbHomePay_click_immediately_pay()
        # self.operate.get_back()
        # self.homePay.jbHomePay_click_immediately_pay()
        # self.homePay.jbHomePay_click_go()
        # self.homePay.jbHomePay_click_paymentSlip_pay()
        # self.homePay.jbHomePay_click_confirmation_of_payment()
        # self.operate.get_back()
        # self.homePay.jbHomePay_click_cancel_order()
        # self.homePay.jbHomePay_click_cancel_order_determine()
        # for i in range(2):
        #     self.operate.get_back()
        # self.homePay.jbHomePay_click_paymentSlip()
        # self.homePay.jbHomePay_click_paymentSlip_cancel()
        # self.homePay.jbHomePay_click_paymentSlip_cancel_determine()
        # self.operate.get_back()

    def test_g_home_pay_009(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单点击支付---选择招行一网通,点击确认支付---返回到物业缴费页面---缴费单取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_pay()
        self.homePay.jbHomePay_click_zh()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        for i in range(2):
            self.operate.get_back()
        self.homePay.jbHomePay_click_paymentSlip()
        self.homePay.jbHomePay_click_paymentSlip_cancel()
        self.homePay.jbHomePay_click_paymentSlip_cancel_determine()
        self.operate.get_back()

    def test_g_home_pay_010(self):
        """缴费---点击立即缴费---选择微信,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_011(self):
        """缴费---点击立即缴费---选择支付宝,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_zfb()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_012(self):
        """缴费---点击立即缴费---选择银行卡,点击确认支付---返回---点击取消"""
        # self.homePay.jbHomePay_click_immediately_pay()
        # self.homePay.jbHomePay_click_confirmation_of_payment()
        # self.operate.get_back()
        # self.homePay.jbHomePay_click_cancel_order()
        # self.homePay.jbHomePay_click_cancel_order_determine()
        # self.operate.get_back()

    def test_g_home_pay_013(self):
        """缴费---点击立即缴费---选择招行一网通,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.click_zh_loc()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_014(self):
        """缴费---点击立即缴费---选择微信,点击确认支付---返回---继续支付---选择支付宝,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_pay_order()
        self.homePay.jbHomePay_click_zfb()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_015(self):
        """缴费---选择某月缴费---点击确认缴费---选择微信,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_first_bill()
        self.homePay.jbHomePay_click_confirmation_payment()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_016(self):
        """缴费---选择某月缴费---点击确认缴费---返回---缴费单点击支付---选择微信,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_first_bill()
        self.homePay.jbHomePay_click_confirmation_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_paymentSlip()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_017(self):
        """缴费---预存物业费---选择预存金额---立即支付---选择微信,点击确认支付---返回---点击取消"""
        self.homePay.jbHomePay_click_pre_storage()
        self.homePay.jbHomePay_click_pre_storage_determine()
        self.homePay.jbHomePay_input_pre_storage_money()
        self.homePay.jbHomePay_click_immediate_payment()
        self.homePay.jbHomePay_click_confirmation_of_payment()
        self.operate.get_back()
        self.homePay.jbHomePay_click_cancel_order()
        self.homePay.jbHomePay_click_cancel_order_determine()
        self.operate.get_back()

    def test_g_home_pay_018(self):
        """缴费---查看历史账单"""
        self.homePay.jbHomePay_click_historyPay()
        self.operate.get_back()
































































