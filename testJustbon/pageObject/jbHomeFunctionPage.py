# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/4/24 14:51
import re,time,random
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
log = PublicLogs()
class JbHomeNoticePage(BasePage):
    """
    公告
    """
    notice_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/top_recyclerview"]/android.widget.LinearLayout[1]'
    input_search_loc="id=>com.hxdsw.brc:id/search_content"
    click_icon_loc="id=>com.hxdsw.brc:id/type_btn"
    click_whole_loc="id=>com.hxdsw.brc:id/type_qb"
    click_news_loc="id=>com.hxdsw.brc:id/type_xwkb"
    click_classroom_loc="id=>com.hxdsw.brc:id/type_xjkt"
    click_prompt_loc="id=>com.hxdsw.brc:id/type_wxts"
    click_activity_loc="id=>com.hxdsw.brc:id/type_hdyg"
    click_lost_found_loc="id=>com.hxdsw.brc:id/type_swzl"
    assert_notice_loc="id=>com.hxdsw.brc:id/news_title_name"
    assert_title_loc="id=>com.hxdsw.brc:id/news_title"
    assert_time_loc="id=>com.hxdsw.brc:id/news_time"
    click_content_loc='xpath=>//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]'

    #公告
    def jbHomeNotice_click_notice(self):
        self.click(self.notice_loc)
        log.info(u"首页页面---点击公告")

    #关键字搜索
    def jbHomeNotice_input_search(self,content):
        self.send_keys(self.input_search_loc,content)
        self.search(self.input_search_loc)
        log.info(u"公告页面---关键字搜索输入内容:%s"%content)

    #右上角图标
    def jbHomeNotice_click_icon(self):
        self.click(self.click_icon_loc)
        log.info(u"公告页面---点击右上角按钮")

    def jbHomeNotice_click_whole(self):
        self.click(self.click_whole_loc)
        log.info(u"公告页面---点击全部")

    def jbHomeNotice_click_news(self):
        self.click(self.click_news_loc)
        log.info(u"公告页面---筛选新闻快报")

    def jbHomeNotice_click_classroom(self):
        self.click(self.click_classroom_loc)
        log.info(u"公告页面---筛选小嘉课堂")

    def jbHomeNotice_click_prompt(self):
        self.click(self.click_prompt_loc)
        log.info(u"公告页面---筛选温馨提示")

    def jbHomeNotice_click_activity(self):
        self.click(self.click_activity_loc)
        log.info(u"公告页面---筛选活动预告")

    def jbHomeNotice_click_lost_found(self):
        self.click(self.click_lost_found_loc)
        log.info(u"公告页面---筛选失物招领")

    def jbHomeNotice_assert_notice(self):
        result=self.text(self.assert_notice_loc)
        log.info(u"公告页面---断言内容---进入公告页面成功")
        return result

    #第一条公告内容的名称
    def jbHomeNotice_assert_title(self):
        result=self.text(self.assert_title_loc)
        log.info(u"公告页面---断言内容---公告第一条内容标题:%s"%result)
        return result

    #第一条公告内容的时间
    def jbHomeNotice_assert_time(self):
        result=self.text(self.assert_time_loc)
        log.info(u"公告页面---断言内容---公告第一条内容标题:%s"%result)
        return result

    def jbHomeNotice_click_content(self):
        self.click(self.click_content_loc)
        log.info(u"公告页面---点击第一个公告")

class JbHomeHousekeeperPage(BasePage):
    """
    管家
    """
    housekeeper_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/top_recyclerview"]/android.widget.LinearLayout[2]'
    more_loc="id=>com.hxdsw.brc:id/another_call"
    assert_more_loc="id=>com.hxdsw.brc:id/title"
    assert_first_name_loc = "ids=>com.hxdsw.brc:id/tv_name"
    #点击管家
    def jbHomeHousekeeper_click_housekeeper(self):
        self.click(self.housekeeper_loc)
        time.sleep(2)
        log.info(u"首页页面---点击管家按钮")

    #查看更多管家
    def jbHomeHousekeeper_click_more(self):
        self.click(self.more_loc)
        log.info(u"管家页面---点击查看全部管家")

    def jbHomeHousekeeper_assert_more(self):
        result=self.text(self.assert_more_loc)
        log.info(u"管家页面---断言内容---进入查看全部管家成功")
        return result

    def jbHomeHousekeeper_assert_first_name(self):
        result = self.find_element(self.assert_first_name_loc)
        # result__first_name = result[0].text
        # log.info(u"管家团队成员---断言内容---第一个管家的名字:%s"%(result__first_name))
        return result


