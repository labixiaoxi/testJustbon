# -*-coding:utf-8 -*-
#__author__ = '廖磊'
# Time:2019/9/5 11:40
from selenium.webdriver.common.by import By
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
from config import getLoginElement as element
log = PublicLogs()

#升级提醒
class StaffUpgrade(BasePage):
        def upgrade_click_close(self):
            self.click("id=>com.justbon.oa:id/close")
            log.info("升级提醒---点击关闭按钮")

#嘉维修
class StaffRepairPage(BasePage):
        def sfRepair_click_repair(self):
            self.click('xpath=>//*[@resource-id="com.justbon.oa:id/rv_modules"]/android.widget.LinearLayout[9]')
            log.info(u"嘉维修---点击嘉维修")

        def sfRepair_assert_list(self):
            result = self.text("id=>com.justbon.oa:id/tv_title")
            log.info(u"嘉维修---断言内容---进入嘉维修页面成功")
            return result

        def sfRepair_assert_add(self):
            result = self.text("id=>com.justbon.oa:id/tv_title")
            log.info(u"嘉维修---断言内容---新增需求提报页面成功")
            return result

        def sfRepair_click_add(self):
            self.click("id=>com.justbon.oa:id/tv_ok")
            log.info(u"发现订单---新增")

        def sfRepair_click_details(self):
            self.click('xpath=>//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout')
            log.info(u"发现订单---列表详情")

        def sfRepair_assert_find_details(self):
            result = self.text("id=>com.justbon.oa:id/tv_title")
            log.info(u"嘉维修---断言内容---发现列表进入详情页面成功")
            return result

        def sfRepair_click_myorder_jxz(self):
            self.click('xpath=>//*[@resource-id="android:id/tabs"]/android.widget.LinearLayout[2]')
            log.info(u"我的订单---进行中")

        def sfRepair_click_orderdetails(self):

            self.click("id=>com.justbon.oa:id/tv_service_type")
            log.info(u"我的订单---详情")

        def sfRepair_assert_details(self):
            result = self.text("id=>com.justbon.oa:id/tv_title")
            log.info(u"嘉维修---断言内容---我的订单列表进入详情页面成功")
            return result

        def sfRepair_click_myorder_ywc(self):
            self.click("id=>com.justbon.oa:id/detail_totask_count_value2")
            log.info(u"我的订单---已完成")

        def sfRepair_click_myorder_yqx(self):
            self.click("id=>com.justbon.oa:id/detail_ovtask_count_value2")
            log.info(u"我的订单---已取消")

        def sfRepair_click_center(self):
            self.click('xpath=>//*[@resource-id="android:id/tabs"]/android.widget.LinearLayout[3]')
            log.info(u"嘉维修---个人中心")

        def sfRepair_assert_center(self):
            result = self.text("id=>com.justbon.oa:id/tv_title")
            log.info(u"嘉维修---断言内容---进入个人中心成功")
            return result

        def sfRepair_click_area(self):
            self.click("id=>com.justbon.oa:id/ll_service_area")
            log.info(u"个人中心---接单区域")

        def sfRepair_assert_area(self):
            result = self.text("id=>com.justbon.oa:id/tv_title")
            log.info(u"嘉维修---断言内容---接单区域列表进入详情成功")
            return result

        def sfRepair_click_servicetype(self):
            self.click("id=>com.justbon.oa:id/ll_service_type")
            log.info(u"个人中心---服务类型")

        def sfRepair_click_myaccount(self):
            self.click("id=>com.justbon.oa:id/ll_account")
            log.info(u"个人中心---我的账户")

#员工APP首页
class StaffHomemenuPage(BasePage):
      def sfhomemenu_click_open(self):
          self.click("id=>com.justbon.oa:id/rl_module_more")
          log.info("首页---展开功能菜单")

      def sfhomemenu_click_mine(self):
          self.click("id=>com.justbon.oa:id/fl_layout_mime")
          log.info("首页---我的")

      def sfhomemenu_click_exit(self):
          self.click("id=>com.justbon.oa:id/tv_exit")
          log.info("我的---退出登录")

      def sfhomemenu_click_exit_toast(self):
          self.click("id=>com.justbon.oa:id/right_button")
          log.info("我的---退出登录---确定")

