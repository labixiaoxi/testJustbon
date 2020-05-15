# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 16:03
import warnings
import unittest, time, HTMLTestRunner, datetime
from public.publicDriver import publicDrivers
from public.publicYaml import PublicGetYaml
from public.publicExcel import PublicExcel
from public.publicOperate import PublicOperate
# from public import publicSql
from public.publicPhone import PublicPhone
from pageObject.staffLoginPage import StaffLoginPage
from pageObject.staffRepairPage import *
from ddt import ddt, data, unpack

@ddt
class TestLoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = publicDrivers()
        cls.login = StaffLoginPage(cls.driver)
        cls.upgrade = StaffUpgrade(cls.driver)
        cls.reparis = StaffRepairPage(cls.driver)
        cls.homemenu = StaffHomemenuPage(cls.driver)
        cls.inspection = StaffInspectionPage(cls.driver)
        cls.operat = PublicOperate(cls.driver)
        cls.house = StaffHouseBroker(cls.driver)
        cls.learne = StaffOnlineLearne(cls.driver)

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    @data(["liaolei1","hhz666."])
    @unpack
    def test_a_login001(self,username,password):
        """登录"""
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.click_login()
        time.sleep(3)

    # def test_a_login002(self):
    #     """升级提醒---关闭"""
    #     try:
    #        self.upgrade.upgrade_click_close()
    #     except:
    #        pass






    #
    # def test_b_repair001(self):
    #     """嘉维修---查看嘉维修"""
    #     self.homemenu.sfhomemenu_click_open()
    #     self.reparis.sfRepair_click_repair()
    #     time.sleep(2)
    #     self.assertEqual("发现订单",self.reparis.sfRepair_assert_list())
    #
    # def test_b_repair002(self):
    #     """嘉维修---新增"""
    #     self.reparis.sfRepair_click_add()
    #     self.assertEqual("需求提报",self.reparis.sfRepair_assert_add())
    #     self.operat.swipe_up()
    #     self.operat.get_back()
    #
    # def test_b_repairs003(self):
    #     """嘉维修---列表滑动跳转详情"""
    #     try:
    #         self.reparis.sfRepair_click_details()
    #         self.assertEqual("发现订单", self.reparis.sfRepair_assert_find_details())
    #         self.operat.swipe_up()
    #         self.operat.swipe_up()
    #         self.operat.swipe_up()
    #         self.operat.swipe_down()
    #         self.operat.get_back()
    #     except:
    #         pass
    #
    # def test_b_repairs004(self):
    #     """嘉维修---我的订单（进行中）"""
    #     self.reparis.sfRepair_click_myorder_jxz()
    #
    # def test_b_repairs005(self):
    #     """嘉维修---我的订单（进行中）详情"""
    #     try:
    #         self.reparis.sfRepair_click_orderdetails()
    #         self.assertEqual("我的订单", self.reparis.sfRepair_assert_details())
    #         self.operat.get_back()
    #     except:
    #         pass
    #
    # def test_b_repairs006(self):
    #     """嘉维修---我的订单（已完成）"""
    #     self.reparis.sfRepair_click_myorder_ywc()
    #
    # def test_b_repairs007(self):
    #     """嘉维修---我的订单（已完成）详情"""
    #     try:
    #         self.reparis.sfRepair_click_orderdetails()
    #         self.assertEqual("我的订单", self.reparis.sfRepair_assert_details())
    #         self.operat.get_back()
    #     except:
    #         pass
    #
    # def test_b_repairs008(self):
    #     """嘉维修---我的订单（已取消）"""
    #     self.reparis.sfRepair_click_myorder_yqx()
    #
    # def test_b_repairs009(self):
    #     """嘉维修---我的订单（已取消）详情"""
    #     try:
    #         self.reparis.sfRepair_click_orderdetails()
    #         self.assertEqual("我的订单", self.reparis.sfRepair_assert_details())
    #         self.operat.get_back()
    #     except:
    #         pass

    # def test_b_repairs010(self):
    #     """"嘉维修---个人中心"""
    #     self.reparis.sfRepair_click_center()
    #     self.assertEqual("个人中心",self.reparis.sfRepair_assert_center())
    #
    # def test_b_repairs011(self):
    #     """个人中心---接单区域"""
    #     self.reparis.sfRepair_click_area()
    #     self.assertEqual("选择接单区域",self.reparis.sfRepair_assert_area())
    #     self.operat.get_back()
    #
    # def test_b_repairs012(self):
    #     """个人中心---服务类型"""
    #     self.reparis.sfRepair_click_servicetype()
    #     self.operat.get_back()
    #
    # def test_b_repairs013(self):
    #     """个人中心---我的账户"""
    #     self.reparis.sfRepair_click_myaccount()
    #     self.operat.get_back()
    #     self.operat.get_back()

    # def test_c_homemenu01(self):
    #     """首页---展开功能菜单"""
    #     self.homemenu.sfhomemenu_click_open()
    #
    # def test_d_inspection01(self):
    #     """智能巡检---首页"""
    #     self.inspection.sfInspection_click_list()
    #     self.assertEqual("工作",self.inspection.sfInspection_assert_list())
    #     time.sleep(2)
    #
    # def test_d_inspection02(self):
    #     """智能巡检---更多"""
    #     self.inspection.sfInspection_click_more()
    #
    # def test_d_inspection03(self):
    #     """智能巡检---签到"""
    #     self.inspection.sfInspection_click_sign()
    #     self.assertEqual("签到",self.inspection.sfInspection_assert_sign())
    #
    # def test_d_inspection04(self):
    #     """智能巡检---选择签到位置"""
    #     self.inspection.sfInspection_click_signlocation()
    #     self.assertEqual("选择组织",self.inspection.sfInspection_assert_organization())
    #
    # def test_d_inspection05(self):
    #     """智能巡检---选择组织"""
    #     self.inspection.sfInspection_click_organization()
    #     time.sleep(1)
    #     self.inspection.sfInspection_click_organization()
    #     time.sleep(1)
    #     self.inspection.sfInspection_click_organization()
    #     time.sleep(1)
    #     self.inspection.sfInspection_click_organization()
    #     time.sleep(1)
    #     self.inspection.sfInspection_click_organization()
    #
    # def test_d_inspection06(self):
    #     """智能巡检---提交"""
    #     self.inspection.sfInspection_click_submit()
    #
    # def test_d_inspection07(self):
    #     """智能巡检---上班签到"""
    #     self.inspection.sfInspection_click_confirm_checkin()
    #
    # def test_d_inspection08(self):
    #     """智能巡检---确认签到"""
    #     self.inspection.sfInspection_click_confirm()
    #     self.assertEqual("任务池", self.inspection.sfInspection_assert_confirm())
    #     time.sleep(2)
    #
    # def test_d_inspection09(self):
    #     """智能巡检---任务列表"""
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.get_back()
    #
    # def test_d_inspection10(self):
    #     """智能巡检---现场报警"""
    #     self.inspection.sfInspection_click_scene()
    #     self.assertEqual("现场报警",self.inspection.sfInspection_assert_secne())
    #     self.operat.get_back()
    #
    # def test_d_inspection11(self):
    #     """智能巡检---维修报警"""
    #     self.inspection.sfInspection_click_repair()
    #     self.assertEqual("维修报警",self.inspection.sfInspection_assert_repair())
    #     self.operat.get_back()
    #
    # def test_d_inspection12(self):
    #     """智能巡检---设备报警"""
    #     self.inspection.sfInspection_click_equipment()
    #     self.assertEqual("设备报警",self.inspection.sfInspection_assert_equipment())
    #     self.operat.get_back()
    #
    # def test_d_inspection13(self):
    #     """智能巡检---待办任务"""
    #     self.inspection.sfInspection_click_todo_task()
    #     self.assertEqual("待办事项",self.inspection.sfInspection_assert_todo_task())
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #
    # def test_d_inspection14(self):
    #     """智能巡检---待办任务---离线"""
    #     self.inspection.sfInspection_click_offline()
    #     self.assertEqual("离线上传",self.inspection.sfInspection_assert_offline())
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.get_back()
    #     self.operat.get_back()
    #
    # def test_d_inspection15(self):
    #     """智能巡检---发现问题"""
    #     self.inspection.sfInspection_click_start_work()
    #     self.assertEqual("开始巡查",self.inspection.sfInspection_assert_start_work())
    #
    # def test_d_inspection16(self):
    #     """智能巡检---发现问题---报修"""
    #     self.inspection.sfInspection_click_start_repair()
    #     time.sleep(1)
    #     self.operat.get_back()
    #
    # def test_d_inspection17(self):
    #     """智能巡检---发现问题---选择状态"""
    #     self.inspection.sfInspection_click_switch_problem()
    #
    # def test_d_inspection22(self):
    #     """智能巡检---数据统计"""
    #     self.inspection.sfInspection_click_statistics()
    #     self.assertEqual("数据统计",self.inspection.sfInspection_assert_statistics())
    #     time.sleep(5)
    #     self.operat.get_back()
    #
    # def test_d_inspection23(self):
    #     """智能巡检---我的记录"""
    #     self.inspection.sfInspection_click_myrecord()
    #     self.assertEqual("我的记录",self.inspection.sfInspection_assert_myrecord())
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.get_back()
    #
    # def test_d_inspection24(self):
    #     """智能巡检---最新通知"""
    #     self.inspection.sfInspection_click_notice()
    #     self.assertEqual("通知",self.inspection.sfInspection_assert_notice())
    #     self.operat.get_back()
    #
    # def test_d_inspection25(self):
    #     """智能巡检---巡更"""
    #     self.inspection.sfInspection_click_more()
    #     self.inspection.sfInspection_click_patrol()
    #     self.assertEqual("巡检任务", self.inspection.sfInspection_assert_patrol())
    #     self.operat.get_back()
    #
    # def test_d_inspection26(self):
    #     """智能巡检---巡航"""
    #     time.sleep(1)
    #     self.inspection.sfInspection_click_loop()
    #     self.assertEqual("搜索",self.inspection.sfInspection_assert_click_loop())
    #
    # def test_d_inspection27(self):
    #     """智能巡检---会话"""
    #     self.inspection.sfInspection_click_conversation()
    #     self.assertEqual("会话",self.inspection.sfInspection_assert_conversation())
    #
    # def test_d_inspection28(self):
    #     """智能巡检---我的"""
    #     self.inspection.sfInspection_click_mine()
    #     self.assertEqual("我",self.inspection.sfInspection_assert_mine())
    #
    # def test_d_inspection29(self):
    #     """智能巡检---我的---操作指引"""
    #     self.inspection.sfInspection_click_guide()
    #     time.sleep(4)
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.get_back()
    #
    # def test_d_inspection30(self):
    #     """智能巡检---我的---公司标准"""
    #     self.inspection.sfInspection_click_standard()
    #     self.assertEqual("公司标准",self.inspection.sfInspection_assert_standard())
    #     time.sleep(2)
    #     self.inspection.sfInspection_click_standard_list()
    #     self.operat.get_back()
    #     self.operat.get_back()
    #
    # def test_d_inspection31(self):
    #     """智能巡检---我的---反馈"""
    #     self.inspection.sfInspection_click_feedback()
    #     self.assertEqual("问题反馈",self.inspection.sfInspection_assert_feedback())
    #     self.operat.get_back()
    #
    # def test_d_inspection32(self):
    #     """智能巡检---我的---设置"""
    #     self.inspection.sfInspection_click_setting()
    #     self.assertEqual("设置",self.inspection.sfInspection_assert_setting())
    #     self.operat.get_back()
    #
    # def test_d_inspection33(self):
    #     """智能巡检---列表首页"""
    #     self.inspection.sfInspection_click_tab_work()
    #
    # def test_d_inspection34(self):
    #     """智能巡检---下班签退"""
    #     self.inspection.sfInspection_click_more()
    #     self.inspection.sfInspection_click_sign()
    #     self.inspection.sfInspection_click_signback()
    #     self.assertEqual("下班签退成功！",self.inspection.sfInspection_assert_back())
    #     self.inspection.sfInspection_click_confirm()
    #     self.operat.get_back()
    #     self.operat.get_back()

    #
    # def test_e_house01(self):
    #    """首页---展开功能菜单"""
    #    self.homemenu.sfhomemenu_click_open()
    #
    # def test_e_house02(self):
    #     """房屋经纪---我要抢单"""
    #     self.house.sfHouse_click_house()
    #     self.assertEqual("房屋经纪",self.house.sfHouse_assert_order())
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #
    # def test_e_house03(self):
    #     """房屋经纪---我的资源"""
    #     self.house.sfHouse_click_resource()
    #     self.assertEqual("房屋经纪",self.house.sfHouse_assert_resource())
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #     self.operat.swipe_left()
    #
    # def test_e_house04(self):
    #     """房屋经纪---我要发布"""
    #     self.house.sfHouse_click_release()
    #     self.assertEqual("房屋经纪",self.house.sfHouse_assert_release())
    #     self.house.sfHouse_click_type()
    #     self.operat.swipe_up()
    #     self.operat.get_back()
    #
    # def test_e_house05(self):
    #     """房屋经纪---我的统计"""
    #     self.house.sfHouse_click_statistics()
    #     self.assertEqual("查询",self.house.sfHouse_assert_statistics())
    #     self.house.sfhouse_click_apartment()
    #     self.house.sfhouse_click_office()
    #     self.operat.swipe_up()
    #     time.sleep(1)
    #     self.operat.get_back()
    #
    # def test_f_learne01(self):
    #     """在线学习---首页"""
    #     self.learne.sflearne_click_homepage()
    #     self.assertEqual("在线学习",self.learne.sflearne_assert_homepage())
    #     time.sleep(3)
    #     self.operat.get_back()

    # def test_z_homemenu01(self):
    #     """员工生活家首页----我的"""
    #     self.homemenu.sfhomemenu_click_mine()
    #     self.homemenu.sfhomemenu_click_exit()
    #     self.homemenu.sfhomemenu_click_exit_toast()
    #     self.operat.get_back()


if __name__ == '__main__':
    unittest.main()