# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 15:17
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
from config import getLoginElement as element
import time
log = PublicLogs()

#登录
class JbLoginPage(BasePage):
    """
    登录数据
    """
    click_register_loc = ''

    #密码
    def login_input_password(self,password):
        self.send_keys(element.password_loc,password)
        log.info(u"登录页面---输入登录密码:%s"%(password))

    #立即登录
    def login_click_loginImmediately(self):
        self.click(element.loginImmediately_loc)
        log.info(u"我的页面---点击立即登录")

    #账号
    def login_input_username(self,username):
        self.send_keys(element.username_loc,username)
        log.info(u"登录页面---输入登录账号:%s"%(username))

    #登录
    def login_click_login(self):
        self.click(element.login_loc)
        log.info(u"登录页面---点击登录按钮")

    # 判断内容-登录
    def login_assert_login(self):
        result = self.text(element.assert_login_loc)
        log.info(u"登录页面---断言内容---进入登录页面成功")
        return result

    #立即登录
    def login_assert_loginImmediately(self):
        result = self.text(element.assert_loginImmediately_loc)
        log.info(u"我的页面---断言内容---进入我的页面成功")
        return result

    #断言内容-账号名称
    def login_assert_name(self):
        result = self.text(element.assert_name_loc)
        log.info(u"我的页面---断言内容---账号名称:%s"%result)
        return result

    #断言内容-加密手机号
    def login_assert_encryptionUserName(self):
        result = self.text(element.assert_encryptionUserName_loc)
        log.info(u"我的页面---断言内容---加密手机号:%s"%result)
        return result

    #断言内容-地址
    def login_assert_add(self):
        result = self.text(element.assert_add_loc)
        log.info(u"我的页面---断言内容---地址:%s"%result)
        return result

    #断言内容-嘉豆数量
    def login_assert_JiaDou(self):
        result = self.text(element.assert_JiaDou_loc)
        log.info(u"我的页面---断言内容---嘉豆数量:%s"%result)
        return result

    def login_click_icon(self):
        self.click(element.click_icon_loc)
        log.info(u"我的页面---点击右上角图标")

    #退出登录
    def login_click_loginOut(self):
        self.click(element.click_loginOut_loc)
        log.info(u"个人设置---点击退出登录")

    #确定
    def login_click_sure(self):
        self.click(element.click_sure_loc)
        log.info(u"个人设置---确定退出登录")

    def register_click_register(self):
        self.click(self.click_register_loc)
        log.info(u"登录页面---点击注册账户")