#智能巡检
class StaffInspectionPage(BasePage):
      def sfInspection_click_list(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/rv_modules"]/android.widget.LinearLayout[4]')
          log.info("首页---智能巡检")

      def sfInspection_assert_list(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info(u"智能巡检---断言内容---进入智能巡检列表成功")
          return result

      def sfInspection_click_more(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.support.v7.widget.LinearLayoutCompat')
          log.info("智能巡检---更多")

      def sfInspection_click_sign(self):
          self.click("id=>com.justbon.oa:id/title")
          log.info("智能巡检---签到")

      def sfInspection_assert_sign(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入签到页面成功")
          return result

      def sfInspection_click_signlocation(self):
          self.click("id=>com.justbon.oa:id/btn_place")
          log.info("智能巡检---选择位置")

      def sfInspection_click_organization(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/org_list"]/android.widget.TextView')
          log.info("智能巡检---选择组织")

      def sfInspection_assert_organization(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入选择组织页面成功")
          return result

      def sfInspection_click_submit(self):
          self.click("id=>com.justbon.oa:id/toolbar_text_btn")
          log.info("智能巡检---提交")

      def sfInspection_click_confirm_checkin(self):
          self.click("id=>com.justbon.oa:id/btn_check_in")
          log.info("智能巡检---上班签到")

      def sfInspection_click_confirm(self):
          self.click("id=>android:id/button2")
          log.info("智能巡检---确定")

      def sfInspection_assert_confirm(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---签到成功")
          return result

      def sfInspection_click_scene(self):
          self.click("id=>com.justbon.oa:id/btn_scene")
          log.info("智能巡检---现场报警")

      def sfInspection_assert_secne(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入现场报警页面成功")
          return result

      def sfInspection_click_repair(self):
          self.click("id=>com.justbon.oa:id/btn_repair")
          log.info("智能巡检---维修报警")

      def sfInspection_assert_repair(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入维修报警页面成功")
          return result

      def sfInspection_click_equipment(self):
          self.click("id=>com.justbon.oa:id/btn_equipment")
          log.info("智能巡检---设备报警")

      def sfInspection_assert_equipment(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入设备报警页面成功")
          return result

      def sfInspection_click_todo_task(self):
          self.click("id=>com.justbon.oa:id/btn_todo")
          log.info("智能巡检---待办任务")

      def sfInspection_assert_todo_task(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入待办事项页面成功")
          return result

      def sfInspection_click_offline(self):
          self.click("id=>com.justbon.oa:id/toolbar_text_btn")
          log.info("智能巡检---待办任务---离线")

      def sfInspection_assert_offline(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入待办事项离线页面成功")
          return result

      def sfInspection_click_start_work(self):
          self.click("id=>com.justbon.oa:id/btn_start_work")
          log.info("智能巡检---发现问题")

      def sfInspection_assert_start_work(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入发现问题页面成功")
          return result

      def sfInspection_click_start_repair(self):
          self.click("id=>com.justbon.oa:id/toolbar_text_btn")
          log.info("智能巡检----发现问题---报修")

      def sfInspection_click_switch_problem(self):
          self.click("id=>com.justbon.oa:id/rb_02")
          log.info("智能巡检---发现问题---切换状态")

      def sfInspection_click_photograph(self):
          self.click("id=>com.justbon.oa:id/image_view")
          log.info("智能巡检---发现问题----拍照toast")

      def sfInspection_click_photopage(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/select_dialog_listview"]/android.widget.TextView[1]')
          log.info("智能巡检---发现问题---拍照首页")

      def sfInspection_click_photo(self):
          self.click("id=>com.huawei.camera:id/shutter_button")
          log.info("智能巡检---发现问题---拍照")

      def sfInspection_click_photo_confirm(self):
          self.click("id=>com.huawei.camera:id/btn_done")
          log.info("智能巡检---发现问题---确认拍照")

      def sfInspection_click_statistics(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/tools_list"]/android.widget.RelativeLayout[1]')
          log.info("智能巡检---数据统计")

      def sfInspection_assert_statistics(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入数据统计页面成功")
          return result

      def sfInspection_click_myrecord(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/tools_list"]/android.widget.RelativeLayout[2]')
          log.info("智能巡检---我的记录")

      def sfInspection_assert_myrecord(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入我的记录页面成功")
          return result

      def sfInspection_click_notice(self):
          self.click("id=>com.justbon.oa:id/btn_more")
          log.info("智能巡检---最新通知")

      def sfInspection_assert_notice(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入最新通知页面成功")
          return result

      def sfInspection_click_patrol(self):
          ele_list = self.driver.find_elements_by_id("com.justbon.oa:id/title")
          ele_list[1].click()
          log.info("智能巡检---巡更")

      def sfInspection_click_start_inspection(self):
          self.click("id=>com.justbon.oa:id/btn_start")
          log.info("智能巡检---开始巡检")

      def sfInspection_assert_start_inspection(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入巡检页面成功")
          return result

      def sfInspection_click_dot(self):
          self.click("id=>com.justbon.oa:id/btn_start_inspecting")
          log.info("智能巡检---打点")

      def sfInspection_assert_patrol(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入巡更页面成功")
          return result

      def sfInspection_click_signback(self):
          self.click("id=>com.justbon.oa:id/btn_check_in")
          log.info("智能巡检---下班签退")

      def sfInspection_assert_signback(self):
          result = self.text("id=>sfInspection_click_signback")
          log.info("智能巡检---断言内容---下班签退成功")
          return result

      def sfInspection_click_loop(self):
          self.click("id=>com.justbon.oa:id/main_tab_record")
          log.info("智能巡检---巡航")

      def sfInspection_assert_click_loop(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入巡航菜单页面成功")
          return result

      def sfInspection_click_conversation(self):
          self.click("id=>com.justbon.oa:id/main_tab_customer")
          log.info("智能巡检---会话")

      def sfInspection_assert_conversation(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入会话菜单页面成功")
          return result

      def sfInspection_click_mine(self):
          self.click("id=>com.justbon.oa:id/main_tab_mine")
          log.info("智能巡检---我的")

      def sfInspection_assert_mine(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入我的页面成功")
          return result

      def sfInspection_click_guide(self):
          self.click("id=>com.justbon.oa:id/guide")
          log.info("智能巡检---操作指引")

      def sfInspection_click_standard(self):
          self.click("id=>com.justbon.oa:id/standard")
          log.info("智能巡检---公司标准")

      def sfInspection_assert_standard(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入我的公司标准列表页面成功")
          return result

      def sfInspection_click_standard_list(self):
          self.click('xpath=>//*[@resource-id="form1"]/android.view.MenuItem')
          log.info("智能巡检---公司标准---列表")

      def sfInspection_click_feedback(self):
          self.click("id=>com.justbon.oa:id/feedback")
          log.info("智能巡检---反馈")

      def sfInspection_assert_feedback(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入问题反馈列表页面成功")
          return result

      def sfInspection_click_setting(self):
          self.click("id=>com.justbon.oa:id/setting")
          log.info("智能巡检---设置")

      def sfInspection_assert_setting(self):
          result = self.text('xpath=>//*[@resource-id="com.justbon.oa:id/toolbar"]/android.widget.TextView')
          log.info("智能巡检---断言内容---进入设置列表页面成功")
          return result

      def sfInspection_click_tab_work(self):
          self.click("id=>com.justbon.oa:id/main_tab_work")
          log.info("智能巡检---列表首页")

      def sfInspection_assert_back(self):
          result = self.text("id=>android:id/message")
          log.info("智能巡检---断言内容---下班签退成功")
          return result

#房屋经纪
class StaffHouseBroker(BasePage):
      def sfHouse_click_house(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/rv_modules"]/android.widget.LinearLayout[8]')
          log.info("首页---房屋经纪")

      def sfHouse_assert_order(self):
          result = self.text("id=>com.justbon.oa:id/tv_title")
          log.info("房屋经纪---断言内容---进入我要抢单页面成功")
          return result

      def sfHouse_click_resource(self):
          self.click("id=>com.justbon.oa:id/rb_house")
          log.info("房屋经纪---我的资源")

      def sfHouse_assert_resource(self):
          result = self.text("id=>com.justbon.oa:id/tv_title")
          log.info("房屋经纪---断言内容---进入我的资源页面成功")
          return result

      def sfHouse_click_release(self):
          self.click("id=>com.justbon.oa:id/rb_customer")
          log.info("房屋经纪---我要发布")

      def sfHouse_assert_release(self):
          result = self.text("id=>com.justbon.oa:id/tv_title")
          log.info("房屋经纪---断言内容---进入我的发布页面成功")
          return result

      def sfHouse_click_type(self):
          self.click("id=>com.justbon.oa:id/rl_residential")
          log.info("房屋经纪---选择发布类型")

      def sfHouse_click_statistics(self):
          self.click("id=>com.justbon.oa:id/rb_statistics")
          log.info("房屋经纪---我的统计")

      def sfHouse_assert_statistics(self):
          result = self.text("id=>com.justbon.oa:id/btn_query")
          log.info("房屋经纪---断言---进入我的统计页面成功")
          return result

      def sfhouse_click_apartment(self):
          self.click("id=>com.justbon.oa:id/rb_apartment")
          log.info("房屋经纪---我的统计---公寓")

      def sfhouse_click_office(self):
          self.click("id=>com.justbon.oa:id/rb_office")
          log.info("房屋经纪---我的统计---写字楼")

#在线学习
class StaffOnlineLearne(BasePage):
      def sflearne_click_homepage(self):
          self.click('xpath=>//*[@resource-id="com.justbon.oa:id/rv_modules"]/android.widget.LinearLayout[1]')
          log.info("首页---在线学习")

      def sflearne_assert_homepage(self):
          result = self.text("id=>com.justbon.oa:id/tv_title")
          log.info("在线学习---断言---进入首页成功")
          return result



#点击图标展开
#sfHouse_click_house = driver.find_elements_by_id('com.justbon.oa:id/tv_module_name')
# for name in names:
#     name_list.append(name.text)
# for i in range(len(name_list)):
#     if name_list[i]=="房屋经纪":
#         driver.find_element_by_xpath('xpath=>//*[@resource-id="com.justbon.oa:id/rv_modules"]/android.widget.LinearLayout[%s]/android.widget.TextView'%(i+1))