class JbhomePayPage(BasePage):
    """
    缴费
    """
    pay_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/top_recyclerview"]/android.widget.LinearLayout[3]'
    historyPay_loc="id=>com.hxdsw.brc:id/historical_bills"
    click_paymentSlip_loc="id=>com.hxdsw.brc:id/rl_my_not_pay"
    click_paymentSlip_cancel_loc="id=>com.hxdsw.brc:id/tv_cancel"
    click_paymentSlip_cancel_determine_loc="id=>com.hxdsw.brc:id/right_button"
    click_paymentSlip_pay_loc="id=>com.hxdsw.brc:id/tv_pay"
    click_invoice_loc="id=>com.hxdsw.brc:id/action_btn"
    click_immediately_pay_loc="id=>com.hxdsw.brc:id/wuye_pay"
    click_pre_storage_loc="id=>com.hxdsw.brc:id/prestore_btn"
    click_pre_storage_cancel_loc="id=>com.hxdsw.brc:id/left_button"
    click_pre_storage_determine_loc="id=>com.hxdsw.brc:id/right_button"
    input_pre_storage_money_loc='id=>com.hxdsw.brc:id/tv_500'
    click_immediate_payment_loc="id=>com.hxdsw.brc:id/pay_immediately"
    click_wx_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/ll_pay_type"]/android.widget.LinearLayout[2]'
    click_wxPay_loc="id=>com.tencent.mm:id/g2b"
    click_zfb_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/ll_pay_type"]/android.widget.LinearLayout[3]'
    click_zh_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/ll_pay_type"]/android.widget.LinearLayout[5]'
    click_confirmation_of_payment_loc="id=>com.hxdsw.brc:id/btn_pay"
    click_cancel_order_loc="id=>com.hxdsw.brc:id/btn_ret_home_page"
    click_cancel_order_determine_loc="id=>com.hxdsw.brc:id/right_button"
    jbHomePay_click_cancel_order_determine_return_loc="id=>com.hxdsw.brc:id/btn_ret_home_page"
    click_pay_order_loc="id=>com.hxdsw.brc:id/btn_retry"
    click_first_bill_loc='xpath=>//*[@resource-id="android:id/list"]/android.widget.LinearLayout[1]'
    click_confirmation_payment_loc="id=>com.hxdsw.brc:id/pay"
    click_go_loc="id=>com.hxdsw.brc:id/right_button"

    #点击缴费
    def jbHomePay_click_pay(self):
        self.click(self.pay_loc)
        log.info(u"首页页面---点击缴费按钮")

    def jbHomePay_click_historyPay(self):
        self.click(self.historyPay_loc)
        log.info(u"物业缴费页面---点击历史账单")

    def jbHomePay_click_paymentSlip(self):
        self.click(self.click_paymentSlip_loc)
        log.info(u"物业缴费页面---点击缴费单")

    #缴费单点击取消
    def jbHomePay_click_paymentSlip_cancel(self):
        self.click(self.click_paymentSlip_cancel_loc)
        log.info(u"物业缴费页面---选择缴费单点击取消")

    #缴费单取消谈框点击确定
    def jbHomePay_click_paymentSlip_cancel_determine(self):
        self.click(self.click_paymentSlip_cancel_determine_loc)
        log.info(u"物业缴费页面---选择缴费单点击确定")

    def jbHomePay_click_paymentSlip_pay(self):
        self.click(self.click_paymentSlip_pay_loc)
        log.info(u"物业缴费页面---缴费单点击支付")

    def jbHomePay_click_invoice(self):
        self.click(self.click_invoice_loc)
        log.info(u"物业缴费页面---点击开发票")

    #立即缴费
    def jbHomePay_click_immediately_pay(self):
        self.click(self.click_immediately_pay_loc)
        log.info(u"物业缴费页面---点击立即缴费")

    #预存物业费
    def jbHomePay_click_pre_storage(self):
        self.click(self.click_pre_storage_loc)
        log.info(u"物业缴费页面---预存物业费")

    def jbHomePay_click_pre_storage_cancel(self):
        self.click(self.click_pre_storage_cancel_loc)
        log.info(u"物业缴费页面---点击取消")

    #预存物业费点击确定
    def jbHomePay_click_pre_storage_determine(self):
        self.click(self.click_pre_storage_determine_loc)
        log.info(u"物业缴费页面---点击确定")

    #输入预存金额
    def jbHomePay_input_pre_storage_money(self):
        self.click(self.input_pre_storage_money_loc)
        log.info(u"预存物业费页面---选择预存金额")

    #立即支付
    def jbHomePay_click_immediate_payment(self):
        self.click(self.click_immediate_payment_loc)
        time.sleep(3)
        log.info(u"预存物业费页面---点击立即支付")

    #微信
    def jbHomePay_click_wx(self):
        self.click(self.click_wx_loc)
        log.info(u"支付缴费页面---选择微信")

    def jbHomePay_click_wxPay(self):
        self.click(self.click_wxPay_loc)
        log.info("维信支付页面---点击立即支付")

    #支付宝
    def jbHomePay_click_zfb(self):
        self.click(self.click_zfb_loc)
        log.info(u"支付缴费页面---选择支付宝")

    #招行一网通
    def jbHomePay_click_zh(self):
        self.click(self.click_zh_loc)
        log.info("支付缴费页面---选择招行一网通")

    #确认支付
    def jbHomePay_click_confirmation_of_payment(self):
        self.click(self.click_confirmation_of_payment_loc)
        time.sleep(10)
        log.info(u"支付页面----点击确认支付")

    #支付缴费取消订单
    def jbHomePay_click_cancel_order(self):
        self.click(self.click_cancel_order_loc)
        log.info(u"支付缴费页面----点击取消订单")

    #支付缴费弹框点击确定
    def jbHomePay_click_cancel_order_determine(self):
        self.click(self.click_cancel_order_determine_loc)
        time.sleep(2)
        log.info(u"支付缴费页面---取消订单弹框点击确定")

    #支付缴费取消订单后点击返回
    def jbHomePay_click_cancel_order_determine_return(self):
        self.click(self.jbHomePay_click_cancel_order_determine_return_loc)
        log.info(u"支付缴费页面---点击返回")

    #支付缴费支付订单
    def jbHomePay_click_pay_order(self):
        self.click(self.click_pay_order_loc)
        log.info(u"支付缴费页面---点击支付订单")

    #选择第一笔待缴费单
    def jbHomePay_click_first_bill(self):
        self.click(self.click_first_bill_loc)
        log.info(u"物业缴费页面---选择第一笔待缴费单")

    #确认缴费
    def jbHomePay_click_confirmation_payment(self):
        self.click(self.click_confirmation_payment_loc)
        log.info(u"账单详情页面---点击确认缴费")

    #现在去(有未支付的订单,点击立即缴费会有弹框)
    def jbHomePay_click_go(self):
        self.click(self.click_go_loc)
        log.info(u"物业缴费页面---点击现在去")

