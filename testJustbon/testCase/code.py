# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 16:03
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
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
        # PublicExcel("../config/locust.xls").write_excel()
    def setUp(self):
        pass

    def test_a_register_001(self):
        """注册---填写已经注册过的账号"""
        self.home.home_click_me()
        self.login.login_click_loginImmediately()


    def test_a_me_register_002(self):
        """注册---密码不符合要求"""

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


    def test_d_home_top_001(self):
        """首页---顶部项目切换"""


    def test_d_home_top_002(self):
        """首页---顶部项目切换回来"""

    def test_d_home_top_003(self):
        """首页---查看车辆限行"""
        pass

    def test_e_home_notice_001(self):
        """公告---查看全部公告列表"""

    def test_e_home_notice_002(self):
        """公告---查看新闻快报公告列表"""


    def test_e_home_notice_003(self):
        """公告---查看小嘉课堂公告列表"""


    def test_e_home_notice_004(self):
        """公告---查看温馨提示公告列表"""


    def test_e_home_notice_005(self):
        """公告---查看活动预告公告列表"""


    def test_e_home_notice_006(self):
        """公告---查看失物招领公告列表"""



    def test_e_home_notice_007(self):
        """公告---查看公告内容"""


    def test_f_home_housekeeper_001(self):
        """管家---查看管家团队成员"""

    def test_h_home_door_001(self):
        """一键开门---进入一键开门"""


    def test_i_home_guarantee_001(self):
        """嘉维修---查看我的订单(进行中)"""


    def test_i_home_guarantee_002(self):
        """嘉维修---查看我的订单(已完成)"""

    def test_i_home_guarantee_003(self):
        """嘉维修---公共维修提交工单失败(未选择预约时间)"""

    def test_i_home_guarantee_004(self):
        """嘉维修---公共维修提交工单失败(未填写内容)"""

    def test_i_home_guarantee_005(self):
        """嘉维修---公共维修提交工单"""

    def test_i_home_guarantee_006(self):
        """嘉维修---灯具线路提交工单"""

    def test_i_home_guarantee_007(self):
        """嘉维修---龙头管件提交工单"""

    def test_i_home_guarantee_008(self):
        """嘉维修---卫浴洁具提交工单"""

    def test_i_home_guarantee_009(self):
        """嘉维修---门窗家居提交工单"""

    def test_i_home_guarantee_010(self):
        """嘉维修---打孔疏通提交工单"""

    def test_i_home_guarantee_011(self):
        """嘉维修---大锁换锁提交工单"""

    def test_i_home_guarantee_012(self):
        """嘉维修---安防预约提交工单"""

    def test_j_home_complaint_001(self):
        """投诉---查看进行中数据"""

    def test_j_home_complaint_002(self):
        """投诉---查看已完成数据"""

    def test_j_home_complaint_003(self):
        """投诉---新增我要表扬工单"""


    def test_j_home_complaint_004(self):
        """投诉---新增我要投诉工单"""


    def test_k_home_visitor_001(self):
        """访客---新增访客"""


    def test_k_home_visitor_002(self):
        """访客---取消作废邀请码"""


    def test_k_home_visitor_003(self):
        """访客---确定作废邀请码"""


    def test_l_home_selected_001(self):
        """嘉宝精选---添加商品到购物车"""


    def test_m_home_water_001(self):
        """送水上门---一键购水"""


    def test_m_home_water_002(self):
        """送水上门---预约送水"""


    def test_m_home_water_003(self):
        """送水上门---个人中心---我的订单"""


    def test_m_home_water_004(self):
        """送水上门---个人中心---我的水票"""


    def test_m_home_water_005(self):
        """送水上门---个人中心---我的地址"""


    def test_m_home_water_006(self):
        """送水上门---个人中心---编辑我的地址"""


    def test_m_home_water_007(self):
        """送水上门---个人中心---我的押金"""


    def test_n_home_house_001(self):
        """房屋租售---查看我的房源"""

    def test_n_home_house_002(self):
        """房屋租售---查看我的车位"""


    def test_n_home_house_003(self):
        """房屋租售---查看我的商铺"""


    def test_n_home_house_004(self):
        """房屋租售---买新房"""


    def test_n_home_house_005(self):
        """房屋租售---二手房"""


    def test_n_home_house_006(self):
        """房屋租售---出租房"""


    def test_n_home_house_007(self):
        """房屋租售---发布出租(住宅)---发布成功"""



    def test_n_home_house_008(self):
        """房屋租售---发布出租(公寓)---发布成功"""

    def test_n_home_house_009(self):
        """房屋租售---发布出租(写字楼)---发布成功"""

    def test_n_home_house_010(self):
        """房屋租售---发布出租(车位)---发布成功"""

    def test_n_home_house_011(self):
        """房屋租售---发布出租(商铺)---发布成功"""

    def test_n_home_house_012(self):
        """房屋租售---发布出售(住宅)---发布成功"""

    def test_n_home_house_013(self):
        """房屋租售---发布出售(公寓)---发布成功"""

    def test_n_home_house_014(self):
        """房屋租售---发布出售(写字楼)---发布成功"""

    def test_n_home_house_015(self):
        """房屋租售---发布出售(车位)---发布成功"""

    def test_n_home_house_016(self):
        """房屋租售---发布出售(商铺)---发布成功"""

    def test_n_home_house_017(self):
        """房屋租售---发布出售(住宅)---发布成功"""

    def test_n_home_house_018(self):
        """房屋租售---帮我找(求租住宅)---发布成功"""

    def test_n_home_house_019(self):
        """房屋租售---帮我找(求租公寓)---发布成功"""

    def test_n_home_house_020(self):
        """房屋租售---帮我找(求租写字楼)---发布成功"""

    def test_n_home_house_021(self):
        """房屋租售---帮我找(求租车位)---发布成功"""

    def test_n_home_house_022(self):
        """房屋租售---帮我找(求租商铺)---发布成功"""

    def test_n_home_house_023(self):
        """房屋租售---帮我找(求售住宅)---发布成功"""

    def test_n_home_house_024(self):
        """房屋租售---帮我找(求售公寓)---发布成功"""

    def test_n_home_house_025(self):
        """房屋租售---帮我找(求售写字楼)---发布成功"""

    def test_n_home_house_026(self):
        """房屋租售---帮我找(求售车位)---发布成功"""

    def test_n_home_house_027(self):
        """房屋租售---帮我找(求售商铺)---发布成功"""

    def test_n_home_house_028(self):
        """房屋租售---品质新盘"""

    def test_n_home_house_029(self):
        """房屋租售---投资首选"""

    def test_n_home_house_030(self):
        """房屋租售---精选车位"""

    def test_n_home_house_031(self):
        """房屋租售---增值服务"""

    def test_n_home_house_032(self):
        """房屋租售---查看房源详情"""

    def test_o_home_checkIn_001(self):
        """拎包入住---进入拎包入住"""


    def test_o_home_checkIn_002(self):
        """拎包入住---热门活动"""


    def test_o_home_checkIn_003(self):
        """拎包入住---参观工地"""

    def test_o_home_checkIn_004(self):
        """拎包入住---装修管家"""


    def test_o_home_checkIn_005(self):
        """拎包入住---精品案例"""

    def test_o_home_checkIn_006(self):
        """拎包入住---旧房翻新"""


    def test_o_home_checkIn_007(self):
        """拎包入住---家具商城"""


    def test_o_home_checkIn_008(self):
        """拎包入住---选设计师"""


    def test_o_home_checkIn_009(self):
        """拎包入住---挑工厂"""


    def test_p_home_delicous_001(self):
        """美食汇---搜索店铺"""

    def test_p_home_delicous_002(self):
        """美食汇---我的收藏"""


    def test_p_home_delicous_003(self):
        """美食汇---就吃火锅"""


    def test_p_home_delicous_004(self):
        """美食汇---烤系列"""


    def test_p_home_delicous_005(self):
        """美食汇---撸个串"""

    def test_p_home_delicous_006(self):
        """美食汇---热卤小吃"""


    def test_p_home_delicous_007(self):
        """美食汇---抗疫专区"""


    def test_p_home_delicous_008(self):
        """美食汇---轻奢中餐"""


    def test_p_home_delicous_009(self):
        """美食汇---商务宴请"""


    def test_p_home_delicous_010(self):
        """美食汇---网红打卡"""


    def test_p_home_delicous_011(self):
        """美食汇---春季汤锅"""

    def test_p_home_delicous_012(self):
        """美食汇---全部分类"""


    def test_q_Intelligent_001(self):
        """智控---进入智控"""

    def test_r_shoppopping_001(self):
        """商城---切换到商城"""


    def test_s_neighbor_001(self):
        """邻里---业主论坛---查看第一个帖子"""


    def test_s_neighbor_002(self):
        """邻里---业主论坛---对帖子点赞和评论"""

    def test_s_neighbor_003(self):
        """邻里---业主论坛---发帖"""


    def test_s_neighbor_004(self):
        """邻里---社区活动---查看第一个活动"""


    def test_s_neighbor_005(self):
        """邻里---跳蚤市场---查看第一个帖子"""


    def test_s_neighbor_006(self):
        """邻里---跳蚤市场---发帖"""


    def test_t_jiaDou_001(self):
        """嘉豆---嘉豆列表"""

    def test_t_jiaDou_002(self):
        """嘉豆---赠送嘉豆"""


    def test_p_jiaDou_003(self):
        """嘉豆---修改密码"""


    def test_p_jiaDou_004(self):
        """嘉豆---使用规则"""


    def test_u_coupon_001(self):
        """优惠券---查看"""


    def test_v_setting_001(self):
        """设置---修改资料"""

    def test_v_setting_002(self):
        """设置---房屋解绑"""

    def test_v_setting_003(self):
        """设置---房屋绑定"""

    def test_w_orders_001(self):
        """我的订单---待付款"""


    def test_w_orders_002(self):
        """我的订单---待发货"""


    def test_w_orders_003(self):
        """我的订单---待收货"""


    def test_w_orders_004(self):
        """我的订单---待评价"""

    def test_w_orders_005(self):
        """我的订单---售后服务"""


    
    @classmethod
    def tearDownClass(cls):
        # PublicExcel("../report/locust.xls").write_excel(0,4,1,datetime.datetime.now())
        # start_time =
        pass

if __name__ == '__main__':
    unittest.main()






























































