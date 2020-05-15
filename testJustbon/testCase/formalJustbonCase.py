# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 16:03
import importlib,sys
importlib.reload(sys)
import unittest, time, HTMLTestRunner, datetime
from public.publicDriver import publicDrivers
from public.publicYaml import PublicGetYaml
from public.publicExcel import PublicExcel
from public.publicOperate import PublicOperate
from pageObject.jbLoginPage import *
from pageObject.jbHomePage import JbHomePage
from pageObject.jbHomeHeadersPage import JbHomeHeadersPage
from pageObject.jbHomeFunctionPage import *
from pageObject.jbHomeLivePage import *
from pageObject.jbShopPage import *
from pageObject.jbNeighborPage import *
from ddt import ddt, data, unpack
from public.publicPhone import PublicPhone
import warnings
warnings.simplefilter("ignore", ResourceWarning)

@ddt
class TestLoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
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
        # PublicExcel("../config/locust.xls").write_excel()

    def setUp(self):
        pass


    def test_a_register_001(self):
        """注册---填写已经注册过的账号"""
        # self.home.home_click_me()
        # self.login.login_click_loginImmediately()


    # @data(["19000000001", "123123","123456"],["19000000001", "123123","abcdef"],["19000000001", "123123","12ab"])
    # @unpack
    def test_a_me_register_002(self):
        """注册---密码不符合要求"""
        time.sleep(5)

    def test_a_me_register_003(self):
        """注册---验证码错误"""

    def test_a_me_register_004(self):
        """注册---未勾选协议"""

    def test_b_me_forgetPassword_001(self):
        """忘记密码---验证码错误"""

    def test_b_me_forgetPassword_002(self):
        """忘记密码---填写未注册的账号"""

    def test_b_me_forgetPassword_003(self):
        """忘记密码---密码不符合要求"""

    def test_c_me_login_001(self):
        """登录---密码错误"""

    def test_c_me_login_002(self):
        """登录---登录成功"""
        self.home.home_click_me()
        self.login.login_click_loginImmediately()
        self.login.login_input_username(self.loginYaml['username'])
        self.login.login_input_password(self.loginYaml['password'])
        self.login.login_click_login()
        self.home.home_click_home()

    def test_d_home_top_001(self):
        """首页---顶部项目切换"""
        self.homeHeaders.homeHeaders_click_add()
        self.homeHeaders.homeHeaders_click_replace_add()
        #切换到我的页面，判断项目是否更换成功
        self.home.home_click_me()
        self.home.home_click_home()

    def test_d_home_top_002(self):
        """首页---顶部项目切换回来"""
        self.homeHeaders.homeHeaders_click_add()
        self.homeHeaders.homeHeaders_click_replace_add()

    def test_d_home_top_003(self):
        """首页---查看车辆限行"""
        pass

    def test_e_home_notice_001(self):
        """公告---查看全部公告列表"""
        self.homeNotice.jbHomeNotice_click_notice()
        self.assertEqual(self.loginYaml['assert_notice'], self.homeNotice.jbHomeNotice_assert_notice(), msg=u"断言标题错误")

    def test_e_home_notice_002(self):
        """公告---查看新闻快报公告列表"""
        self.homeNotice.jbHomeNotice_click_icon()
        self.homeNotice.jbHomeNotice_click_news()

    def test_e_home_notice_003(self):
        """公告---查看小嘉课堂公告列表"""
        self.homeNotice.jbHomeNotice_click_icon()
        self.homeNotice.jbHomeNotice_click_classroom()

    def test_e_home_notice_004(self):
        """公告---查看温馨提示公告列表"""
        self.homeNotice.jbHomeNotice_click_icon()
        self.homeNotice.jbHomeNotice_click_prompt()

    def test_e_home_notice_005(self):
        """公告---查看活动预告公告列表"""
        self.homeNotice.jbHomeNotice_click_icon()
        self.homeNotice.jbHomeNotice_click_activity()

    def test_e_home_notice_006(self):
        """公告---查看失物招领公告列表"""
        self.homeNotice.jbHomeNotice_click_icon()
        self.homeNotice.jbHomeNotice_click_lost_found()


    def test_e_home_notice_007(self):
        """公告---查看公告内容"""
        self.homeNotice.jbHomeNotice_click_icon()
        self.homeNotice.jbHomeNotice_click_whole()
        self.homeNotice.jbHomeNotice_click_content()
        # self.homeNotice.get_switch_h5()
        # self.operate.get_back()
        # self.homeNotice.get_switch_android()
        self.operate.get_back()
        self.operate.get_back()

    def test_f_home_housekeeper_001(self):
        """管家---查看管家团队成员"""
        self.homeHousekeeper.jbHomeHousekeeper_click_housekeeper()
        self.homeHousekeeper.jbHomeHousekeeper_click_more()
        name_list = []  # 每页所有数据都写入列表
        names_list = []  # 每页最后一个写入列表
        flag = True
        while flag:
            names = self.homeHousekeeper.jbHomeHousekeeper_assert_first_name()
            for name in names:
                if name.text in name_list:
                    continue
                name_list.append(name.text)
            if names[len(names) - 1].text in names_list:
                flag = False
            else:
                names_list.append(names[len(names) - 1].text)
            self.operate.swipe_up()
        for i in name_list:
            log.info(i,)
        self.operate.get_back()

    def test_g_home_pay_001(self):
        """缴费---点击立即缴费---返回---再次点击立即缴费---缴费单取消"""
        self.homePay.jbHomePay_click_pay()
        self.homePay.jbHomePay_click_immediately_pay()
        self.operate.get_back()
        self.homePay.jbHomePay_click_immediately_pay()
        self.homePay.jbHomePay_click_go()
        time.sleep(1)
        self.homePay.jbHomePay_click_paymentSlip_cancel()
        time.sleep(1)
        self.homePay.jbHomePay_click_paymentSlip_cancel_determine()
        time.sleep(1)
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
        # self.homePay.jbHomePay_click_immediately_pay()
        # self.operate.get_back()
        # self.homePay.jbHomePay_click_immediately_pay()
        # self.homePay.jbHomePay_click_go()
        # self.homePay.jbHomePay_click_paymentSlip_pay()
        # self.homePay.jbHomePay_click_confirmation_of_payment()
        # self.operate.get_back()
        # self.homePay.jbHomePay_click_cancel_order()
        # self.homePay.jbHomePay_click_cancel_order_determine()
        # self.operate.get_back()

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
        # self.homePay.jbHomePay_click_cancel_order()
        # self.homePay.jbHomePay_click_cancel_order_determine()
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
        # self.homePay.jbHomePay_click_cancel_order()
        # self.homePay.jbHomePay_click_cancel_order_determine()
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
        # self.homePay.jbHomePay_click_cancel_order()
        # self.homePay.jbHomePay_click_cancel_order_determine()
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
        self.homePay.jbHomePay_click_zh()
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
        self.homePay.jbHomePay_click_confirmation_payment()
        self.homePay.jbHomePay_click_go()
        self.homePay.jbHomePay_click_paymentSlip_pay()
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

    def test_h_home_door_001(self):
        """一键开门---进入一键开门"""
        self.openDoor.jbHomeDoor_click_door()
        self.operate.get_back()

    def test_i_home_guarantee_001(self):
        """嘉维修---查看我的订单(进行中)"""
        self.homeGuarantee.jbHomeGuarantee_click_guarantee()
        self.homeGuarantee.jbHomeGuarantee_click_order()

    def test_i_home_guarantee_002(self):
        """嘉维修---查看我的订单(已完成)"""
        self.homeGuarantee.jbHomeGuarantee_click_done()
        self.operate.get_back()

    def test_i_home_guarantee_003(self):
        """嘉维修---公共维修提交工单失败(未选择预约时间)"""
        self.homeGuarantee.jbHomeGuarantee_click_publicGuarantee()
        self.homeGuarantee.jbHomeGuarantee_input_content(self.contentTime)
        # self.homeGuarantee.jbHomeFuarantee_click_submit()
        self.operate.get_back()

    def test_i_home_guarantee_004(self):
        """嘉维修---公共维修提交工单失败(未填写内容)"""
        self.homeGuarantee.jbHomeGuarantee_click_publicGuarantee()
        self.homeGuarantee.jbHomeGuarantee_click_select()
        self.homeGuarantee.jbHomeGuarantee_click_determine()
        # self.homeGuarantee.jbHomeFuarantee_click_submit()
        self.operate.get_back()

    def test_i_home_guarantee_005(self):
        """嘉维修---公共维修提交工单"""
        self.homeGuarantee.jbHomeGuarantee_click_publicGuarantee()
        self.homeGuarantee.jbHomeGuarantee_input_content(self.contentTime)
        self.homeGuarantee.jbHomeGuarantee_click_select()
        self.homeGuarantee.jbHomeGuarantee_click_determine()
        # self.homeGuarantee.jbHomeFuarantee_click_submit()
        self.operate.get_back()

    def test_i_home_guarantee_006(self):
        """嘉维修---灯具线路"""
        #程序限制了不能频繁提交工单,1分钟提交一次
        # time.sleep(60)
        self.homeGuarantee.jbHomeFuarantee_click_djlx()
        self.homeGuarantee.jbHomePuantee_click_immediate_appointment()
        # self.homeGuarantee.jbHomePuantee_click_frequency_determine()
        self.operate.get_back()
        time.sleep(2)
        self.operate.get_back()

    def test_i_home_guarantee_007(self):
        """嘉维修---龙头管件"""
        self.homeGuarantee.jbHomeFuarantee_click_djlx()
        self.homeGuarantee.jbHomePuantee_click_immediate_appointment()
        # self.homeGuarantee.jbHomePuantee_click_frequency_determine()
        self.operate.get_back()
        self.operate.get_back()

    def test_i_home_guarantee_008(self):
        """嘉维修---卫浴洁具"""
        self.homeGuarantee.jbHomeFuarantee_click_wyjj()
        self.homeGuarantee.jbHomePuantee_click_immediate_appointment()
        # self.homeGuarantee.jbHomePuantee_click_frequency_determine()
        self.operate.get_back()
        time.sleep(2)
        self.operate.get_back()

    def test_i_home_guarantee_009(self):
        """嘉维修---门窗家居"""
        self.homeGuarantee.jbHomeFuarantee_click_mcjj()
        self.homeGuarantee.jbHomePuantee_click_immediate_appointment()
        # self.homeGuarantee.jbHomePuantee_click_frequency_determine()
        self.operate.get_back()
        time.sleep(2)
        self.operate.get_back()

    def test_i_home_guarantee_010(self):
        """嘉维修---打孔疏通"""
        self.homeGuarantee.jbHomeFuarantee_click_dkst()
        self.homeGuarantee.jbHomePuantee_click_immediate_appointment()
        # self.homeGuarantee.jbHomePuantee_click_frequency_determine()
        self.operate.get_back()
        time.sleep(2)
        self.operate.get_back()

    def test_i_home_guarantee_011(self):
        """嘉维修---开锁换锁"""
        self.homeGuarantee.jbHomeFuarantee_click_kshs()
        self.homeGuarantee.jbHomePuantee_click_immediate_appointment()
        # self.homeGuarantee.jbHomePuantee_click_frequency_determine()
        for i in range(3):
            self.operate.get_back()
            time.sleep(1)

    def test_j_home_complaint_001(self):
        """投诉---查看进行中数据"""
        self.homeComplaint.jbHomeComplaint_click_complaint()

    def test_j_home_complaint_002(self):
        """投诉---查看已完成数据"""
        self.homeComplaint.jbHomeComplaint_click_done()

    def test_j_home_complaint_003(self):
        """投诉---新增我要表扬工单"""
        self.homeComplaint.jbHomeComplaint_click_wantPraise()
        self.homeComplaint.jbHomeComplaint_input_content(self.contentTime)
        #正式环境
        # self.homeComplaint.jbHomeComplaint_click_submit()
        #测试环境
        self.operate.get_back()

    def test_j_home_complaint_004(self):
        """投诉---新增我要投诉工单"""
        self.homeComplaint.jbHomeComplaint_click_wantComplaint()
        self.homeComplaint.jbHomeComplaint_input_content(self.contentTime)
        #正式环境
        # self.homeComplaint.jbHomeComplaint_click_submit()
        #测试环境
        self.operate.get_back()
        self.operate.get_back()


    def test_k_home_visitor_001(self):
        """访客---二维码通行访客邀请"""
        self.homeVisitor.jbHomeVisitor_click_visitor()
        self.homeVisitor.jbHomeVisitor_click_icon()
        self.homeVisitor.jbHomeVisitor_click_Current1()

    def test_k_home_visitor_002(self):
        """访客---人脸通行访客邀请(业主填写)"""
        self.homeVisitor.jbHomeVisitor_click_icon()
        self.homeVisitor.jbHomeVisitor_click_Current2()

    def test_k_home_visitor_003(self):
        """访客---人脸通行访客邀请(访客填写)"""
        self.homeVisitor.jbHomeVisitor_click_icon()
        self.homeVisitor.jbHomeVisitor_click_Current3()
        self.operate.get_back()

    # def test_l_home_selected_001(self):
    #     """嘉宝精选---添加商品到购物车"""
    #     self.selected.jbHomeSelected_click_selected()
    #     self.selected.get_switch_h5()
    #     time.sleep(5)
    #     self.selected.jbHomSelected_click_page1()
    #     time.sleep(2)
    #     self.selected.jbHomSelected_click_page2()
    #     time.sleep(2)
    #     self.selected.jbHomSelected_click_page3()
    #     time.sleep(2)
    #     self.selected.jbHomSelected_click_page4()
    #     for i in range(4):
    #         self.operate.get_back()
    #         time.sleep(1)
    #     self.selected.get_switch_android()
    #
    # def test_m_home_water_001(self):
    #     """送水上门---一键购水"""
    #     self.operate.swipe_up()
    #     self.homeWater.jbHomeWater_click_water()
    #     self.homeWater.get_switch_h5()
    #     self.homeWater.jbHomeWater_click_waterPicture()
    #     self.homeWater.jbHomeWater_click_addNum()
    #     self.homeWater.jbHomeWater_click_pay()
    #     self.operate.get_back()
    #
    # def test_m_home_water_002(self):
    #     """送水上门---预约送水"""
    #     self.homeWater.jbHomeWater_click_giveWater()
    #     # self.homeWater.jbHomeWater_click_tips()
    #     self.operate.get_back()
    #
    # def test_m_home_water_003(self):
    #     """送水上门---个人中心---我的订单"""
    #     self.homeWater.jbHomeWater_click_personal()
    #     self.homeWater.jbHomeWater_click_order()
    #     self.homeWater.jbHomeWater_click_stayDelivery()
    #     self.homeWater.jbHomeWater_click_deliveryIn()
    #     self.homeWater.jbHomeWater_click_deliveryComplete()
    #     self.homeWater.jbHomeWater_click_deliveryAbnormal()
    #     self.operate.get_back()
    #
    # def test_m_home_water_004(self):
    #     """送水上门---个人中心---我的水票"""
    #     self.homeWater.jbHomeWater_click_ticket()
    #     self.operate.get_back()
    #
    # def test_m_home_water_005(self):
    #     """送水上门---个人中心---我的地址"""
    #     self.homeWater.jbHomeWater_click_address()
    #     self.homeWater.jbHomeWater_click_newAddress()
    #     self.homeWater.jbHomeWater_click_province()
    #     self.homeWater.jbHomeWater_click_determineProvince()
    #     self.homeWater.jbHomeWater_click_village()
    #     self.homeWater.jbHomeWater_click_determineVillage()
    #     # self.homeWater.jbHomeWater_input_detailedAddress(u"四川省成都市成都市")
    #     # self.homeWater.test()
    #     # self.homeWater.jbHomeWater_input_houseNumber(123)
    #     self.homeWater.jbHomeWater_click_waterStation()
    #     self.homeWater.jbHomeWater_click_confirm()
    #     self.operate.get_back()
    #
    # def test_m_home_water_006(self):
    #     """送水上门---个人中心---编辑我的地址"""
    #     self.homeWater.jbHomeWater_click_edit()
    #     self.homeWater.jbHomeWater_click_confirm()
    #     self.operate.get_back()
    #
    # def test_m_home_water_007(self):
    #     """送水上门---个人中心---我的押金"""
    #     self.homeWater.jbHomeWater_click_deposit()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #     self.homeWater.get_switch_android()
    #
    def test_n_home_house_001(self):
        """房屋租售---查看我的房源"""
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_house()
        self.homeHouse.jbHomeCheck_click_icon()
        self.homeHouse.jbHomeCheck_click_my_housing_resources()
        self.operate.get_back()

    def test_n_home_house_002(self):
        """房屋租售---查看我的车位"""
        self.homeHouse.jbHomeCheck_click_icon()
        self.homeHouse.jbHomeCheck_click_my_publish_parking()
        self.operate.get_back()

    def test_n_home_house_003(self):
        """房屋租售---查看我的商铺"""
        self.homeHouse.jbHomeCheck_click_icon()
        self.homeHouse.jbHomeCheck_click_my_screenShops()
        self.operate.get_back()

    def test_n_home_house_004(self):
        """房屋租售---买新房"""
        self.homeHouse.jbHomeCheck_click_newHouse()
        self.homeHouse.jbHomeCheck_click_price()
        self.homeHouse.jbHomeCheck_click_screenPrice()
        self.operate.get_back()

    def test_n_home_house_005(self):
        """房屋租售---二手房"""
        self.homeHouse.jbHomeCheck_click_secondHandHouse()
        self.homeHouse.jbHomeCheck_click_price()
        self.homeHouse.jbHomeCheck_click_screenPrice()
        self.operate.get_back()

    def test_n_home_house_006(self):
        """房屋租售---出租房"""
        self.homeHouse.jbHomeCheck_click_rentHouse()
        self.homeHouse.jbHomeCheck_click_price()
        self.homeHouse.jbHomeCheck_click_screenPrice()
        self.operate.get_back()

    def test_n_home_house_007(self):
        """房屋租售---发布出租(住宅)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publishHouse()
        self.homeHouse.jbHomeCheck_click_publish_screenHouse()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_floor()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
        self.homeHouse.jbHomeCheck_click_leaseHouse_floorAll()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
        self.operate.swipe_up()
        self.operate.swipe_up()
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_008(self):
        """房屋租售---发布出租(公寓)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_flats()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_floor()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
        self.homeHouse.jbHomeCheck_click_leaseHouse_floorAll()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_009(self):
        """房屋租售---发布出租(写字楼)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_office()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_floor()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
        self.homeHouse.jbHomeCheck_click_leaseHouse_floorAll()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
        self.operate.swipe_up()
        self.operate.swipe_up()
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_010(self):
        """房屋租售---发布出租(车位)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_parking()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_parking()
        self.homeHouse.jbHomeCheck_click_leaseHouse_select_parking()
        self.homeHouse.jbHomeCheck_click_leaseHouse_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_select_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_011(self):
        """房屋租售---发布出租(商铺)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_shops()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.homeHouse.jbHomeCheck_click_leaseHouse_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_select_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_012(self):
        """房屋租售---发布出售(住宅)---发布成功"""
        self.homeHouse.jbHomeCheck_click_sell()
        self.homeHouse.jbHomeCheck_click_publish_screenHouse()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_floor()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
        self.homeHouse.jbHomeCheck_click_leaseHouse_floorAll()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_013(self):
        """房屋租售---发布出售(公寓)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_flats()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_floor()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
        self.homeHouse.jbHomeCheck_click_leaseHouse_floorAll()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
        self.operate.swipe_up()
        self.operate.swipe_up()

        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_014(self):
        """房屋租售---发布出售(写字楼)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_office()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_floor()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
        self.homeHouse.jbHomeCheck_click_leaseHouse_floorAll()
        self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
        self.operate.swipe_up()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_015(self):
        """房屋租售---发布出售(车位)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_parking()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_parking()
        self.homeHouse.jbHomeCheck_click_leaseHouse_select_parking()
        self.homeHouse.jbHomeCheck_click_leaseHouse_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_select_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_016(self):
        """房屋租售---发布出售(商铺)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_shops()
        self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
        self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
        self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
        self.homeHouse.jbHomeCheck_click_leaseHouse_areas()
        self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
        self.homeHouse.jbHomeCheck_click_leaseHouse_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_select_shops_floor()
        self.homeHouse.jbHomeCheck_click_leaseHouse_picture()
        self.homeHouse.jbHomeCheck_click_leaseHouse_gallery()
        self.homeHouse.jbHomeCheck_click_leaseHouse_album()
        self.homeHouse.jbHomeCheck_click_leaseHouse_photo()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()
        self.operate.get_back()


    def test_n_home_house_018(self):
        """房屋租售---帮我找(求租住宅)---发布成功"""
        self.homeHouse.jbHomeCheck_click_findHouse()
        self.homeHouse.jbHomeCheck_click_publish_screenHouse()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_019(self):
        """房屋租售---帮我找(求租公寓)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_flats()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_020(self):
        """房屋租售---帮我找(求租写字楼)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_office()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_021(self):
        """房屋租售---帮我找(求租车位)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_parking()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_022(self):
        """房屋租售---帮我找(求租商铺)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_shops()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_023(self):
        """房屋租售---帮我找(求售住宅)---发布成功"""
        self.homeHouse.jbHomeCheck_click_explore_market_potential()
        self.homeHouse.jbHomeCheck_click_publish_screenHouse()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_024(self):
        """房屋租售---帮我找(求售公寓)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_flats()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()



    def test_n_home_house_025(self):
        """房屋租售---帮我找(求售写字楼)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_office()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
        self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_026(self):
        """房屋租售---帮我找(求售车位)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_parking()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village()
        self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
        self.operate.get_search()
        self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()

    def test_n_home_house_027(self):
        """房屋租售---帮我找(求售商铺)---发布成功"""
        self.homeHouse.jbHomeCheck_click_publish_shops()
        self.homeHouse.jbHomeCheck_input_findHouse_title("测试")
        self.homeHouse.jbHomeCheck_click_seek_screenOffice_price()
        self.homeHouse.jbHomeCheck_click_select_seek_screenOffice_price()
        self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_province()
        self.homeHouse.jbHomeCheck_click_leaseHouse_city()
        self.homeHouse.jbHomeCheck_click_leaseHouse_area()
        self.homeHouse.jbHomeCheck_click_findHouse_areas()
        self.homeHouse.jbHomeCheck_click_select_seek_area()
        # 测试环境
        # self.homeHouse.jbHomeCheck_click_leaseHouse_release()
        #正式环境
        self.operate.get_back()
        self.operate.get_back()


    def test_n_home_house_028(self):
        """房屋租售---品质新盘"""
        self.homeHouse.jbHomeCheck_click_pzxx()
        self.homeHouse.jbHomeCheck_click_price()
        self.homeHouse.jbHomeCheck_click_screenPrice()
        self.operate.get_back()

    def test_n_home_house_029(self):
        """房屋租售---投资首选"""
        self.homeHouse.jbHomeCheck_click_tzsx()
        self.homeHouse.jbHomeCheck_click_price()
        self.homeHouse.jbHomeCheck_click_screenPrice()
        self.operate.get_back()

    def test_n_home_house_030(self):
        """房屋租售---精选车位"""
        self.homeHouse.jbHomeCheck_click_jxcw()
        self.homeHouse.jbHomeCheck_click_price()
        self.homeHouse.jbHomeCheck_click_screenPrice()
        self.operate.get_back()

    def test_n_home_house_031(self):
        """房屋租售---增值服务"""
        self.homeHouse.jbHomeCheck_click_zzfw()
        self.operate.get_back()
        self.operate.get_back()

    # def test_o_home_checkIn_001(self):
    #     """拎包入住---进入拎包入住"""
    #     self.operate.swipe_up()
    #     self.homeCheckIn.jbHomeCheckIn_click_checkIn()
    #
    # def test_o_home_checkIn_002(self):
    #     """拎包入住---热门活动"""
    #     self.homeCheckIn.jbHomeCheckIn_click_rmhd()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(3)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_o_home_checkIn_003(self):
    #     """拎包入住---参观工地"""
    #     self.homeCheckIn.jbHomeCheckIn_click_cggd()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(3)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_o_home_checkIn_004(self):
    #     """拎包入住---装修管家"""
    #     self.homeCheckIn.jbHomeCheckIn_click_zxgj()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_o_home_checkIn_005(self):
    #     """拎包入住---精品案例"""
    #     self.homeCheckIn.jbHomeCheckIn_click_jpal()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_o_home_checkIn_006(self):
    #     """拎包入住---旧房翻新"""
    #     self.homeCheckIn.jbHomeCheckIn_click_jffx()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_o_home_checkIn_007(self):
    #     """拎包入住---家具商城"""
    #     self.homeCheckIn.jbHomeCheckIn_click_jjsc()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_o_home_checkIn_008(self):
    #     """拎包入住---选设计师"""
    #     self.homeCheckIn.jbHomeCheckIn_click_xsjs()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_o_home_checkIn_009(self):
    #     """拎包入住---挑工厂"""
    #     self.homeCheckIn.jbHomeCheckIn_click_tgc()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #     self.operate.get_back()
    #
    def test_p_home_delicous_001(self):
        """美食汇---搜索店铺"""
        self.delicous.jbHomeDelicious_click_delicious()
        self.delicous.jbHomeDelicious_click_search1()
        # self.delicous.jbHomeDelicious_click_content()
        # self.delicous.jbHomeDelicious_input_content("火锅")
        # self.delicous.jbHomeDelicious_click_search2()
        # self.delicous.jbHomeDelicious_click_collection_shop()
        # for i in range(2):
        #     self.operate.get_back()
        self.operate.get_back()

    def test_p_home_delicous_002(self):
        """美食汇---我的收藏"""
        self.delicous.jbHomeDelicious_click_collection()
        self.delicous.jbHomeDelicious_click_collection_shop()
        for i in range(2):
            self.operate.get_back()

    def test_p_home_delicous_003(self):
        """美食汇---就吃火锅"""
        self.delicous.jbHomeDelicous_click_all_classification()
        self.delicous.jbHomeDelicous_click_classification1()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()


    def test_p_home_delicous_004(self):
        """美食汇---烤系列"""
        self.delicous.jbHomeDelicous_click_classification2()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_005(self):
        """美食汇---撸个串"""
        self.delicous.jbHomeDelicous_click_classification3()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_006(self):
        """美食汇---热卤小吃"""
        self.delicous.jbHomeDelicous_click_classification4()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_007(self):
        """美食汇---抗疫专区"""
        self.delicous.jbHomeDelicous_click_classification5()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_008(self):
        """美食汇---轻奢中餐"""
        self.delicous.jbHomeDelicous_click_classification6()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_009(self):
        """美食汇---商务宴请"""
        self.delicous.jbHomeDelicous_click_classification7()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_010(self):
        """美食汇---网红打卡"""
        self.delicous.jbHomeDelicous_click_classification8()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_011(self):
        """美食汇---春季汤锅"""
        self.delicous.jbHomeDelicous_click_classification9()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        self.operate.get_back()

    def test_p_home_delicous_012(self):
        """美食汇---春季汤锅"""
        self.delicous.jbHomeDelicous_click_classification10()
        self.delicous.jbHomeDelicious_click_collection_shop()
        self.operate.get_back()
        self.delicous.jbHomeDelicous_click_score_sort()
        self.delicous.jbHomeDelicous_click_latest_online()
        for i in range(3):
            self.operate.get_back()


    # def test_q_Intelligent_001(self):
    #     """智控---进入智控"""
    #     self.home.home_click_security()

    # def test_r_shoppopping_001(self):
    #     """商城---切换到商城"""
    #     self.home.home_click_shopping()
    #     self.shop.get_switch_h5()
    #     self.shop.get_switch_android()

    def test_s_neighbor_001(self):
        """邻里---社区活动---查看第一个活动"""
        self.home.home_click_neighbor()
        self.neighbor.jbNeighbor_click_activity()
        self.neighbor.jbNeighbor_click_activity1()
        self.operate.get_back()

    def test_s_neighbor_002(self):
        """邻里---跳蚤市场---查看第一个帖子"""
        self.neighbor.jbNeighbor_click_market()
        self.neighbor.jbNeighbor_click_market_post()
        self.operate.get_back()

    def test_s_neighbor_006(self):
        """邻里---跳蚤市场---发帖"""
    #     self.neighbor.jbNeighbor_click_market_posting()
    #     self.neighbor.jbNeighbor_input_posting_content("发帖内容")
    #     self.neighbor.jbNeighbor_click_picture_icon()
    #     self.neighbor.jbNeighbor_click_picture()
    #     self.neighbor.jbNeighbor_click_album()
    #     self.neighbor.jbNeighbor_click_photo()
    #     self.neighbor.jbNeighbor_input_market_price("100")
    #     self.neighbor.jbNeighbor_click_market_classification()
    #     self.neighbor.jbNeighbor_click_market_select_classification()
    #     self.neighbor.jbNeighbor_input_market_phone("13683450124")
    #     self.neighbor.jbNeighbor_click_market_release()
    #
    def test_t_jiaDou_001(self):
        """嘉豆---嘉豆列表"""
        self.home.home_click_me()
        self.jiaDou.jbJiaDou_click_jiaDou()
        time.sleep(1)
        # self.assertEquals(self.loginYaml['assert_jiaDou'],self.jiaDou.jbJiaDou_assert_jiaDou(),msg="")

    def test_t_jiaDou_002(self):
        """嘉豆---赠送嘉豆"""
        self.jiaDou.jbJiaDou_click_give()
        time.sleep(1)
        # self.assertEquals(self.loginYaml['assert_give'],self.jiaDou.jbJiaDou_assert_give(),msg="")
        self.jiaDou.jbJia_input_giveNum(100)
        self.jiaDou.jbJiaDou_input_giveNumber("13683450124")
        self.jiaDou.jbJiaDou_click_confirm()
        self.jiaDou.jbJiaDou_input_password("123456")
        self.jiaDou.jbJiaDou_click_button()
        self.jiaDou.jbJiaDou_click_complete()

    def test_t_jiaDou_003(self):
        """嘉豆---修改密码"""
        self.jiaDou.jbJiaDou_click_alterPwd()
        # self.assertEquals(u"修改密码",self.jiaDou.jbJiaDou_assert_alterPwd(),msg="")
        self.jiaDou.jbJiaDou_click_alterPwd_confirm()
        self.operate.get_back()

    def test_t_jiaDou_004(self):
        """嘉豆---使用规则"""
        # self.jiaDou.jbJiaDou_click_rule()
        # self.orders.get_switch_h5()
        # self.operate.get_back()
        # self.orders.get_switch_android()
        self.operate.get_back()
    #
    # def test_u_coupon_001(self):
    #     """优惠券---查看"""
    #     self.coupon.jbCoupon_click_coupon()
    #     self.coupon.get_switch_h5()
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    def test_v_setting_001(self):
        """设置---修改资料"""
        self.setting.jbSetting_click_head()
        self.setting.jbSetting_click_edit()
        self.setting.jbSetting_click_preservation()

    # def test_v_setting_002(self):
    #     """设置---房屋解绑"""
    #     self.setting.jbSetting_click_project_add()
    #     self.setting.jbSetting_click_untying_house()
    #     self.setting.jbSetting_click_untying_house_reason()
    #     self.setting.jbSetting_click_select_reason_determine()
    #
    # def test_v_setting_003(self):
    #     """设置---房屋绑定(成功)"""
    #     time.sleep(10)
    #     self.setting.jbSetting_click_add_house()
    #     #城市
    #     self.setting.jbSetting_click_city()
    #     self.setting.jbSetting_click_select_city()
    #     self.operate.get_back()
    #     #社区
    #     #正式环境
    #     self.setting.jbSetting_click_community()
    #     self.setting.jbSetting_input_community_name("生活家智慧小区")
    #     self.setting.jbSetting_click_select_community_name()
    #     self.operate.get_back()
    #     #测试环境
    #     # self.setting.jbSetting_click_community()
    #     # self.setting.jbSetting_click_select_pixian()
    #     # self.setting.jbSetting_click_select_community()
    #     # self.operate.get_back()
    #     #楼栋号
    #     self.setting.jbSetting_click_building()
    #     self.setting.jbSetting_click_select_building_formal()
    #     self.operate.get_back()
    #     #单元房号
    #     self.setting.jbSetting_click_unit_room_number()
    #     self.setting.jbSetting_click_select_unit_room_number_formal()
    #     #手机号
    #     self.setting.jbSetting_input_mobile("5555")
    #     self.setting.jbSetting_click_verification()
    #     self.operate.get_back()
    #     time.sleep(4)
    #
    # def test_v_setting_005(self):
    #     """设置---房屋绑定(失败,绑定已绑定的其他房屋)"""
    #     self.setting.jbSetting_click_add_house()
    #     #城市
    #     self.setting.jbSetting_click_city()
    #     self.setting.jbSetting_click_select_city()
    #     self.operate.get_back()
    #     #社区
    #     self.setting.jbSetting_click_community()
    #     self.setting.jbSetting_click_select_pixian()
    #     self.setting.jbSetting_click_select_community()
    #     self.operate.get_back()
    #     #楼栋号
    #     self.setting.jbSetting_click_building()
    #     self.setting.jbSetting_click_select_building()
    #     self.operate.get_back()
    #     #单元房号
    #     self.setting.jbSetting_click_unit_room_number()
    #     self.setting.jbSetting_click_select_unit_room_number()
    #     #手机号
    #     self.setting.jbSetting_input_mobile("8888")
    #     self.setting.jbSetting_click_verification()
    #
    # def test_w_orders_001(self):
    #     """我的订单---待付款"""
    #     self.orders.jbOrders_click_payment()
    #     self.orders.get_switch_h5()
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    # def test_w_orders_002(self):
    #     """我的订单---待发货"""
    #     self.orders.jbOrders_click_deliver_goods()
    #     self.orders.get_switch_h5()
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    # def test_w_orders_003(self):
    #     """我的订单---待收货"""
    #     self.orders.jbOrders_click_receiving_goods()
    #     self.orders.get_switch_h5()
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    # def test_w_orders_004(self):
    #     """我的订单---待评价"""
    #     self.orders.jbOrders_click_evaluate()
    #     self.orders.get_switch_h5()
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    # def test_w_orders_005(self):
    #     """我的订单---售后服务"""
    #     self.orders.jbOrders_click_after_sale()
    #     self.orders.get_switch_h5()
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    # def test_w_orders_006(self):
    #     """我的订单---中奖纪录"""
    #     self.orders.jbOrders_click_winning_the_prize()
    #     # self.assertEquals(self.loginYaml['assert_winning_the_prize'],self.orders.jbOrders_assert_winning_the_prize(),msg="")
    #     self.operate.get_back()
    #
    # def test_w_orders_007(self):
    #     """我的订单---缴费记录"""
    #     self.orders.jbOrders_click_pay()
    #     self.assertEquals(self.loginYaml['assert_pay'],self.orders.jbOrders_assert_pay(),msg="")
    #     self.operate.get_back()
    #
    # def test_w_orders_008(self):
    #     """我的订单---我的活动"""
    #     self.orders.jbOrders_click_activity()
    #     self.assertEquals(self.loginYaml['assert_activity'],self.orders.jbOrders_assert_activity(),msg="")
    #     self.operate.get_back()
    #
    # def test_w_orders_009(self):
    #     """我的订单---我的消息"""
    #     self.orders.jbOrders_click_news()
    #     self.orders.get_switch_h5()
    #     self.assertEquals(self.loginYaml['assert_news'],self.orders.jbOrders_assert_news(),msg="")
    #     self.orders.jbOrders_click_read()
    #     time.sleep(2)
    #     self.orders.jbOrders_click_unRead()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    # def test_w_orders_010(self):
    #     """我的订单---我的房源"""
    #     self.orders.jbOrders_click_housing_resources()
    #     self.assertEquals(self.loginYaml['assert_housing_resources'],self.orders.jbOrders_assert_housing_resources(),msg="")
    #     self.operate.get_back()
    #
    # def test_w_orders_011(self):
    #     """我的订单---我的发票(物业缴费)"""
    #     self.orders.jbOrders_click_invoice()
    #     self.assertEquals(self.loginYaml['assert_invoice'],self.orders.jbOrders_assert_invoice(),msg="")
    #     self.orders.jbOrders_click_wuye_pay()
    #     self.operate.get_back()
    #
    # def test_w_orders_012(self):
    #     """我的订单---我的发票（临停开票）"""
    #     self.orders.jbOrders_click_draw_bill()
    #     self.operate.get_back()
    #
    # def test_w_orders_013(self):
    #     """我的订单---我的发票（开票历史）"""
    #     self.orders.jbOrders_click_bill_history()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #
    # def test_w_orders_014(self):
    #     """我的订单---商务合作"""
    #     self.orders.jbOrders_click_cooperation()
    #     self.orders.get_switch_h5()
    #     time.sleep(3)
    #     self.operate.get_back()
    #     self.orders.get_switch_android()
    #
    def test_z_loginOut_001(self):
        """个人设置---修改密码"""
        self.login.login_click_icon()
        self.setting.jbSetting_click_change_password()
        self.operate.get_back()

    def test_z_loginOut_002(self):
        """个人设置---清除缓存"""
        self.setting.jbSetting_click_clear_cache()
        self.setting.jbSetting_click_sure_clear_cache()
        time.sleep(2)

    def test_z_loginOut_003(self):
        """个人设置---切换智控模式"""
        self.setting.jbSetting_click_zhikong_pattern()
        self.setting.jbSetting_click_switch_zhikong_pattern()
        time.sleep(2)

    def test_z_loginOut_004(self):
        """个人设置---切换摇一摇开门"""
        self.setting.jbSetting_click_shake()
        time.sleep(2)

    # def test_z_loginOut_005(self):
    #     """个人设置---切换通知声音"""
    #     self.setting.jbSetting_click_notification_voice()
    #     time.sleep(2)
    #
    # def test_z_loginOut_006(self):
    #     """个人设置---切换通知震动"""
    #     self.setting.jbSetting_click_notification_vibration()
    #     time.sleep(2)

    def test_z_loginOut_007(self):
        """个人设置---意见反馈"""
        self.setting.jbSetting_click_feedback()
        self.operate.get_back()
        time.sleep(2)

    def test_z_loginOut_008(self):
        """个人设置---关于生活家"""
        self.setting.jbSetting_click_home()
        self.operate.get_back()
        time.sleep(2)

    # def test_z_loginOut_009(self):
    #     """个人设置---个人信息投诉"""
    #     self.setting.jbSetting_click_complaint()
    #     self.setting.jbSetting_click_complaint1()
    #     self.setting.jbSetting_click_select_reason()
    #     self.setting.jbSetting_click_confirm_complaint()
    #     self.setting.jbSetting_click_button()
    #     self.operate.get_back()

    def test_z_loginOut_010(self):
        """个人设置---账号注销"""
        self.setting.jbSetting_click_cancellation()
        self.operate.get_back()

    def test_z_loginOut_011(self):
        """个人设置---退出登录"""
        self.login.login_click_loginOut()
        self.login.login_click_sure()

    @classmethod
    def tearDownClass(cls):
        # PublicExcel("../report/locust.xls").write_excel(0,4,1,datetime.datetime.now())
        # start_time =
        pass

if __name__ == '__main__':
    unittest.main()