class JbJiaDouPage(BasePage):
    """
    嘉豆
    """
    click_jiaDou_loc="id=>com.hxdsw.brc:id/tv_jiadou_num"
    click_give_loc="id=>com.hxdsw.brc:id/tv_transfer"
    input_giveNum_loc="id=>com.hxdsw.brc:id/et_num"
    input_giveNumber_loc="id=>com.hxdsw.brc:id/et_phone"
    click_confirm_loc="id=>com.hxdsw.brc:id/bt_publish"
    input_password_loc="id=>com.hxdsw.brc:id/et_pwd"
    click_button_loc="id=>com.hxdsw.brc:id/right_button"
    click_complete_loc="id=>com.hxdsw.brc:id/btn_confirm"
    click_alterPwd_loc="id=>com.hxdsw.brc:id/tv_modify_pwd"
    click_alterPwd_confirm_loc="id=>com.hxdsw.brc:id/btn_next"
    click_rule_loc="id=>com.hxdsw.brc:id/tv_action"
    assert_jiaDou_loc = "id=>com.hxdsw.brc:id/title"
    assert_give_loc="id=>com.hxdsw.brc:id/tv_title"
    assert_alterPwd_loc=""

    #点击嘉豆
    def jbJiaDou_click_jiaDou(self):
        self.click(self.click_jiaDou_loc)
        log.info(u"我的页面---点击嘉豆")

    def jbJiaDou_assert_jiaDou(self):
        result = self.text(self.assert_jiaDou_loc)
        log.info(u"断言内容---进入嘉豆页面成功")
        return result

    #我要赠送
    def jbJiaDou_click_give(self):
        self.click(self.click_give_loc)
        log.info(u"我的嘉豆页面---点击我要赠送")

    def jbJiaDou_assert_give(self):
        result = self.text(self.assert_give_loc)
        log.info(u"断言内容---进入嘉豆转赠页面成功")
        return result

    #赠送数量
    def jbJia_input_giveNum(self,num):
        self.send_keys(self.input_giveNum_loc,num)
        log.info(u"嘉豆转赠页面---输入赠送数量:%s"%num)

    #获赠人
    def jbJiaDou_input_giveNumber(self,number):
        self.send_keys(self.input_giveNumber_loc,number)
        log.info(u"嘉豆转赠页面---输入赠送手机号:%s"%number)

    #确认
    def jbJiaDou_click_confirm(self):
        self.click(self.click_confirm_loc)
        log.info(u"嘉豆转赠页面---点击确认")

    #输入嘉豆密码
    def jbJiaDou_input_password(self,password):
        self.send_keys(self.input_password_loc,password)
        log.info(u"嘉豆转赠页面---输入嘉豆密码:%s"%password)

    #输入密码后点击确定
    def jbJiaDou_click_button(self):
        self.click(self.click_button_loc)
        log.info(u"嘉豆转赠页面---点击确定")

    #完成
    def jbJiaDou_click_complete(self):
        self.click(self.click_complete_loc)
        log.info(u"嘉豆转赠页面---点击完成")


    #修改密码
    def jbJiaDou_click_alterPwd(self):
        self.click(self.click_alterPwd_loc)
        log.info(u"我的嘉豆页面---点击修改密码")


    def jbJiaDou_assert_alterPwd(self):
        result = self.text(self.assert_alterPwd_loc)
        log.info(u"断言内容---进入修改密码页面成功")
        return result

    #点击确定
    def jbJiaDou_click_alterPwd_confirm(self):
        self.click(self.click_alterPwd_confirm_loc)
        log.info(u"修改密码页面---点击确定")

    #使用规则
    def jbJiaDou_click_rule(self):
        self.click(self.click_rule_loc)
        log.info("我的嘉豆页面---点击使用规则")

class JbCouponPage(BasePage):
    """
    优惠券
    """
    click_coupon_loc=u"id=>com.hxdsw.brc:id/tv_discount_num"
    click_overdue_loc='xpath=>/html/body/div[1]/div/div[1]/a[2]'
    click_receive_loc='xpath=>/html/body/div[1]/div/div[1]/a[3]'
    assert_coupon_loc="xpath=>/html/body/header/h1"
    #优惠券
    def jbCoupon_click_coupon(self):
        self.click(self.click_coupon_loc)
        time.sleep(6)
        log.info(u"我的页面---点击优惠券")

    #已用/过期
    def jbCoupon_click_overdue(self):
        self.click(self.click_overdue_loc)
        log.info(u"我的优惠券---切换到已用/过期")

    #领取优惠券
    def jbCoupon_click_receive(self):
        self.click(self.click_receive_loc)
        log.info(u"我的优惠券---切换到领取优惠券")

    def jbCoupon_assert_coupon(self):
        result = self.text(self.assert_coupon_loc)
        log.info(u"断言内容---进入我的优惠券页面成功")
        return result