class JbhomeOpenDoorPage(BasePage):
    """
    开门
    """

    click_door_loc = 'xpath=>//*[@resource-id="com.hxdsw.brc:id/top_recyclerview"]/android.widget.LinearLayout[4]'
    def jbHomeDoor_click_door(self):
        self.click(self.click_door_loc)
        log.info(u"首页页面---进入开门")

class JbhomeGuaranteePage(BasePage):
    """
    报修
    """
    guarantee_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/top_recyclerview"]/android.widget.LinearLayout[5]'
    order_loc="id=>com.hxdsw.brc:id/order"
    assert_guarantee_loc="id=>com.hxdsw.brc:id/title"
    assert_conduct_id_loc="ids=>com.hxdsw.brc:id/orderNum"
    assert_conduct_status_loc="ids=>com.hxdsw.brc:id/state"
    assert_conduct_content_loc="ids=>com.hxdsw.brc:id/content"
    assert_conduct_time_loc="ids=>com.hxdsw.brc:id/time"
    done_loc="id=>com.hxdsw.brc:id/finished"
    assert_done_id_loc="ids=>com.hxdsw.brc:id/orderNum"
    assert_done_status_loc="ids=>com.hxdsw.brc:id/state"
    assert_done_content_loc="ids=>com.hxdsw.brc:id/content"
    assert_done_time_loc="ids=>com.hxdsw.brc:id/time"
    publicGuarantee_loc="id=>com.hxdsw.brc:id/publicRepair"
    content_loc="id=>com.hxdsw.brc:id/suggest"
    click_select_loc="id=>com.hxdsw.brc:id/time"
    click_submit_loc="id=>com.hxdsw.brc:id/submit"
    assert_submit_loc="id=>com.hxdsw.brc:id/submit"
    click_determine_loc="id=>com.hxdsw.brc:id/confirm"
    click_djlx_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/repair_ll"]/android.widget.GridView/android.widget.LinearLayout[1]'
    click_ltgj_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/repair_ll"]/android.widget.GridView/android.widget.LinearLayout[2]'
    click_wyjj_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/repair_ll"]/android.widget.GridView/android.widget.LinearLayout[3]'
    click_mcjj_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/repair_ll"]/android.widget.GridView/android.widget.LinearLayout[4]'
    click_dkst_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/repair_ll"]/android.widget.GridView/android.widget.LinearLayout[5]'
    click_kshs_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/repair_ll"]/android.widget.GridView/android.widget.LinearLayout[6]'
    click_afyy_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/repair_ll"]/android.widget.GridView[2]/android.widget.LinearLayout/android.widget.LinearLayout'
    click_frequency_determine_loc="id=>com.hxdsw.brc:id/right_button"
    click_immediate_appointment_loc="id=>com.hxdsw.brc:id/submit"

    #点击报修
    def jbHomeGuarantee_click_guarantee(self):
        self.click(self.guarantee_loc)
        log.info(u"首页页面---点击报修按钮")

    #我的订单
    def jbHomeGuarantee_click_order(self):
        self.click(self.order_loc)
        log.info(u"报修页面---点击我的订单")


    def jbHomeGuarantee_assert_guarantee(self):
        result = self.text(self.assert_guarantee_loc)
        log.info(u"报修页面---断言内容---进入报修页面成功")
        return result

    #进行中的第一个订单id
    def jbHomeGuarantee_assert_conduct_id(self):
        result_text = self.find_element(self.assert_conduct_id_loc)
        result = re.findall("\d+",result_text[0].text)
        try:
            log.info(u"我的保修订单页面---断言内容---第一个订单编号:%s"%result[0])
            return result[0]
        except:
            log.info(u"我的报修订单页面---断言内容---进行中无订单")
            return None

    #进行中的第一个订单状态
    def jbHomeGuarantee_assert_conduct_status(self):
        result = self.find_element(self.assert_conduct_status_loc)
        try:
            if result[0].text == u"待接单":
                result_status="10"
            elif result[0].text == u"处理中":
                result_status="20"
            elif result[0].text == u"待付款":
                result_status="30"
            log.info(u"我的保修订单页面---断言内容---进行中第一个订单状态:%s"%result[0].text)
            return result_status
        except:
            log.info(u"我的报修订单页面---断言内容---进行中无订单")
            return None

    #进行中的第一个订单内容
    def jbHomeGuarantee_assert_conduct_content(self):
        result = self.find_element(self.assert_conduct_content_loc)
        try:
            log.info(u"我的保修订单页面---断言内容---进行中第一个订单内容:%s"%result[1].text)
            return result[1].text
        except:
            log.info(u"我的报修订单页面---断言内容---进行中无订单")
            return None

    #进行中的第一个订单时间
    def jbHomeGuarantee_assert_conduct_time(self):
        result = self.find_element(self.assert_conduct_time_loc)
        try:
            log.info(u"我的保修订单页面---断言内容---进行中第一个订单时间:%s"%result[0].text)
            return result[0].text
        except:
            log.info(u"我的报修订单页面---断言内容---进行中无订单")
            return None

    #点击已完成
    def jbHomeGuarantee_click_done(self):
        self.click(self.done_loc)
        log.info(u"我的报修订单页面---点击切换到已完成")


    #已完成的第一个订单id
    def jbHomeGuarantee_assert_done_id(self):
        result_text = self.text(self.assert_done_id_loc)
        result = re.findall("\d+",result_text[0].text)

        try:
            log.info(u"我的保修订单页面---断言内容---已完成的第一个订单编号:%s"%result)
            return result[0]
        except:
            log.info(u"我的报修订单页面---断言内容---已完成无订单")
            return None


    #已完成的第一个订单状态
    def jbHomeGuarantee_assert_done_status(self):
        result = self.find_element(self.assert_done_status_loc)
        try:
            if result == u"已完成":
                result_status="50"
            elif result == u"已取消":
                result_status="60"
            log.info(u"我的保修订单页面---断言内容---已完成第一个订单状态:%s"%result[0].text)
            return result_status
        except:
            log.info(u"我的报修订单页面---断言内容---已完成无订单")
            return None

    #已完成的第一个订单内容
    def jbHomeGuarantee_assert_done_content(self):
        result = self.text(self.assert_done_content_loc)
        try:
            log.info(u"我的保修订单页面---断言内容---已完成第一个订单内容:%s"%result[1].text)
            return result[1].text
        except:
            log.info(u"我的报修订单页面---断言内容---已完成无订单")
            return None

    #已完成的第一个订单时间
    def jbHomeGuarantee_assert_done_time(self):
        result = self.text(self.assert_done_time_loc)
        try:
            log.info(u"我的保修订单页面---断言内容---已完成第一个订单时间:%s"%result[0].text)
            return result[0].text
        except:
            log.info(u"我的报修订单页面---断言内容---已完成无订单")
            return None


    #点击公共维修
    def jbHomeGuarantee_click_publicGuarantee(self):
        time.sleep(2)
        self.click(self.publicGuarantee_loc)
        log.info(u"嘉维修页面---点击公共维修")

    #工单填写内容
    def jbHomeGuarantee_input_content(self,value):
        self.send_keys(self.content_loc,value)
        log.info(u"公共维修---工单填写---填写内容:%s"%value)

    #点击请选择
    def jbHomeGuarantee_click_select(self):
        self.click(self.click_select_loc)
        log.info(u"公告维修---工单填写页面---点击请选择")

    #点击确定
    def jbHomeGuarantee_click_determine(self):
        self.click(self.click_determine_loc)
        log.info(u"公告维修---工单填写页面---选择时间后,点击确认")

    #点击提交
    def jbHomeFuarantee_click_submit(self):
        self.click(self.click_submit_loc)
        log.info(u"公共维修---工单填写页面---点击提交")
        time.sleep(2)

    def jbHomeFuarantee_assert_submit(self):
        result = self.text(self.assert_submit_loc)
        log.info(u"公共维修---工单填写页面---提交按钮:%s"%result)

    def jbHomeFuarantee_click_djlx(self):
        self.click(self.click_djlx_loc)
        log.info(u"嘉维修页面---点击灯具路线")

    def jbHomeFuarantee_click_ltgj(self):
        self.click(self.click_ltgj_loc)
        log.info(u"嘉维修页面---点击龙头管件")

    def jbHomeFuarantee_click_wyjj(self):
        self.click(self.click_wyjj_loc)
        log.info(u"嘉维修页面---点击卫具洁具")

    def jbHomeFuarantee_click_mcjj(self):
        self.click(self.click_mcjj_loc)
        log.info(u"嘉维修页面---点击门窗家居")

    def jbHomeFuarantee_click_dkst(self):
        self.click(self.click_dkst_loc)
        log.info(u"嘉维修页面---点击打孔疏通")

    def jbHomeFuarantee_click_kshs(self):
        self.click(self.click_kshs_loc)
        log.info(u"嘉维修页面---点击开锁换锁")

    def jbHomeFuantee_click_afyy(self):
        self.click(self.click_afyy_loc)
        log.info(u"嘉维修页面---点击安防预约")


    #保险次数为0,点击确定
    def jbHomePuantee_click_frequency_determine(self):
        self.click(self.click_frequency_determine_loc)
        log.info("嘉维修页面---点击确定")

    #立即预约
    def jbHomePuantee_click_immediate_appointment(self):
        self.click(self.click_immediate_appointment_loc)
        log.info("灯具线路页面---点击立即预约")
    #
    # #灯具线路点击服务时间
    # def jbHomePuantee_click_djlx_time(self):
    #     self.click(self.click_djlx_time_loc)
    #     log.info("灯具路线预约服务页面---点击服务时间")
    #
    # #灯具路线选择服务时间
    # def jbHomePuantee_click_djlx_select_time(self):
    #     self.click(self.click_djlx_select_time_loc)
    #     log.info("灯具路线预约服务页面---选择服务时间")
    #
    # #填写内容
    # def jbHomePuantee_input_djlx_content(self,content):
    #     self.send_keys(self.input_djlx_content_loc,content)
    #     log.info("预约服务页面---填写内容:{}".format(content))
    #
    # #预约服务页面_立即预约
    # def jbHomePuantee_click_djlx_immediate_appointment(self):
    #     self.click(self.click_djlx_immediate_appointment_loc)
    #     log.info("预约服务页面---点击立即预约")



