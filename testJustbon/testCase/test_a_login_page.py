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
        PublicPhone().write_excel()
        # PublicExcel("../config/locust.xls").write_excel()
    def setUp(self):
        pass

    def test_a_login_001(self):
        """登录---进入登录"""
        time.sleep(10)
        self.home.home_click_me()
        self.assertEqual(self.loginYaml['assert_loginImmediately'], self.login.login_assert_loginImmediately(),msg=u"断言立即登录失败")
        self.login.login_click_loginImmediately()
        self.assertEqual(self.loginYaml['assert_login'], self.login.login_assert_login(), msg=u"断言登录失败")

    # @data(["",""],["13683450124","1256"],["","123456"],["13683450124",""],["13683450125","123ab"])
    @data(["13683450124", "123123"])
    @unpack
    def test_a_login_002(self, username, password):
        """登录---各种异常登录"""
        self.login.login_input_username(username)
        self.login.login_input_password(password)
        self.login.login_click_login()
        self.assertEqual(self.loginYaml['assert_login'], self.login.login_assert_login(), msg=u"断言失败")

    def test_a_login_003(self):
        """正确的账号密码---登录"""
        # sql_mobile_name = "select nichen_ from jcp_core_sys_contact  where mobile_='%s'" % (self.loginYaml['username'])
        # mobile_name = publicSql.publicSql(sql_mobile_name)
        # encryption_mobile = str(self.loginYaml['username'][0:3] + "****" + str(self.loginYaml['username'][7:12]))
        # sql_project_name = "select d.name_ from jcp_core_sys_contact c left join jcp_core_pm_project d on c.project_id_=d.project_id_ where c.mobile_='%s'" % (self.loginYaml['username'])
        # sql_project_resource_name = "select d.name_ from jcp_core_sys_contact c left join jcp_core_pm_project_resource d on c.project_id_=d.project_id_ and c.resource_id_=d.resource_id_ where c.mobile_='%s'" % (self.loginYaml['username'])
        self.login.login_input_username(self.loginYaml['username'])
        self.login.login_input_password(self.loginYaml['password'])
        self.login.login_click_login()
        time.sleep(4)
        self.operate.get_back()
        # self.assertIn(mobile_name[0],self.login.login_assert_name(),msg=u"断言名称失败")
        # self.assertEqual(encryption_mobile,self.login.login_assert_encryptionUserName(),msg=u"断言加密手机号失败")
        # self.assertIn((publicSql.publicSql(sql_project_name))[0],self.login.login_assert_add(),msg=u"断言地址失败")
        # self.assertIn((publicSql.publicSql(sql_project_resource_name))[0],self.login.login_assert_add(),msg=u"断言地址失败")

    def test_b_homeHeaders_001(self):
        """首页---顶部信息(限行)"""
        self.home.home_click_home()
        # self.assertEqual(self.homeHeaders.homeHeader_LimitRow_small(),self.homeHeaders.homeHeaders_assert_LimitRow_small(),msg=u"断言限行错误")
        # self.assertEqual(self.homeHeaders.homeHeader_LimitRow_large(),self.homeHeaders.homeHeaders_assert_LimitRow_large(),msg=u"断言限行错误")

    # def test_b_homeHeaders_002(self):
    #     """首页---切换项目"""
    #     self.homeHeaders.homeHeaders_click_add()
    #     self.homeHeaders.homeHeaders_click_replace_add()
    #     replace= self.homeHeaders.homeHeaders_assert_add()
    #     #切换到我的页面，判断项目是否更换成功
    #     self.home.home_click_me()
    #     # self.assertIn(replace,self.setting.JbSetting_assert_project_name(),msg="")
    #     self.home.home_click_home()
    #
    # def test_b_homeHeaders_003(self):
    #     """首页----再次切换项目"""
    #     self.homeHeaders.homeHeaders_click_add()
    #     self.homeHeaders.homeHeaders_click_replace_add()
    #
    # def test_c_homeNotice_001(self):
    #     """公告---每个类型的切换"""
    #     self.homeNotice.jbHomeNotice_click_notice()
    #     self.assertEqual(self.loginYaml['assert_notice'], self.homeNotice.jbHomeNotice_assert_notice(), msg=u"断言标题错误")
    #     self.homeNotice.jbHomeNotice_click_icon()
    #     self.homeNotice.jbHomeNotice_click_news()
    #
    #     self.homeNotice.jbHomeNotice_click_icon()
    #     self.homeNotice.jbHomeNotice_click_classroom()
    #
    #     self.homeNotice.jbHomeNotice_click_icon()
    #     self.homeNotice.jbHomeNotice_click_prompt()
    #
    #     self.homeNotice.jbHomeNotice_click_icon()
    #     self.homeNotice.jbHomeNotice_click_activity()
    #
    #     self.homeNotice.jbHomeNotice_click_icon()
    #     self.homeNotice.jbHomeNotice_click_lost_found()
    #
    # def test_c_homeNotice_002(self):
    #     """公告---搜索栏搜索关键字"""
        self.homeNotice.jbHomeNotice_click_icon()
        self.homeNotice.jbHomeNotice_click_whole()
        self.homeNotice.jbHomeNotice_input_search(self.loginYaml['send_keys_input_search'])
        self.operate.get_search()
    #
    # def test_c_homeNotice_003(self):
    #     """公告---查看公告内容"""
    #     self.homeNotice.jbHomeNotice_click_content()
    #     self.homeNotice.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeNotice.get_switch_android()
    #     self.operate.get_back()
    #     time.sleep(2)
    #
    # def test_d_homeHousekeeper_001(self):
    #     """管家---查看管家团队成员"""
    #     self.homeHousekeeper.jbHomeHousekeeper_click_housekeeper()
    #     self.homeHousekeeper.jbHomeHousekeeper_click_more()
    #     name_list = []  # 每页所有数据都写入列表
    #     names_list = []  # 每页最后一个写入列表
    #     flag = True
    #     while flag:
    #         names = self.homeHousekeeper.jbHomeHousekeeper_assert_first_name()
    #         for name in names:
    #             if name.text in name_list:
    #                 continue
    #             name_list.append(name.text)
    #         if names[len(names) - 1].text in names_list:
    #             flag = False
    #         else:
    #             names_list.append(names[len(names) - 1].text)
    #         self.operate.swipe_up()
    #     for i in name_list:
    #         log.info(i, )
    #     # sql="select d.NAME_ from jcp_core_sys_contact c left join jcp_core_servant_team d on c.project_id_=d.PROJECT_ID_ where c.mobile_='%s'"%(self.loginYaml['username'])
    #     # sql_reult = publ1icSql.publicSqlAll(sql)
    #     # sql_names_list=[]
    #     # for i in sql_reult:
    #     #     sql_names_list.append(i[0])
    #     # for i in name_list:
    #     #     self.assertIn(i,sql_names_list,msg=u"管家成员不一致")
    #     self.operate.get_back()
    #
    # def test_e_homePay_001(self):
    #     """缴费---查看缴费单"""
    #     self.homePay.jbHomePay_click_pay()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #
    # def test_e_homePay_002(self):
    #     """缴费---查看物业缴费开票"""
    #     self.homePay.jbHomePay_click_invoice()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_003(self):
    #     """缴费---预存物业费(选择使用招行)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #
    # def test_e_homePay_004(self):
    #     """缴费---预存物业费(招行待支付取消订单)"""
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_cancel_order()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.homePay.jbHomePay_click_cancel_order_determine_return()
    #
    # def test_e_homePay_005(self):
    #     """缴费---预存物业费(招行缴费单取消订单)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_006(self):
    #     """缴费---预存物业费(招行缴费单进行再次支付)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_pay_order()
    #     for i in range(2):
    #         self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_007(self):
    #     """缴费---预存物业费(选择使用微信)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #
    # def test_e_homePay_008(self):
    #     """缴费---预存物业费(微信待支付取消订单)"""
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_cancel_order()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.homePay.jbHomePay_click_cancel_order_determine_return()
    #
    # def test_e_homePay_009(self):
    #     """缴费---预存物业费(微信缴费单取消订单)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_010(self):
    #     """缴费---预存物业费(微信缴费单进行再次支付)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_pay_order()
    #     for i in range(2):
    #         self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_011(self):
    #     """缴费---预存物业费(选择使用支付宝)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_zfb()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #
    #
    # def test_e_homePay_012(self):
    #     """缴费---预存物业费(支付宝待支付取消订单)"""
    #
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_cancel_order()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.homePay.jbHomePay_click_cancel_order_determine_return()
    #
    # def test_e_homePay_013(self):
    #     """缴费---预存物业费(支付宝缴费单取消订单)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_zfb()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_014(self):
    #     """缴费---预存物业费(支付宝缴费单进行再次支付)"""
    #     self.homePay.jbHomePay_click_pre_storage()
    #     self.homePay.jbHomePay_click_pre_storage_determine()
    #     self.homePay.jbHomePay_input_pre_storage_money()
    #     self.homePay.jbHomePay_click_immediate_payment()
    #     self.homePay.jbHomePay_click_zfb()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_pay_order()
    #     self.operate.get_back()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_015(self):
    #     """缴费---全部待缴账单缴费(招行)"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_016(self):
    #     """缴费---全部待缴费订单取消(招行)"""
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_017(self):
    #     """缴费---全部待缴账单缴费(使用微信)"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_018(self):
    #     """缴费---全部待缴费订单取消(微信)"""
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_019(self):
    #     """缴费---全部待缴账单缴费(支付宝)"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.homePay.jbHomePay_click_zfb()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_020(self):
    #     """缴费---全部待缴费订单取消(支付宝)"""
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(5)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_021(self):
    #     """缴费----部分待缴账单缴费(招行)"""
    #     self.homePay.jbHomePay_click_first_bill()
    #     self.homePay.jbHomePay_click_confirmation_payment()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_022(self):
    #     """缴费----部分待缴订单取消(招行)"""
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_023(self):
    #     """缴费----部分待缴账单缴费(微信)"""
    #     self.homePay.jbHomePay_click_first_bill()
    #     self.homePay.jbHomePay_click_confirmation_payment()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_024(self):
    #     """缴费----部分待缴订单取消(微信)"""
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_025(self):
    #     """缴费----部分待缴账单缴费(支付宝)"""
    #     self.homePay.jbHomePay_click_first_bill()
    #     self.homePay.jbHomePay_click_confirmation_payment()
    #     self.homePay.jbHomePay_click_zfb()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_e_homePay_026(self):
    #     """缴费----部分待缴订单取消(支付宝)"""
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     time.sleep(10)
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_027(self):
    #     """缴费---点击立即缴费后--->在缴费单取消订单"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    #
    # def test_e_homePay_028(self):
    #     """缴费---点击立即缴费后--->在缴费单使用微信支付--->取消订单"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_cancel_order()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_029(self):
    #     """缴费---点击立即缴费后--->在缴费单使用支付宝支付--->取消订单"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_zfb()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_cancel_order()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # # def test_e_homePay_030(self):
    # #     """缴费---点击立即缴费后--->在缴费单使用招行支付--->取消订单"""
    # #     self.homePay.jbHomePay_click_immediately_pay()
    # #     self.operate.get_back()
    # #     self.homePay.jbHomePay_click_paymentSlip()
    # #     self.homePay.jbHomePay_click_paymentSlip_pay()
    # #     self.homePay.jbHomePay_click_wx()
    # #     self.homePay.jbHomePay_click_confirmation_of_payment()
    # #     self.operate.get_back()
    # #     self.homePay.jbHomePay_click_cancel_order()
    # #     self.homePay.jbHomePay_click_cancel_order_determine()
    # #     self.operate.get_back()
    #
    # def test_e_homePay_031(self):
    #     """缴费---点击立即缴费后--->在缴费单使用微信支付--->在缴费单取消订单"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    #
    # def test_e_homePay_032(self):
    #     """缴费---点击立即缴费后--->在缴费单使用支付宝支付--->在缴费单取消订单"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_zfb()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_paymentSlip()
    #     self.homePay.jbHomePay_click_paymentSlip_cancel()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_034(self):
    #     """缴费---点击立即缴费后--->在缴费单使用招行支付--->在缴费单取消订单"""
    #     pass
    #
    # def test_e_homePay_035(self):
    #     """缴费---点击立即缴费后--->返回再次点击立即缴费--->在缴费单使用微信支付,取消订单"""
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_immediately_pay()
    #     self.homePay.jbHomePay_click_go()
    #     self.homePay.jbHomePay_click_paymentSlip_pay()
    #     self.homePay.jbHomePay_click_wx()
    #     self.homePay.jbHomePay_click_confirmation_of_payment()
    #     self.operate.get_back()
    #     self.homePay.jbHomePay_click_cancel_order()
    #     self.homePay.jbHomePay_click_cancel_order_determine()
    #     self.operate.get_back()
    #
    # def test_e_homePay_036(self):
    #     """缴费---查看历史账单"""
    #     self.homePay.jbHomePay_click_historyPay()
    #     self.operate.get_back()
    #
    # def test_f_homeGuarantee_001(self):
    #     """嘉维修---公共维修"""
    #     self.homeGuarantee.jbHomeGuarantee_click_guarantee()
    #     self.homeGuarantee.jbHomeGuarantee_click_publicGuarantee()
    #     self.homeGuarantee.jbHomeGuarantee_input_content(self.contentTime)
    #     self.homeGuarantee.jbHomeGuarantee_click_select()
    #     self.homeGuarantee.jbHomeGuarantee_click_determine()
    #     # self.homeGuarantee.jbHomeFuarantee_click_submit()
    #     self.operate.get_back()
    #
    # def test_f_homeGuarantee_002(self):
    #     """嘉维修---查看进行中的订单"""
    #     self.homeGuarantee.jbHomeGuarantee_click_order()
    #
    # def test_f_homeGuarantee_003(self):
    #     """嘉维修---查看已完成的订单"""
    #     self.homeGuarantee.jbHomeGuarantee_click_done()
    #
    # def test_f_homeGuarantee_004(self):
    #     """嘉维修---房屋维修遍历操作"""
    #     self.operate.get_back()
    #     self.homeGuarantee.jbHomeFuarantee_click_djlx()
    #     self.operate.get_back()
    #     self.homeGuarantee.jbHomeFuarantee_click_ltgj()
    #     self.operate.get_back()
    #     self.homeGuarantee.jbHomeFuarantee_click_wyjj()
    #     self.operate.get_back()
    #     self.homeGuarantee.jbHomeFuarantee_click_mcjj()
    #     self.operate.get_back()
    #     self.homeGuarantee.jbHomeFuarantee_click_dkst()
    #     self.operate.get_back()
    #     self.homeGuarantee.jbHomeFuarantee_click_kshs()
    #     self.operate.get_back()
    #
    # def test_f_homeGuarantee_005(self):
    #     """嘉维修---安防预约"""
    #     self.homeGuarantee.jbHomeFuantee_click_afyy()
    #     self.operate.get_back()
    #     self.operate.get_back()

    def test_f_homeOpenDoor_001(self):
        """开门---进入开门"""
        self.openDoor.jbHomeDoor_click_door()
        self.operate.get_back()
        self.operate.get_back()


    def test_g_homeComplaint_001(self):
        """投诉---查看进行中数据"""
        self.homeComplaint.jbHomeComplaint_click_complaint()

    def test_g_homeComplaint_002(self):
        """投诉---查看已完成数据"""
        self.homeComplaint.jbHomeComplaint_click_done()


    def test_g_homeComplaint_003(self):
        """投诉---新增我要表扬工单"""
        self.homeComplaint.jbHomeComplaint_click_wantPraise()
        self.homeComplaint.jbHomeComplaint_input_content(self.contentTime)
        # self.homeComplaint.jbHomeComplaint_click_submit()
        self.operate.get_back()

    def test_g_homeComplaint_004(self):
        """投诉---新增我要投诉工单"""
        self.homeComplaint.jbHomeComplaint_click_wantComplaint()
        self.homeComplaint.jbHomeComplaint_input_content(self.contentTime)
        # self.homeComplaint.jbHomeComplaint_click_submit()
        self.operate.get_back()
        self.operate.get_back()

    def test_h_homeVisitor_001(self):
        """访客---新增访客"""
        self.homeVisitor.jbHomeVisitor_click_visitor()
        self.homeVisitor.jbHomeVisitor_click_newVisitor()
        self.homeVisitor.jbHomeVisitor_input_name(u"小西")
        self.homeVisitor.jbHomeVisitor_input_num()
        self.homeVisitor.jbHomeVisitor_click_submit()

    def test_h_homeVisitor_002(self):
        """访客---取消作废邀请码"""
        self.homeVisitor.jbHomeVisitor_click_delete()
        self.homeVisitor.jbHomeVisitor_click_cancel()

    def test_h_homeVisitor_003(self):
        """访客---确定作废邀请码"""
        self.homeVisitor.jbHomeVisitor_click_delete()
        self.homeVisitor.jbHomeVisitor_click_sure()
        self.operate.get_back()
        time.sleep(2)
        self.operate.get_back()
        self.operate.get_back()


    # def test_i_selected_001(self):
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

    def test_j_homeWater_001(self):
        """送水上门---一键购水"""
        self.operate.swipe_up()
        self.homeWater.jbHomeWater_click_water()
        self.homeWater.get_switch_h5()
        self.homeWater.jbHomeWater_click_waterPicture()
        self.homeWater.jbHomeWater_click_addNum()
        self.homeWater.jbHomeWater_click_pay()
        self.operate.get_back()

    def test_j_homeWater_002(self):
        """送水上门---预约送水"""
        self.homeWater.jbHomeWater_click_giveWater()
        # self.homeWater.jbHomeWater_click_tips()
        self.operate.get_back()

    def test_j_homeWater_003(self):
        """送水上门---个人中心---我的订单"""
        self.homeWater.jbHomeWater_click_personal()
        self.homeWater.jbHomeWater_click_order()
        self.homeWater.jbHomeWater_click_stayDelivery()
        self.homeWater.jbHomeWater_click_deliveryIn()
        self.homeWater.jbHomeWater_click_deliveryComplete()
        self.homeWater.jbHomeWater_click_deliveryAbnormal()
        self.operate.get_back()

    def test_j_homeWater_004(self):
        """送水上门---个人中心---我的水票"""
        self.homeWater.jbHomeWater_click_ticket()
        self.operate.get_back()

    def test_j_homeWater_005(self):
        """送水上门---个人中心---我的地址"""
        self.homeWater.jbHomeWater_click_address()
        self.homeWater.jbHomeWater_click_newAddress()
        self.homeWater.jbHomeWater_click_province()
        self.homeWater.jbHomeWater_click_determineProvince()
        self.homeWater.jbHomeWater_click_village()
        self.homeWater.jbHomeWater_click_determineVillage()
        # self.homeWater.jbHomeWater_input_detailedAddress(u"四川省成都市成都市")
        # self.homeWater.test()
        # self.homeWater.jbHomeWater_input_houseNumber(123)
        self.homeWater.jbHomeWater_click_waterStation()
        self.homeWater.jbHomeWater_click_confirm()
        self.operate.get_back()

    def test_j_homeWater_006(self):
        """送水上门---个人中心---编辑我的地址"""
        self.homeWater.jbHomeWater_click_edit()
        self.homeWater.jbHomeWater_click_confirm()
        self.operate.get_back()

    def test_j_homeWater_007(self):
        """送水上门---个人中心---我的押金"""
        self.homeWater.jbHomeWater_click_deposit()
        self.operate.get_back()
        self.operate.get_back()
        self.operate.get_back()
        self.homeWater.get_switch_android()

    # def test_k_homeCheckIn_001(self):
    #     """拎包入住---进入拎包入住"""
    #     self.operate.swipe_up()
    #     self.homeCheckIn.jbHomeCheckIn_click_checkIn()
    #
    # def test_k_homeCheckIn_002(self):
    #     """拎包入住---热门活动"""
    #     self.homeCheckIn.jbHomeCheckIn_click_rmhd()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(3)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_k_homeCheckIn_003(self):
    #     """拎包入住---参观工地"""
    #     self.homeCheckIn.jbHomeCheckIn_click_cggd()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(3)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_k_homeCheckIn_004(self):
    #     """拎包入住---装修管家"""
    #     self.homeCheckIn.jbHomeCheckIn_click_zxgj()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_k_homeCheckIn_005(self):
    #     """拎包入住---精品案例"""
    #     self.homeCheckIn.jbHomeCheckIn_click_jpal()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_k_homeCheckIn_006(self):
    #     """拎包入住---旧房翻新"""
    #     self.homeCheckIn.jbHomeCheckIn_click_jffx()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_k_homeCheckIn_007(self):
    #     """拎包入住---家具商城"""
    #     self.homeCheckIn.jbHomeCheckIn_click_jjsc()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_k_homeCheckIn_008(self):
    #     """拎包入住---选设计师"""
    #     self.homeCheckIn.jbHomeCheckIn_click_xsjs()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_k_homeCheckIn_009(self):
    #     """拎包入住---挑工厂"""
    #     self.homeCheckIn.jbHomeCheckIn_click_tgc()
    #     self.homeCheckIn.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_001(self):
    #     """房屋租售---进入房屋租售"""
    #     self.homeHouse.jbHomeCheck_click_house()
    #
    # def test_l_homeHouse_002(self):
    #     """房屋租售---我的房源"""
    #     self.homeHouse.jbHomeCheck_click_icon()
    #     self.homeHouse.jbHomeCheck_click_my_housing_resources()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_003(self):
    #     """房屋租售---我的车位"""
    #     self.homeHouse.jbHomeCheck_click_icon()
    #     self.homeHouse.jbHomeCheck_click_my_publish_parking()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_004(self):
    #     """房屋租售---我的商铺"""
    #     self.homeHouse.jbHomeCheck_click_icon()
    #     self.homeHouse.jbHomeCheck_click_my_screenShops()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_005(self):
    #     """房屋租售---搜索小区(没有数据)"""
    #     self.homeHouse.jbHomeCheck_click_search()
    #     self.homeHouse.jbHomeCheck_input_content(u"顺江小区")
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_006(self):
    #     """房屋租售---搜索小区(有数据)"""
    #     self.homeHouse.jbHomeCheck_click_search()
    #     # self.homeHouse.jbHomeCheck_input_content(u"天府逸家二期")
    #
    # def test_l_homeHouse_007(self):
    #     """房屋租售---房源详情"""
    #     self.homeHouse.jbHomeCheck_click_first_screenHouse()
    #     self.homeHouse.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeHouse.get_switch_android()
    #     self.operate.get_back()
    #     time.sleep(2)
    #     print("滑动")
    #     self.operate.swipe_down()
    #
    # def test_l_homeHouse_008(self):
    #     """房屋租售---买新房"""
    #     self.homeHouse.jbHomeCheck_click_newHouse()
    #     self.homeHouse.jbHomeCheck_click_price()
    #     self.homeHouse.jbHomeCheck_click_screenPrice()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_009(self):
    #     """房屋租售---二手房"""
    #     self.homeHouse.jbHomeCheck_click_secondHandHouse()
    #     self.homeHouse.jbHomeCheck_click_price()
    #     self.homeHouse.jbHomeCheck_click_screenPrice()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_010(self):
    #     """房屋租售---出租房"""
    #     self.homeHouse.jbHomeCheck_click_rentHouse()
    #     self.homeHouse.jbHomeCheck_click_price()
    #     self.homeHouse.jbHomeCheck_click_screenPrice()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_011(self):
    #     """房屋租售---发布资源(出租住宅)"""
    #     self.homeHouse.jbHomeCheck_click_publishHouse()
    #     self.homeHouse.jbHomeCheck_click_publish_screenHouse()
    #     # self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     # self.homeHouse.jbHomeCheck_click_leaseHouse_village()
    #     # self.homeHouse.jbHomeCheck_input_leaseHouse_village("顺江小区")
    #     # self.homeHouse.jbHomeCheck_click_leaseHouse_village_name()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
    #     self.operate.swipe_up()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_012(self):
    #     """房屋租售---发布资源(出租公寓)"""
    #     self.homeHouse.jbHomeCheck_click_publish_flats()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
    #     self.operate.swipe_up()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_013(self):
    #     """房屋租售---发布资源(出租写字楼)"""
    #     self.homeHouse.jbHomeCheck_click_publish_office()
    #     # self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
    #     self.operate.swipe_up()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_014(self):
    #     """房屋租售---发布资源(出租车位)"""
    #     self.homeHouse.jbHomeCheck_click_publish_parking()
    #     # self.homeHouse.jbHomeCheck_input_leaseHouse_title("测试")
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseParking_parking_type()
    #     self.homeHouse.jbHomeCheck_click_leaseParking_selectParking_type()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_015(self):
    #     """房屋租售---发布资源(出租商铺)"""
    #     self.homeHouse.jbHomeCheck_click_publish_shops()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(1)
    #     self.homeHouse.jbHomeCheck_click_leaseParking_floor_type()
    #     self.homeHouse.jbHomeCheck_click_leaseParking_selectFloor_type()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_016(self):
    #     """房屋租售---发布资源(出售住宅)"""
    #     self.homeHouse.jbHomeCheck_click_sell()
    #     self.homeHouse.jbHomeCheck_click_publish_screenHouse()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
    #     self.operate.swipe_up()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_017(self):
    #     """房屋租售---发布资源(出售公寓)"""
    #     self.homeHouse.jbHomeCheck_click_publish_flats()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
    #     self.operate.swipe_up()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_018(self):
    #     """房屋租售---发布资源(出售写字楼)"""
    #     self.homeHouse.jbHomeCheck_click_publish_office()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_renovation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_apartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectApartment()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_orientation()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectOrientation()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(10)
    #     self.operate.swipe_up()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floor(1)
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_floorAll(10)
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_019(self):
    #     """房屋租售---发布资源(出售车位)"""
    #     self.homeHouse.jbHomeCheck_click_publish_parking()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_click_leaseParking_parking_type()
    #     self.homeHouse.jbHomeCheck_click_leaseParking_selectParking_type()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_020(self):
    #     """房屋租售---发布资源(出售商铺)"""
    #     self.homeHouse.jbHomeCheck_click_publish_shops()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_price(100000)
    #     self.homeHouse.JbHomeCheck_click_leaseHouse_province_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_province()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_city()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_area()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_pay()
    #     self.homeHouse.jbHomeCheck_click_leaseHouse_selectPay()
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_built("2019")
    #     self.homeHouse.jbHomeCheck_input_leaseHouse_area(1)
    #     self.homeHouse.jbHomeCheck_click_leaseParking_floor_type()
    #     self.homeHouse.jbHomeCheck_click_leaseParking_selectFloor_type()
    #     for i in range(2):
    #         self.operate.get_back()
    #
    # def test_l_homeHouse_021(self):
    #     """房屋租售---品质新盘"""
    #     self.homeHouse.jbHomeCheck_click_pzxx()
    #     self.homeHouse.jbHomeCheck_click_price()
    #     self.homeHouse.jbHomeCheck_click_screenPrice()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_022(self):
    #     """房屋租售---投资首选"""
    #     self.homeHouse.jbHomeCheck_click_tzsx()
    #     self.homeHouse.jbHomeCheck_click_price()
    #     self.homeHouse.jbHomeCheck_click_screenPrice()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_023(self):
    #     """房屋租售---精选车位"""
    #     self.homeHouse.jbHomeCheck_click_jxcw()
    #     self.homeHouse.jbHomeCheck_click_price()
    #     self.homeHouse.jbHomeCheck_click_screenPrice()
    #     self.operate.get_back()
    #
    # def test_l_homeHouse_024(self):
    #     """房屋租售---增值服务"""
    #     self.homeHouse.jbHomeCheck_click_zzfw()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #
    # def test_m_homeParcel001(self):
    #     """我的包邮---进入包邮"""
    #     self.homeParcel.jbHomeParcel_click_parcel()
    #     self.homeParcel.get_switch_h5()
    #     time.sleep(2)
    #     self.operate.get_back()
    #     self.homeCheckIn.get_switch_android()
    #
    # def test_n_homePeriphery001(self):
    #     """周边商圈---进入周边商圈"""
    #     self.operate.swipe_up()
    #     self.homePeriphery.jbHomePeriphery_click_periphery()
    #     self.operate.get_back()
    # #     self.homePeriphery.get_switch_h5()
    # #
    # # def test_n_homePeriphery002(self):
    # #     """周边商圈---生活服务"""
    # #     self.homePeriphery.jbHomePeriphery_click_service()
    # #     self.homePeriphery.jbHomePeriphery_click_service_product()
    # #     time.sleep(1)
    # #     self.operate.get_back()
    # #
    # # def test_n_homePeriphery003(self):
    # #     """周边商圈---餐饮美食"""
    # #     self.homePeriphery.jbHomePeriphery_click_food()
    # #     self.homePeriphery.jbHomePeriphery_click_food_product()
    # #     time.sleep(1)
    # #     self.operate.get_back()
    # #
    # # def test_n_homePeriphery004(self):
    # #     """周边商圈---休闲娱乐"""
    # #     self.homePeriphery.jbHomePeriphery_click_entertainment()
    # #     self.homePeriphery.jbHomePeriphery_click_entertainment_product()
    # #     time.sleep(1)
    # #     self.operate.get_back()
    # #
    # # def test_n_homePeriphery005(self):
    # #     """周边商圈---教育培训"""
    # #     self.homePeriphery.jbHomePeriphery_click_education()
    # #     self.homePeriphery.jbHomePeriphery_click_education_product()
    # #     time.sleep(1)
    # #     self.operate.get_back()
    # #     self.operate.get_back()
    # #     self.homePeriphery.get_switch_android()
    #
    def test_o_shop_001(self):
        """商城---切换到商城"""
        self.home.home_click_shopping()
        self.shop.get_switch_h5()
        self.shop.get_switch_android()

    def test_p_jiaDou001(self):
        """嘉豆---进入嘉豆"""
        self.home.home_click_me()
        self.jiaDou.jbJiaDou_click_jiaDou()
        time.sleep(1)
        self.assertEquals(self.loginYaml['assert_jiaDou'],self.jiaDou.jbJiaDou_assert_jiaDou(),msg="")

    def test_p_jiaDou002(self):
        """嘉豆---赠送嘉豆"""
        self.jiaDou.jbJiaDou_click_give()
        time.sleep(1)
        self.assertEquals(self.loginYaml['assert_give'],self.jiaDou.jbJiaDou_assert_give(),msg="")
        self.jiaDou.jbJia_input_giveNum(100)
        self.jiaDou.jbJiaDou_input_giveNumber("13683450124")
        self.jiaDou.jbJiaDou_click_confirm()
        self.jiaDou.jbJiaDou_input_password("123456")
        self.jiaDou.jbJiaDou_click_button()
        self.jiaDou.jbJiaDou_click_complete()

    def test_p_jiaDou003(self):
        """嘉豆---修改密码"""
        self.jiaDou.jbJiaDou_click_alterPwd()
        # self.assertEquals(u"修改密码",self.jiaDou.jbJiaDou_assert_alterPwd(),msg="")
        self.jiaDou.jbJiaDou_click_alterPwd_confirm()
        for i in range(2):
            self.operate.get_back()

    def test_q_coupon001(self):
        """优惠券---查看"""
        self.coupon.jbCoupon_click_coupon()
        self.coupon.get_switch_h5()
        # self.coupon.jbCoupon_click_overdue()
        # time.sleep(1)
        # self.coupon.jbCoupon_click_receive()
        # time.sleep(1)
        self.operate.get_back()
        self.orders.get_switch_android()

    def test_r_setting_001(self):
        """我的资料---修改资料"""
        self.setting.jbSetting_click_head()
        self.assertEquals(self.loginYaml['assert_head'],self.setting.jbSetting_assert_head(),msg="")
        self.setting.jbSetting_click_edit()
        self.setting.jbSetting_click_preservation()

    def test_r_setting_002(self):
        """我的资料---取消更换项目"""
        self.setting.jbSetting_click_project_add()
        self.assertEquals(self.loginYaml['assert_project_add'],self.setting.jbSetting_assert_project_add(),msg="")
        self.setting.jbSetting_click_other_project_add()
        self.setting.jbSetting_click_cancel_project_add()

    def test_r_setting_003(self):
        """我的资料---切换项目成功"""
        other_project_add_name=self.setting.jbSetting_assert_other_project_add_name()
        self.setting.jbSetting_click_other_project_add()
        self.setting.jbSetting_click_switch_project_add()
        current_project_add_name=self.setting.jbSetting_assert_other_project_add_name()
        # self.assertEquals(other_project_add_name,current_project_add_name,msg="")

    def test_r_setting_004(self):
        """我的资料---再次切换项目"""
        self.setting.jbSetting_click_other_project_add()
        self.setting.jbSetting_click_switch_project_add()
        self.operate.get_back()

    def test_s_orders_001(self):
        """我的订单---待付款"""
        self.orders.jbOrders_click_payment()
        self.orders.get_switch_h5()
        self.operate.get_back()
        self.orders.get_switch_android()

    def test_s_orders_002(self):
        """我的订单---待发货"""
        self.orders.jbOrders_click_deliver_goods()
        self.orders.get_switch_h5()
        self.operate.get_back()
        self.orders.get_switch_android()

    def test_s_orders_003(self):
        """我的订单---待收货"""
        self.orders.jbOrders_click_receiving_goods()
        self.orders.get_switch_h5()
        self.operate.get_back()
        self.orders.get_switch_android()

    def test_s_orders_004(self):
        """我的订单---待评价"""
        self.orders.jbOrders_click_evaluate()
        self.orders.get_switch_h5()
        self.operate.get_back()
        self.orders.get_switch_android()

    def test_s_orders_005(self):
        """我的订单---售后服务"""
        self.orders.jbOrders_click_after_sale()
        self.orders.get_switch_h5()
        self.operate.get_back()
        self.orders.get_switch_android()

    # def test_s_orders_006(self):
    #     """我的订单---中奖纪录"""
    #     self.orders.jbOrders_click_winning_the_prize()
    #     # self.assertEquals(self.loginYaml['assert_winning_the_prize'],self.orders.jbOrders_assert_winning_the_prize(),msg="")
    #     self.operate.get_back()
    #
    # def test_s_orders_007(self):
    #     """我的订单---缴费记录"""
    #     self.orders.jbOrders_click_pay()
    #     self.assertEquals(self.loginYaml['assert_pay'],self.orders.jbOrders_assert_pay(),msg="")
    #     self.operate.get_back()
    #
    # def test_s_orders_008(self):
    #     """我的订单---我的活动"""
    #     self.orders.jbOrders_click_activity()
    #     self.assertEquals(self.loginYaml['assert_activity'],self.orders.jbOrders_assert_activity(),msg="")
    #     self.operate.get_back()
    #
    # def test_s_orders_009(self):
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
    # def test_s_orders_010(self):
    #     """我的订单---我的房源"""
    #     self.orders.jbOrders_click_housing_resources()
    #     self.assertEquals(self.loginYaml['assert_housing_resources'],self.orders.jbOrders_assert_housing_resources(),msg="")
    #     self.operate.get_back()
    #
    # def test_s_orders_011(self):
    #     """我的订单---我的发票(物业缴费)"""
    #     self.orders.jbOrders_click_invoice()
    #     self.assertEquals(self.loginYaml['assert_invoice'],self.orders.jbOrders_assert_invoice(),msg="")
    #     self.orders.jbOrders_click_wuye_pay()
    #     self.operate.get_back()
    #
    # def test_s_orders_012(self):
    #     """我的订单---我的发票（临停开票）"""
    #     self.orders.jbOrders_click_draw_bill()
    #     self.operate.get_back()
    #
    # def test_s_orders_013(self):
    #     """我的订单---我的发票（开票历史）"""
    #     self.orders.jbOrders_click_bill_history()
    #     self.operate.get_back()
    #     self.operate.get_back()
    #
    # def test_s_orders_014(self):
    #     """我的订单---商务合作"""
    #     self.orders.jbOrders_click_cooperation()
    #     self.orders.get_switch_h5()
    #     time.sleep(3)
    #     self.operate.get_back()
    #     self.orders.get_switch_android()

    def test_z_loginOut001(self):
        """个人设置---修改密码"""
        self.login.login_click_icon()
        self.setting.jbSetting_click_change_password()
        self.operate.get_back()

    def test_z_loginOut002(self):
        """个人设置---清除缓存"""
        self.setting.jbSetting_click_clear_cache()
        self.setting.jbSetting_click_sure_clear_cache()
        time.sleep(2)

    def test_z_loginOut003(self):
        """个人设置---切换智控模式"""
        self.setting.jbSetting_click_zhikong_pattern()
        self.setting.jbSetting_click_switch_zhikong_pattern()
        time.sleep(2)

    def test_z_loginOut004(self):
        """个人设置---切换摇一摇开门"""
        self.setting.jbSetting_click_shake()
        time.sleep(2)

    def test_z_loginOut005(self):
        """个人设置---切换通知声音"""
        self.setting.jbSetting_click_notification_voice()
        time.sleep(2)

    def test_z_loginOut006(self):
        """个人设置---切换通知震动"""
        self.setting.jbSetting_click_notification_vibration()
        time.sleep(2)

    def test_z_loginOut007(self):
        """个人设置---意见反馈"""
        self.setting.jbSetting_click_feedback()
        self.operate.get_back()
        time.sleep(2)


    def test_z_loginOut008(self):
        """个人设置---关于生活家"""
        self.setting.jbSetting_click_home()
        self.operate.get_back()
        time.sleep(2)

    def test_z_loginOut009(self):
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
    # suite = unittest.TestSuite()
    # suite.addTest(TestLoginCase('test_a_login_001'))
    # html_file = '../report/report_justbon.html'
    # fp = open(html_file, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title="嘉宝ui自动化测试报告",
    #     description="ui自动化"
    # )
    # runner.run(suite)
    # fp.close()