class JbOrdersPage(BasePage):
    """
    我的订单
    """
    click_payment_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/parallax_scroll_view"]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]'
    click_deliver_goods_loc="id=>com.hxdsw.brc:id/tv_sendgoods"
    click_receiving_goods_loc="id=>com.hxdsw.brc:id/tv_receivegoods"
    click_evaluate_loc="id=>com.hxdsw.brc:id/tv_evaluate"
    click_after_sale_loc="id=>com.hxdsw.brc:id/tv_aftersale_service"
    click_winning_the_prize_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_me_tabs"]/android.widget.LinearLayout[5]'
    assert_winning_the_prize_loc="id=>com.hxdsw.brc:id/title"
    click_pay_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_me_tabs"]/android.widget.LinearLayout[4]'
    assert_pay_loc="id=>com.hxdsw.brc:id/tv_title"
    click_activity_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_me_tabs"]/android.widget.LinearLayout[3]'
    assert_activity_loc="id=>com.hxdsw.brc:id/title"
    click_news_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_me_tabs"]/android.widget.LinearLayout[1]'
    assert_news_loc="xpath=>/html/body/header/h1"
    click_read_loc="xpath=>/html/body/div[1]/div/div[1]/a[2]"
    click_unRead_loc="xpath=>/html/body/div[1]/div/div[1]/a[3]"
    click_housing_resources_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_me_tabs"]/android.widget.LinearLayout[2]'
    assert_housing_resources_loc="id=>com.hxdsw.brc:id/tv_title"
    click_rent_seeking_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/tl_tabs"]/android.widget.LinearLayout/android.support.v7.app.ActionBar$Tab[2]'
    click_invoice_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_me_tabs"]/android.widget.LinearLayout[7]'
    assert_invoice_loc="id=>com.hxdsw.brc:id/tv_title"
    click_wuye_pay_loc="id=>com.hxdsw.brc:id/ll_wuye_pay"
    click_draw_bill_loc="id=>com.hxdsw.brc:id/ll_draw_bill"
    click_bill_history_loc="id=>com.hxdsw.brc:id/ll_bill_history"
    click_cooperation_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_me_tabs"]/android.widget.LinearLayout[6]'


    #待付款
    def jbOrders_click_payment(self):
        time.sleep(1)
        self.click(self.click_payment_loc)
        log.info(u"我的页面---点击待付款")

    #待发货
    def jbOrders_click_deliver_goods(self):
        self.click(self.click_deliver_goods_loc)
        log.info(u"我的页面---点击待发货")

    #待收货
    def jbOrders_click_receiving_goods(self):
        self.click(self.click_receiving_goods_loc)
        log.info(u"我的页面---点击待收货")

    #待评价
    def jbOrders_click_evaluate(self):
        self.click(self.click_evaluate_loc)
        log.info(u"我的页面---点击待评价")

    #售后服务
    def jbOrders_click_after_sale(self):
        self.click(self.click_after_sale_loc)
        log.info(u"我的页面---点击售后服务")

    #中奖纪录
    def jbOrders_click_winning_the_prize(self):
        self.click(self.click_winning_the_prize_loc)
        log.info(u"我的页面---点击中奖纪录")

    def jbOrders_assert_winning_the_prize(self):
        result = self.text(self.assert_winning_the_prize_loc)
        log.info(u"断言内容---进入中奖纪录页面成功")
        return result

    #缴费记录
    def jbOrders_click_pay(self):
        self.click(self.click_pay_loc)
        log.info(u"我的页面---点击缴费记录")

    def jbOrders_assert_pay(self):
        result = self.text(self.assert_pay_loc)
        log.info(u"断言内容---进入缴费记录页面成功")
        return result

    #我的活动
    def jbOrders_click_activity(self):
        self.click(self.click_activity_loc)
        time.sleep(2)
        log.info(u"我的页面---点击我的活动")

    def jbOrders_assert_activity(self):
        result = self.text(self.assert_activity_loc)
        log.info(u"断言内容---进入我的活动页面成功")
        return result

    #我的消息
    def jbOrders_click_news(self):
        self.click(self.click_news_loc)
        log.info(u"我的页面---点击我的消息")

    def jbOrders_assert_news(self):
        result = self.text(self.assert_news_loc)
        log.info(u"断言内容---进入我的消息页面成功")
        return result

    #已阅读
    def jbOrders_click_read(self):
        self.click(self.click_read_loc)
        log.info(u"消息通知---点击已阅读")

    #未阅读
    def jbOrders_click_unRead(self):
        self.click(self.click_unRead_loc)
        log.info(u"消息通知---点击未阅读")

    #我的房源
    def jbOrders_click_housing_resources(self):
        self.click(self.click_housing_resources_loc)
        log.info(u"我的页面---点击我的房源")

    def jbOrders_assert_housing_resources(self):
        result = self.text(self.assert_housing_resources_loc)
        log.info(u"断言内容---进入我的房源页面成功")
        return result

    #求组求售
    def jbOrders_click_rent_seeking(self):
        self.click(self.click_rent_seeking_loc)
        log.info(u"我的房源---点击求租求售")

    #我的发票
    def jbOrders_click_invoice(self):
        self.click(self.click_invoice_loc)
        log.info(u"我的页面---点击我的发票")

    def jbOrders_assert_invoice(self):
        result = self.text(self.assert_invoice_loc)
        log.info(u"断言内容---进入我的发票页面成功")
        return result

    #物业缴费
    def jbOrders_click_wuye_pay(self):
        self.click(self.click_wuye_pay_loc)
        log.info(u"开具发票---点击物业缴费")

    #临停开票
    def jbOrders_click_draw_bill(self):
        self.click(self.click_draw_bill_loc)
        log.info(u"开具发票---点击临停开票")

    #开票历史
    def jbOrders_click_bill_history(self):
        self.click(self.click_bill_history_loc)
        log.info(u"开具发票---点击开票历史")


    #商务合作
    def jbOrders_click_cooperation(self):
        self.click(self.click_cooperation_loc)
        log.info(u"我的页面---点击商务合作")