class JbHomeComplaintPage(BasePage):
    """
    投诉
    """
    click_complaint_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/top_recyclerview"]/android.widget.LinearLayout[6]'
    click_done_loc="id=>com.hxdsw.brc:id/finished"
    click_wantPraise_loc="id=>com.hxdsw.brc:id/praise_ll"
    input_content_loc="id=>com.hxdsw.brc:id/suggest"
    click_submit_loc="id=>com.hxdsw.brc:id/submit"
    click_wantComplaint_loc="id=>com.hxdsw.brc:id/complaint_ll"
    assert_conduct_name_loc='//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/com.hxdsw.brc:id/title/com.hxdsw.brc:id/task_type'
    assert_conduct_id_loc='//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/com.hxdsw.brc:id/title/com.hxdsw.brc:id/com.hxdsw.brc:id/task_no'
    assert_conduct_content_loc='//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/com.hxdsw.brc:id/context_ll/com.hxdsw.brc:id/context'
    assert_done_name_loc='//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/com.hxdsw.brc:id/title/com.hxdsw.brc:id/task_type'
    assert_done_id_loc='//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/com.hxdsw.brc:id/title/com.hxdsw.brc:id/com.hxdsw.brc:id/task_no'
    assert_done_content_loc='//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/com.hxdsw.brc:id/context_ll/com.hxdsw.brc:id/context'

    #投诉
    def jbHomeComplaint_click_complaint(self):
        self.click(self.click_complaint_loc)
        log.info(u"首页页面---点击投诉")

    #切换到已完成
    def jbHomeComplaint_click_done(self):
        self.click(self.click_done_loc)
        log.info(u"投诉表扬---点击已完成")

    #我要表扬
    def jbHomeComplaint_click_wantPraise(self):
        self.click(self.click_wantPraise_loc)
        log.info(u"投诉表扬---点击我要表扬")

    #填写内容
    def jbHomeComplaint_input_content(self,content):
        self.send_keys(self.input_content_loc,content)
        log.info(u"表扬工单填写页面---填写内容:%s"%(content))

    #点击提交
    def jbHomeComplaint_click_submit(self):
        self.click(self.click_submit_loc)
        log.info(u"表扬工单填写页面---点击提交")

    #点击投诉
    def jbHomeComplaint_click_wantComplaint(self):
        self.click(self.click_wantComplaint_loc)
        log.info(u"投诉表扬---点击我要投诉")

    #进行中的name(表扬或投诉)
    def jbHomeComplaint_assert_conduct_name(self):
        result_text = self.find_element(self.assert_conduct_name_loc)
        try:
            log.info(u"投诉表扬页面---断言内容---进行中第一个工单类型:%s"%result_text[0].text)
            return result_text[0].text
        except:
            log.info(u"投诉表扬页面---断言内容---无工单")
            return None

    #进行中的id
    def jbHomeComplaint_assert_conduct_id(self):
        result_text = self.find_element(self.assert_conduct_id_loc)
        result = re.findall("\d+",result_text[0].text)
        try:

            log.info(u"投诉表扬页面---断言内容---进行中第一个工单id:%s"%result)
            return result
        except:
            log.info(u"投诉表扬页面---断言内容---无工单")
            return None

    #进行中的内容
    def jbHomeComplaint_assert_conduct_content(self):
        result_text = self.find_element(self.assert_conduct_content_loc)
        try:
            log.info(u"投诉表扬页面---断言内容---进行中第一个工单内容:%s"%result_text[0].text)
            return result_text[0].text
        except:
            log.info(u"投诉表扬页面---断言内容---无工单")
            return None

#进行中的name(表扬或投诉)
    def jbHomeComplaint_assert_done_name(self):
        result_text = self.find_element(self.assert_done_name_loc)
        try:
            log.info(u"投诉表扬页面---断言内容---已完成第一个工单类型:%s"%result_text[0].text)
            return result_text[0].text
        except:
            log.info(u"投诉表扬页面---断言内容---无工单")
            return None

    #已完成的id
    def jbHomeComplaint_assert_done_id(self):
        result_text = self.find_element(self.assert_done_id_loc)
        result = re.findall("\d+",result_text[0].text)
        try:

            log.info(u"投诉表扬页面---断言内容---已完成第一个工单id:%s"%result)
            return result
        except:
            log.info(u"投诉表扬页面---断言内容---无工单")
            return None

    #已完成的内容(显示是手机号)
    def jbHomeComplaint_assert_done_content(self):
        result_text = self.find_element(self.assert_done_content_loc)
        try:
            log.info(u"投诉表扬页面---断言内容---已完成第一个工单内容:%s"%result_text[0].text)
            return result_text[0].text
        except:
            log.info(u"投诉表扬页面---断言内容---无工单")
            return None

class JbHomeVisitorPage(BasePage):
    """
    访客
    """
    click_visitor_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/top_recyclerview"]/android.widget.LinearLayout[7]'
    click_icon_loc="id=>com.hxdsw.brc:id/menuIV"
    click_Current1_loc="id=>com.hxdsw.brc:id/qr_code_access_btn"
    click_Current2_loc="id=>com.hxdsw.brc:id/face_code_access_btn_own"
    click_Current3_loc="id=>com.hxdsw.brc:id/face_code_access_btn_guest"
    assert_add_loc="id=>com.hxdsw.brc:id/houseInfo"
    click_newVisitor_loc="id=>com.hxdsw.brc:id/addVisitor"
    input_name_loc="id=>com.hxdsw.brc:id/name"
    input_num_loc="id=>com.hxdsw.brc:id/num"
    click_submit_loc="id=>com.hxdsw.brc:id/submit_ll"
    assert_name_loc="id=>com.hxdsw.brc:id/name"
    assert_num_loc="id=>com.hxdsw.brc:id/num"
    click_delete_loc="id=>com.hxdsw.brc:id/invalid"
    click_cancel_loc="id=>com.hxdsw.brc:id/left_button"
    click_sure_loc="id=>com.hxdsw.brc:id/right_button"

    #访客
    def jbHomeVisitor_click_visitor(self):
        self.click(self.click_visitor_loc)
        log.info(u"首页页面---点击访客")

    #右上角图标
    def jbHomeVisitor_click_icon(self):
        self.click(self.click_icon_loc)
        log.info("访客邀请页面---点击右上角图标")

    #二维码通行访客邀请
    def jbHomeVisitor_click_Current1(self):
        self.click(self.click_Current1_loc)
        log.info("访客邀请页面---点击二维码通行访客邀请")

    #人脸通行访客邀请(业主填写)
    def jbHomeVisitor_click_Current2(self):
        self.click(self.click_Current2_loc)
        log.info("访客邀请页面---人脸通行访客邀请(业主填写)")

    #人脸通行访客邀请(访客填写)
    def jbHomeVisitor_click_Current3(self):
        self.click(self.click_Current3_loc)
        log.info("访客邀请页面---人脸通行访客邀请(访客填写)")



    #地址
    def jbHomeVisitor_assert_add(self):
        result = self.text(self.assert_add_loc)
        log.info(u"访客邀请页面---断言内容---地址:%s"%result)

    #新建房客
    def jbHomeVisitor_click_newVisitor(self):
        self.click(self.click_newVisitor_loc)
        log.info(u"访客邀请页面---点击新建访客")

    #输入访客姓名
    def jbHomeVisitor_input_name(self,name):
        time.sleep(2)
        self.send_keys(self.input_name_loc,name)
        log.info(u"新邀请页面---输入访客姓名:%s"%name)

    #输入人数
    def jbHomeVisitor_input_num(self):
        result_num = random.randint(1,10)
        self.send_keys(self.input_num_loc,result_num)
        log.info(u"新邀请页面---输入人数")

    #点击生成通行证
    def jbHomeVisitor_click_submit(self):
        self.click(self.click_submit_loc)
        log.info(u"新邀请页面---点击生成通行证")


    def jbHomeVisitor_assert_name(self):
        result = self.text(self.assert_name_loc)
        log.info(u"新邀请页面---断言内容---访客姓名:%s"%result)

    def jbHomeVisitor_assert_num(self):
        result = self.text(self.assert_num_loc)
        log.info(u"新邀请页面---断言内容---访客人数:%s"%result)

    #作废
    def jbHomeVisitor_click_delete(self):
        self.click(self.click_delete_loc)
        log.info(u"新邀请页面---点击作废")

    #取消
    def jbHomeVisitor_click_cancel(self):
        self.click(self.click_cancel_loc)
        log.info(u"新邀请页面---邀请码点击取消")

    #确定
    def jbHomeVisitor_click_sure(self):
        self.click(self.click_sure_loc)
        log.info(u"新邀请页面---邀请码点击确定")


