class JbSettingPage(BasePage):
    """
    设置
    """
    click_head_loc="id=>com.hxdsw.brc:id/tv_nike_name"
    assert_head_loc="id=>com.hxdsw.brc:id/tv_title"
    click_edit_loc="id=>com.hxdsw.brc:id/right_text_button"
    click_preservation_loc="id=>com.hxdsw.brc:id/right_text_button"
    click_project_add_loc="id=>com.hxdsw.brc:id/menu_address"
    assert_project_name_loc="id=>com.hxdsw.brc:id/menu_address"
    assert_project_add_loc="id=>com.hxdsw.brc:id/tv_title"
    click_other_project_add_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/other_house_lv"]/android.widget.RelativeLayout'
    click_cancel_project_add=u"id=>com.hxdsw.brc:id/left_button"
    click_switch_project_add="id=>com.hxdsw.brc:id/right_button"
    assert_currert_project_add_name='xpath=>//*[@resource-id="com.hxdsw.brc:id/rl_curr_house"]/android.widget.TextView[1]'
    assert_other_project_add_name='xpath=>//*[@resource-id="com.hxdsw.brc:id/other_house_lv"]/android.widget.RelativeLayout/android.widget.TextView[1]'
    click_change_password_loc="id=>com.hxdsw.brc:id/layout_change_pwd"
    click_clear_cache_loc="id=>com.hxdsw.brc:id/layout_clear_cache"
    click_sure_clear_cache_loc="id=>com.hxdsw.brc:id/right_button"
    click_zhikong_pattern_loc="id=>com.hxdsw.brc:id/layout_security_mode"
    click_switch_zhikong_pattern_loc="id=>com.hxdsw.brc:id/box_new"
    click_shake_loc="id=>com.hxdsw.brc:id/OpenDoorOnBtn"
    click_notification_voice_loc="id=>com.hxdsw.brc:id/tb_notification_sound"
    click_notification_vibration_loc="id=>com.hxdsw.brc:id/tb_notification_vibrator"
    click_feedback_loc="id=>com.hxdsw.brc:id/ll_suggestion"
    click_home_loc="id=>com.hxdsw.brc:id/ll_about"
    click_complaint_loc="id=>com.hxdsw.brc:id/ll_complaint"
    click_complaint1_loc="id=>com.hxdsw.brc:id/ll_complaint"
    click_select_reason_loc="id=>com.hxdsw.brc:id/rb_reason1"
    click_confirm_complaint_loc="id=>com.hxdsw.brc:id/tv_next"
    click_button_loc="id=>com.hxdsw.brc:id/single_button"
    click_cancellation_loc="id=>com.hxdsw.brc:id/ll_logout"
    click_untying_house_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/other_house']/android.widget.ListView/android.widget.RelativeLayout/android.widget.TextView[3]"
    click_untying_house_reason_loc="id=>com.hxdsw.brc:id/rb_reason1"
    click_select_reason_determine_loc="id=>com.hxdsw.brc:id/right_button"
    click_add_house_loc="id=>com.hxdsw.brc:id/add_house"
    click_city_loc="id=>com.hxdsw.brc:id/city_layout"
    click_select_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/content']/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[6]"
    click_community_loc="id=>com.hxdsw.brc:id/community_layout"
    click_select_pixian_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/left_community_lv']/android.widget.RelativeLayout[7]"
    click_select_community_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/community_lv']/android.widget.LinearLayout[6]"
    click_building_loc="id=>com.hxdsw.brc:id/building_no_layout"
    click_select_building_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/building_lv']/android.widget.LinearLayout[8]"
    click_select_building_formal_loc="id=>com.hxdsw.brc:id/text"
    click_unit_room_number_loc="id=>com.hxdsw.brc:id/unit_room_number_layout"
    click_select_unit_room_number_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/house_no_lv']/android.widget.LinearLayout[3]"
    click_select_unit_room_number_formal_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/house_no_lv']/android.widget.LinearLayout"
    input_mobile_loc="id=>com.hxdsw.brc:id/last_phone_no"
    click_verification_loc="id=>com.hxdsw.brc:id/start_verify"
    input_community_name_loc="id=>com.hxdsw.brc:id/input_serach"
    click_select_community_name_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/query_results_lv']/android.widget.LinearLayout[4]"




    #我的资料
    def jbSetting_click_head(self):
        self.click(self.click_head_loc)
        log.info(u"我的页面---点击头像")

    def jbSetting_assert_head(self):
        result = self.text(self.assert_head_loc)
        log.info(u"断言内容---进入我的资料页面成功")
        return result

    #编辑资料
    def jbSetting_click_edit(self):
        self.click(self.click_edit_loc)
        log.info(u"我的资料页面---点击编辑")

    #保存
    def jbSetting_click_preservation(self):
        time.sleep(1)
        self.click(self.click_preservation_loc)
        log.info(u"我的资料页面---点击保存")

    #我的项目
    def jbSetting_click_project_add(self):
        self.click(self.click_project_add_loc)
        log.info(u"我的页面---点击项目")

    def JbSetting_assert_project_name(self):
        result = self.text(self.assert_project_name_loc)
        log.info(u"断言内容---项目名称：%s"%result)
        return result

    #我的项目
    def jbSetting_assert_project_add(self):
        result = self.text(self.assert_project_add_loc)
        log.info(u"断言内容---进入我的房屋页面成功")
        return result

    #其他房屋
    def jbSetting_click_other_project_add(self):
        self.click(self.click_other_project_add_loc)
        log.info(u"我的房屋---点击其他房屋")

    #切换取消
    def jbSetting_click_cancel_project_add(self):
        self.click(self.click_cancel_project_add)
        log.info(u"我的房屋---点击取消")

    #切换
    def jbSetting_click_switch_project_add(self):
        self.click(self.click_switch_project_add)
        log.info(u"我的房屋---点击切换")

    #当前房屋名称
    def jbSetting_assert_current_project_add_name(self):
        result = self.text(self.assert_currert_project_add_name)
        log.info(u"我的房屋---当前房屋名称:%s"%(result))
        return result

    #其他房屋名称
    def jbSetting_assert_other_project_add_name(self):
        result = self.text(self.assert_other_project_add_name)
        log.info(u"我的房屋---其他房屋名称:%s"%(result))
        return result


    #修改密码
    def jbSetting_click_change_password(self):
        self.click(self.click_change_password_loc)
        log.info(u"个人设置页面---点击修改密码")

    #清除缓存
    def jbSetting_click_clear_cache(self):
        self.click(self.click_clear_cache_loc)
        log.info(u"个人设置页面---点击清除缓存")

    #确定清除缓存
    def jbSetting_click_sure_clear_cache(self):
        self.click(self.click_sure_clear_cache_loc)
        log.info(u"个人设置页面---点击清除缓存")

    #智控模式
    def jbSetting_click_zhikong_pattern(self):
        self.click(self.click_zhikong_pattern_loc)
        log.info(u"个人设置页面---点击智控模式")

    def jbSetting_click_switch_zhikong_pattern(self):
        self.click(self.click_switch_zhikong_pattern_loc)
        log.info(u"个人设置页面---切换到新版")

    #摇一摇开门
    def jbSetting_click_shake(self):
        self.click(self.click_shake_loc)
        log.info(u"个人设置页面---点击摇一摇开门")

    #通知声音
    def jbSetting_click_notification_voice(self):
        self.click(self.click_notification_voice_loc)
        log.info(u"个人设置页面---点击通知声音")

    #通知震动
    def jbSetting_click_notification_vibration(self):
        self.click(self.click_notification_vibration_loc)
        log.info(u"个人设置页面---点击通知震动")

    #意见反馈
    def jbSetting_click_feedback(self):
        self.click(self.click_feedback_loc)
        log.info(u"个人设置页面---点击意见反馈")

    #关于生活家
    def jbSetting_click_home(self):
        self.click(self.click_home_loc)
        log.info(u"个人设置页面---点击关于生活家")

    #个人信息投诉
    def jbSetting_click_complaint(self):
        self.click(self.click_complaint_loc)
        log.info("个人设置页面---点击个人信息投诉")

    #个人信息安全投诉
    def jbSetting_click_complaint1(self):
        self.click(self.click_complaint1_loc)
        log.info("个人信息投诉页面---点击个人信息安全投诉")

    #选择第一个原因
    def jbSetting_click_select_reason(self):
        self.click(self.click_select_reason_loc)
        log.info("个人信息安全投诉页面---选择第一个原因")

    #确认投诉
    def jbSetting_click_confirm_complaint(self):
        self.click(self.click_confirm_complaint_loc)
        log.info("个人信息安全投诉页面---点击确认投诉")

    #关闭提示框(知道了)
    def jbSetting_click_button(self):
        time.sleep(2)
        self.click(self.click_button_loc)
        log.info("个人信息安全投诉页面---点击知道了")
        time.sleep(1)

    #账号注销
    def jbSetting_click_cancellation(self):
        self.click(self.click_cancellation_loc)
        log.info("个人设置页面---点击账号注销")

    #房屋解绑
    def jbSetting_click_untying_house(self):
        self.click(self.click_untying_house_loc)
        log.info("我的房屋页面---点击解绑房屋")

    #选择房屋解绑原因
    def jbSetting_click_untying_house_reason(self):
        self.click(self.click_untying_house_reason_loc)
        log.info("我的房屋页面---解绑房屋原因")

    #选中原因后点击确定
    def jbSetting_click_select_reason_determine(self):
        self.click(self.click_select_reason_determine_loc)
        log.info("我的房屋页面---点击确定")

    #点击添加房屋
    def jbSetting_click_add_house(self):
        self.click(self.click_add_house_loc)
        log.info("我的房屋页面---点击添加房屋")

    #城市
    def jbSetting_click_city(self):
        self.click(self.click_city_loc)
        log.info("选择房屋信息页面---点击城市")

    #选择城市
    def jbSetting_click_select_city(self):
        self.click(self.click_select_loc)
        log.info("选择城市页面---选择成都市")

    #社区
    def jbSetting_click_community(self):
        self.click(self.click_community_loc)
        log.info("选择房屋信息页面---点击社区")


    #选择郫县
    def jbSetting_click_select_pixian(self):
        self.click(self.click_select_pixian_loc)
        log.info("选择社区页面---选择郫县")

    #选择幸福满庭
    def jbSetting_click_select_community(self):
        self.click(self.click_select_community_loc)
        log.info("选择社区页面---选择幸福满庭")

    #楼栋号
    def jbSetting_click_building(self):
        self.click(self.click_building_loc)
        log.info("选择房屋信息页面---点击楼栋号")

    #选择楼栋号(17栋)
    def jbSetting_click_select_building(self):
        self.click(self.click_select_building_loc)
        log.info("选择楼栋页面---选择幸福满庭17栋")

    #正式环境选择楼栋号
    def jbSetting_click_select_building_formal(self):
        self.click(self.click_select_building_formal_loc)
        log.info("选择楼栋页面---生活家智慧小区CRM中心1栋")

    #单元房号
    def jbSetting_click_unit_room_number(self):
        self.click(self.click_unit_room_number_loc)
        log.info("选择房屋信息页面---点击单元房号")

    #选择单元和房号(17-01-0403)
    def jbSetting_click_select_unit_room_number(self):
        self.click(self.click_select_unit_room_number_loc)
        log.info("选择单元和房号页面---选择幸福满庭17栋XFMT一期17-01-0403")

    #正式环境选择单元和房号(1栋1楼)
    def jbSetting_click_select_unit_room_number_formal(self):
        self.click(self.click_select_unit_room_number_formal_loc)
        log.info("选择单元和房号页面---选择成都市生活家智慧小区CRM中心1栋1楼")

    #输入域手机号后4位
    def jbSetting_input_mobile(self,content):
        self.send_keys(self.input_mobile_loc,content)
        log.info("选择房屋信息页面---输入手机号码后四位:{}".format(content))

    #开始验证
    def jbSetting_click_verification(self):
        self.click(self.click_verification_loc)
        log.info("选择房屋信息页面---点击开始验证")

    #社区_输入社区名称
    def jbSetting_input_community_name(self,content):
        self.send_keys(self.input_community_name_loc,content)
        log.info("选择社区页面---输入名称:{}".format(content))

    #社区_选择社区名称
    def jbSetting_click_select_community_name(self):
        self.click(self.click_select_community_name_loc)
        log.info("选择社区页面---选择社区")









