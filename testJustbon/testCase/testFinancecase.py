# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 16:03
from pageObject.financeLoginPage import  FinanceLoginPage
from pageObject.financePlatformHomePage import FinancePlatformHomePage
from pageObject.financeHomePage import FinanceHomePage
from pageObject.financeAccountManagementPage import FinanceAccountManagement
from pageObject.financeCustormerPaymentPage import FinanceCustormerPayment
from pageObject.financeCustormerChargePage import FinancenCustormerCharge
from pageObject.financeCustormerRefundPage import FinanceCustormerRefund
from pageObject.financePaymentInquiryPage import FinancePaymentInquiry
from pageObject.financePaymoneyApplyPage import FinancePaymoneyApply
from pageObject.financeReceiptManagementPage import FinanceReceiptTypeManagement
from pageObject.financeReceiptEntryPage import FinanceReceiptEntry
from pageObject.financeReceiptUsePage import FinanceReceiptUse
from pageObject.financeReceiptOneCancellationPage import FinanceOneCancellation
from pageObject.financeReceiptTwoCancellationPage import FinanceTwoCancellation
from pageObject.financeReceiptBackPage import FinanceReceiptBack
from pageObject.financeReceiptRemovePage import FinanceReceiptRemove
from pageObject.financeReceiptCancelPage import FinanceReceiptCancel
from pageObject.financeInvoiceCountPage import FinanceInvoiceCount
from pageObject.financeReceiptCountPage import FinanceReceiptCount
from pageObject.financeHoldCountPage import FinanceHoldCount
from pageObject.financeManagerRemovePage import FinanceManagerRemove
from unittest import TestCase
from selenium import webdriver
import unittest


class TestLoginCase(TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.data = []
        cls.lp = FinanceLoginPage(cls.driver)
        cls.hp = FinanceHomePage(cls.driver)
        cls.fhp = FinancePlatformHomePage(cls.driver)
        cls.am = FinanceAccountManagement(cls.driver)
        cls.cp = FinanceCustormerPayment(cls.driver)
        cls.cc = FinancenCustormerCharge(cls.driver)
        cls.cr = FinanceCustormerRefund(cls.driver)
        cls.pp = FinancePaymentInquiry(cls.driver)
        cls.pa = FinancePaymoneyApply(cls.driver)
        cls.rtm = FinanceReceiptTypeManagement(cls.driver)
        cls.rep = FinanceReceiptEntry(cls.driver)
        cls.ru = FinanceReceiptUse(cls.driver)
        cls.ocp = FinanceOneCancellation(cls.driver)
        cls.tcp = FinanceTwoCancellation(cls.driver)
        cls.rb = FinanceReceiptBack(cls.driver)
        cls.rm = FinanceReceiptRemove(cls.driver)
        cls.rc = FinanceReceiptCancel(cls.driver)
        cls.ic = FinanceInvoiceCount(cls.driver)
        cls.rco = FinanceReceiptCount(cls.driver)
        cls.hc = FinanceHoldCount(cls.driver)
        cls.mr = FinanceManagerRemove(cls.driver)

    def test_a_loginpage_001(self):
        """登录——登录进入"""
        self.lp.get_url('https://i.justbon.com/')
        self.lp.finance_input_name()
        self.lp.finance_input_password()
        self.lp.finance_click_login()
        self.fhp.finance_click_platform_iknow()
        self.fhp.finance_click_finance()
        self.fhp.finance_click_iknow()

    def test_d_accountmanagementpage_002(self):
        """计费管理——批量计费管理"""
        self.hp.finance_click_account_management()
        self.hp.finance_click_batch_charging_management()

    def test_d_accountmanagementpage_003(self):
        """批量计费管理——选择项目"""
        self.am.finance_click_project()
        self.am.finance_input_project()
        self.am.finance_click_project_select()

    def test_d_accountmanagementpage_004(self):
        """批量计费管理——选择资源"""
        self.am.finance_input_resource()
        self.am.finance_click_resource()

    def test_d_accountmanagementpage_005(self):
        """批量计费管理——选择计费类型"""
        self.am.finance_select_charge_type()

    def test_d_accountmanagementpage_006(self):
        """批量计费管理——选择费用来源"""
        self.am.finance_click_source()

    def test_d_accountmanagementpage_007(self):
        """批量计费管理——选择计费科目"""
        self.am.finance_click_account()
        self.am.finance_click_type()

    def test_d_accountmanagementpage_008(self):
        """批量计费管理——填写金额"""
        self.am.finance_input_money()

    def test_d_accountmanagementpage_009(self):
        """批量计费管理——选择起止时间"""
        self.am.finance_click_startdate()
        self.am.finance_click_enddate()

    def test_d_accountmanagementpage_010(self):
        """批量计费管理——填写备注"""
        self.am.finance_input_remark()

    def test_d_accountmanagementpage_011(self):
        """批量计费管理——计费"""
        self.am.finance_click_cost()

    def test_d_accountmanagementpage_012(self):
        """批量计费管理——取消"""
        self.am.finance_click_cancel()

    def test_d_accountmanagementpage_013(self):
        """批量计费管理——返回首页"""
        self.cp.finance_click_homepage()

    def test_e_custormerpaymentchargepage_001(self):
        """实收管理——客户收费"""
        self.cp.finance_menu()
        self.cp.finance_click_payment_management()
        self.cp.finance_click_custormer_charge()

    def test_e_custormerpaymentchargepage_002(self):
        """客户收费——选择项目"""
        self.cc.finance_click_project()
        self.cc.finance_input_project()
        self.cc.finance_select_project()

    def test_e_custormerpaymentchargepage_003(self):
        """客户收费——选择资源"""
        self.cc.finance_input_resource()
        self.cc.finance_select_resource()

    def test_e_custormerpaymentchargepage_004(self):
        """客户收费——选择欠费"""
        self.cc.finance_select_fee()

    def test_e_custormerpaymentchargepage_005(self):
        """客户收费——选择支付方式"""
        self.cc.finance_click_payment_type()
        self.cc.finance_select_payment_type()

    def test_e_custormerpaymentchargepage_006(self):
        """客户收费——选择是否开票"""
        self.cc.finance_click_receipt()
        self.cc.finance_select_receipt()

    def test_e_custormerpaymentchargepage_007(self):
        """客户收费——选择是否收取滞纳金"""
        self.cc.finance_click_penalty()
        self.cc.finance_select_penalty()

    def test_e_custormerpaymentchargepage_008(self):
        """客户收费——选择票据类型"""
        self.cc.finance_click_fixed()
        self.cc.finance_click_nofixed()
        self.cc.finance_click_invoice()

    def test_e_custormerpaymentchargepage_009(self):
        """客户收费——选择收费时间"""
        self.cc.finance_click_time()
        self.cc.finance_select_time()

    def test_e_custormerpaymentchargepage_010(self):
        """客户收费——填写收费备注"""
        self.cc.finance_input_remark()

    def test_e_custormerpaymentchargepage_011(self):
        """客户收费——填写电子收据备注"""
        self.cc.finance_input_inivoice_remark()

    def test_e_custormerpaymentchargepage_012(self):
        """客户收费——返回首页"""
        self.cp.finance_click_homepage()

    def test_f_custormerrefundpage_001(self):
        """实收管理——客服退费"""
        self.cp.finance_click_payment_management()
        self.cp.finance_click_custormer_refund()
        self.cp.finance_menu()

    def test_f_custormerrefundpage_002(self):
        """客服退费——选择项目"""
        self.cr.finance_click_project()
        self.cr.finance_input_project()
        self.cr.finance_select_project()

    def test_f_custormerrefundpage_003(self):
        """客服退费——选择资源"""
        self.cr.finance_input_resource()
        self.cr.finance_select_resource()

    def test_f_custormerrefundpage_004(self):
        """客服退费——选择科目"""
        self.cr.finance_account_input()
        self.cr.finance_account_select()

    def test_f_custormerrefundpage_005(self):
        """客服退费——选择起止时间"""
        self.cr.finance_starttime_select()
        self.cr.finance_endtime_select()

    def test_f_custormerrefundpage_006(self):
        """客服退费——查询"""
        self.cr.finance_refund_search()

    def test_f_custormerrefundpage_007(self):
        """客服退费——重置"""
        self.cr.finance_reset_click()

    def test_f_custormerrefundpage_008(self):
        """客服退费——选择退费数据"""
        self.cr.finance_refund_select()

    def test_f_custormerrefundpage_009(self):
        """客服退费——退费按钮"""
        self.cr.finance_refundbutton_click()

    def test_f_custormerrefundpage_010(self):
        """客服退费——选择退费方式"""
        self.cr.finance_refundtype_click()
        self.cr.finance_refundtype_select()

    def test_f_custormerrefundpage_011(self):
        """客服退费——填写退滞纳金额"""
        self.cr.finance_penalty_input()

    def test_f_custormerrefundpage_012(self):
        """客服退费——选择是否恢复欠费"""
        self.cr.finance_arrear_click()
        self.cr.finance_arrear_select()

    def test_f_custormerrefundpage_013(self):
        """客服退费——填写退费金额"""
        self.cr.finance_money_input()

    def test_f_custormerrefundpage_014(self):
        """客服退费——填写退费备注"""
        self.cr.finance_refund_remark()

    def test_f_custormerrefundpage_015(self):
        """客服退费——关闭退费弹窗"""
        self.cr.finance_refund_close()

    def test_f_custormerrefundpage_016(self):
        """客服退费——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_g_paymentinquiry_001(self):
        """实收管理——实收查询"""
        self.cp.finance_click_payment_management()
        self.cp.finance_click_payment_inquiry()
        self.cp.finance_menu()

    def test_g_paymentinquiry_002(self):
        """实收查询——选择项目"""
        self.pp.finance_company_click()
        self.pp.finance_project_select()

    def test_g_paymentinquiry_003(self):
        """实收查询——选择资源"""
        self.pp.finance_resource_select()

    def test_g_paymentinquiry_004(self):
        """实收查询——选择状态"""
        self.pp.finance_status_select()

    def test_g_paymentinquiry_005(self):
        """实收查询——选择科目"""
        self.pp.finance_account_select()

    def test_g_paymentinquiry_006(self):
        """实收查询——更多查询条件"""
        self.pp.finance_showmore_click()

    def test_g_paymentinquiry_007(self):
        """实收查询——选择支付方式"""
        self.pp.finance_paymode_select()

    def test_g_paymentinquiry_008(self):
        """实收查询——选择起止时间"""
        self.pp.finance_startdate_select()
        self.pp.finance_enddate_select()

    def test_g_paymentinquiry_009(self):
        """实收查询——填写票据号码"""
        self.pp.finance_receipt_input()

    def test_g_paymentinquiry_010(self):
        """实收查询——选择缴费类型"""
        self.pp.finance_paytype_select()

    def test_g_paymentinquiry_011(self):
        """实收查询——填写金额"""
        self.pp.finance_money_input()

    def test_g_paymentinquiry_012(self):
        """实收查询——查询"""
        self.pp.finance_search_click()

    def test_g_paymentinquiry_013(self):
        """实收查询——补开定额票"""
        self.pp.finance_nofixed_make()
        self.pp.finance_nofixed_click()
        self.pp.finance_nofixed_select()
        self.pp.finance_recevicedate_select()
        self.pp.finance_nofixed_close()

    def test_g_paymentinquiry_014(self):
        """实收查询——非补开定额票"""
        self.pp.finance_fixed_click()
        self.pp.finance_fixed_select()
        self.pp.finance_fixed_close()

    def test_g_paymentinquiry_015(self):
        """实收查询——补开电子收据"""
        self.pp.finance_invoice_click()
        self.pp.finance_invoice_remark_input()
        self.pp.finance_invoice_close()

    def test_g_paymentinquiry_016(self):
        """实收查询——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_h_paymoney_001(self):
        """财务交款——交款申请"""
        self.cp.finance_click_paymoney_apply()
        self.cp.finance_click_pay_money()
        self.cp.finance_menu()

    def test_h_paymoney_002(self):
        """交款申请——选择项目"""
        self.pa.finance_project_click()

    def test_h_paymoney_003(self):
        """交款申请——填写备注"""
        self.pa.finance_remark_input()

    def test_h_paymoney_004(self):
        """交款申请——计费科目明细"""
        self.pa.finance_account_detail_click()

    def test_h_paymoney_005(self):
        """交款申请——计费科目汇总"""
        self.pa.finance_account_total_click()

    def test_h_paymoney_006(self):
        """交款申请——票据使用汇总"""
        self.pa.finance_receipt_total_click()

    def test_h_paymoney_007(self):
        """财务交款——票据基本明细"""
        self.pa.finance_detail_click()

    def test_h_paymoney_008(self):
        """交款申请——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_i_receipt_001(self):
        """票据管理——票据类型管理"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_click_receipt_type_management()
        self.cp.finance_menu()

    def test_i_receipt_002(self):
        """票据类型管理——票据类型结构树"""
        self.rtm.finance_receipttype_click()

    def test_i_receipt_003(self):
        """票据类型管理——增加"""
        self.rtm.finance_receipttype_add()
        self.rtm.finance_typename_input()
        self.rtm.finance_number_input()
        self.rtm.finance_sort_click()
        self.rtm.finance_amount_input()
        self.rtm.finance_cancel_click()

    def test_i_receipt_004(self):
        """票据类型管理——修改"""
        self.rtm.finance_status_get()
        self.rtm.finance_receipttype_modify()
        self.rtm.finance_typename_modify()
        self.rtm.finance_number_modify()
        self.rtm.finance_sort_modify()
        self.rtm.finance_modify_cancel_click()

    def test_i_receipt_005(self):
        """票据类型管理——删除"""
        self.rtm.finance_remove_click()
        self.rtm.finance_close()

    def test_i_receipt_006(self):
        """票据类型管理——禁用"""
        self.rtm.finance_forbidden_click()
        self.rtm.finance_close()

    def test_i_receipt_007(self):
        """票据类型管理——启用"""
        self.rtm.finance_use_click()
        self.rtm.finance_close()

    def test_i_receipt_008(self):
        """票据类型管理——名称栏"""
        self.rtm.finance_nametext_input()

    def test_i_receipt_009(self):
        """票据类型管理——编码栏"""
        self.rtm.finance_numbertext_input()

    def test_i_receipt_010(self):
        """票据类型管理——选择分类"""
        self.rtm.finance_sort_select()

    def test_i_receipt_011(self):
        """票据类型管理——查询"""
        self.rtm.finance_search_click()

    def test_i_receipt_012(self):
        """票据类型管理——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_j_receipt_001(self):
        """票据管理——申请票据入库"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_click_receipt_entry()
        self.cp.finance_menu()

    def test_j_receipt_002(self):
        """申请票据入库——项目选择"""
        self.rep.finance_range_click()
        self.rep.finance_project_click()

    def test_j_receipt_003(self):
        """申请票据入库——填入申请原因"""
        self.rep.finance_remark_input()

    def test_j_receipt_004(self):
        """申请票据入库——添加"""
        self.rep.finance_add_click()

    def test_j_receipt_005(self):
        """申请票据入库——票据类型"""
        self.rep.finance_type_click()
        self.rep.finance_type_input()
        self.rep.finance_typename_click()

    def test_j_receipt_006(self):
        """申请票据入库——起始号码"""
        self.rep.finance_startno_click()
        self.rep.finance_startno_input()

    def test_j_receipt_007(self):
        """申请票据入库——结束号码"""
        self.rep.finance_endno_click()
        self.rep.finance_endno_input()

    def test_j_receipt_008(self):
        """申请票据入库——断言号码"""
        self.assertEqual(self.rep.finance_sno_input(), self.rep.finance_number_count())

    def test_j_receipt_009(self):
        """申请票据入库——选择票据类型数据"""
        self.rep.finance_data_select()

    def test_j_receipt_010(self):
        """申请票据入库——删除"""
        self.rep.finance_remove_click()

    def test_j_receipt_011(self):
        """申请票据入库——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_k_receipt_001(self):
        """票据管理——申请票据领用"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_click_receipt_use()
        self.cp.finance_menu()

    def test_k_receipt_002(self):
        """申请票据领用——项目选择"""
        self.ru.finance_range_click()
        self.ru.finance_project_click()

    def test_k_receipt_003(self):
        """申请票据领用——填入申请原因"""
        self.ru.finance_remark_input()

    def test_k_receipt_004(self):
        """申请票据领用——添加"""
        self.ru.finance_add_click()

    def test_k_receipt_005(self):
        """申请票据领用——票据类型"""
        self.ru.finance_type_click()
        self.ru.finance_type_input()
        self.ru.finance_typename_click()

    def test_k_receipt_006(self):
        """申请票据领用——申请数量"""
        self.ru.finance_count_click()
        self.ru.finance_count_input()

    def test_k_receipt_007(self):
        """申请票据领用——删除"""
        self.ru.finance_remove_click()

    def test_k_receipt_008(self):
        """申请票据领用——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_l_receipt_001(self):
        """票据管理——票据一级核销"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_click_one_cancellation()
        self.cp.finance_menu()

    def test_l_receipt_002(self):
        """票据一级核销——选择项目"""
        self.ocp.finance_project_cancel_click()

    def test_l_receipt_003(self):
        """票据一级核销——填写申请原因"""
        self.ocp.finance_remark_input()

    def test_l_receipt_004(self):
        """票据一级核销——添加"""
        self.ocp.finance_add_click()

    def test_l_receipt_005(self):
        """票据一级核销——选择数据"""
        self.ocp.finance_data_a_click()

    def test_l_receipt_006(self):
        """票据一级核销——确定"""
        self.ocp.finance_submit_click()

    def test_l_receipt_007(self):
        """票据一级核销——选择已选择数据"""
        self.ocp.finance_data_b_click()

    def test_l_receipt_008(self):
        """票据一级核销——添加"""
        self.ocp.finance_add_click()

    def test_l_receipt_009(self):
        """票据一级核销——断言数据类型名称"""
        self.assertEqual(self.ocp.finance_type_a_text(), self.ocp.finance_type_b_text())

    def test_l_receipt_010(self):
        """票据一级核销——断言票据状态"""
        self.assertEqual(self.ocp.finance_status_a_text(), self.ocp.finance_status_b_text())

    def test_l_receipt_011(self):
        """票据一级核销——断言起始号码"""
        self.assertEqual(self.ocp.finance_startno_a_text(), self.ocp.finance_startno_b_text())

    def test_l_receipt_012(self):
        """票据一级核销——断言结束号码"""
        self.assertEqual(self.ocp.finance_endno_a_text(), self.ocp.finance_endno_b_text())

    def test_l_receipt_013(self):
        """票据一级核销——断言票据数量"""
        self.assertEqual(self.ocp.finance_count_a_text(), self.ocp.finance_count_b_text())

    def test_l_receipt_014(self):
        """票据一级核销——取消"""
        self.ocp.finance_cancel_click()

    def test_l_receipt_015(self):
        """票据一级核销——删除"""
        self.ocp.finance_remove_click()

    def test_l_receipt_016(self):
        """票据一级核销——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_m_receipt_001(self):
        """票据管理——票据二级核销"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_click_two_cancellation()
        self.cp.finance_menu()

    def test_m_receipt_002(self):
        """票据二级核销——填写申请原因"""
        self.tcp.finance_remark_input()

    def test_m_receipt_003(self):
        """票据二级核销——添加"""
        self.tcp.finance_add_click()

    def test_m_receipt_004(self):
        """票据二级核销——取消"""
        self.tcp.finance_cancel_click()

    def test_m_receipt_005(self):
        """票据二级核销——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_n_receipt_001(self):
        """票据管理——申请票据退回"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_receipt_back()
        self.cp.finance_menu()

    def test_n_receipt_002(self):
        """申请票据退回——项目选择"""
        self.rb.finance_range_click()
        self.rb.finance_project_click()

    def test_n_receipt_003(self):
        """申请票据退回——填入申请原因"""
        self.rb.finance_remark_input()

    def test_n_receipt_004(self):
        """申请票据退回——添加"""
        self.rb.finance_add_click()

    def test_n_receipt_005(self):
        """申请票据退回——取消"""
        self.rb.finance_cancel_click()

    def test_n_receipt_006(self):
        """申请票据退回——删除"""
        self.rb.finance_remove_click()

    def test_n_receipt_007(self):
        """申请票据退回——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_o_receipt_001(self):
        """票据管理——申请票据删除"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_receipt_remove()
        self.cp.finance_menu()

    def test_o_receipt_002(self):
        """申请票据删除——项目选择"""
        self.rm.finance_range_click()
        self.rm.finance_project_click()

    def test_o_receipt_003(self):
        """申请票据删除——添加"""
        self.rm.finance_add_click()

    def test_o_receipt_004(self):
        """申请票据删除——取消"""
        self.rm.finance_cancel_click()

    def test_o_receipt_005(self):
        """申请票据删除——删除"""
        self.rm.finance_remove_click()

    def test_o_receipt_006(self):
        """申请票据删除——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_p_receipt_001(self):
        """票据管理——票据作废/恢复"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_receipt_cancel()
        self.cp.finance_menu()

    def test_p_receipt_002(self):
        """票据作废/恢复——输入票据类型"""
        self.rc.finance_type_input()

    def test_p_receipt_003(self):
        """票据作废/恢复——选择票据类型"""
        self.rc.finance_type_click()

    def test_p_receipt_004(self):
        """票据作废/恢复——输入起始号码"""
        self.rc.finance_startno_input()

    def test_p_receipt_005(self):
        """票据作废/恢复——输入截止号码"""
        self.rc.finance_endno_input()

    def test_p_receipt_006(self):
        """票据作废/恢复——输入备注"""
        self.rc.finance_remark_input()

    def test_p_receipt_007(self):
        """票据作废/恢复——点击恢复"""
        self.rc.finance_resume_click()

    def test_p_receipt_008(self):
        """票据作废/恢复——取消"""
        self.rc.finance_cancel_click()

    def test_p_receipt_009(self):
        """票据作废/恢复——点击作废"""
        self.rc.finance_nullify_click()

    def test_p_receipt_010(self):
        """票据作废/恢复——取消"""
        self.rc.finance_cancel_click()

    def test_p_receipt_011(self):
        """票据作废/恢复——查看收费记录"""
        self.rc.finance_cat_click()

    def test_p_receipt_012(self):
        """票据作废/恢复——获取票据关联收费数据成功"""
        self.rc.finance_endno_input()

    def test_p_receipt_013(self):
        """票据作废/恢复——点击票据明细"""
        self.rc.finance_detail_click()

    def test_p_receipt_014(self):
        """票据作废/恢复——点击关闭"""
        self.rc.finance_close_click()

    def test_p_receipt_015(self):
        """票据作废/恢复——点击重置"""
        self.rc.finance_reset_click()

    def test_p_receipt_016(self):
        """票据作废/恢复——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_q_receipt_001(self):
        """票据管理——电子收据统计"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_invoice_count()
        self.cp.finance_menu()

    def test_q_receipt_002(self):
        """电子收据统计——选择组织机构"""
        self.ic.finance_company_click()

    def test_q_receipt_003(self):
        """电子收据统计——选择项目"""
        self.ic.finance_project_click()

    def test_q_receipt_004(self):
        """电子收据统计——输入起始号码"""
        self.ic.finance_startno_a_input()

    def test_q_receipt_005(self):
        """电子收据统计——输入结束号码"""
        self.ic.finance_endno_a_input()

    def test_q_receipt_006(self):
        """电子收据统计——查询"""
        self.ic.finance_search_a_click()

    def test_q_receipt_007(self):
        """电子收据统计——重置"""
        self.ic.finance_reset_a_click()

    def test_q_receipt_008(self):
        """电子收据统计——选择数据"""
        self.ic.finance_data_a_click()

    def test_q_receipt_009(self):
        """电子收据统计——查看明细"""
        self.ic.finance_catdetail_a_click()

    def test_q_receipt_010(self):
        """电子收据统计——选择资源"""
        self.ic.finance_resource_click()

    def test_q_receipt_011(self):
        """电子收据统计——选择开票时间起"""
        self.ic.finance_starttime_click()

    def test_q_receipt_012(self):
        """电子收据统计——选择开票时间止"""
        self.ic.finance_endtime_click()

    def test_q_receipt_013(self):
        """电子收据统计——输入票据起始号码"""
        self.ic.finance_startno_b_input()

    def test_q_receipt_014(self):
        """电子收据统计——输入票据结束号码"""
        self.ic.finance_endno_b_input()

    def test_q_receipt_015(self):
        """电子收据统计——展开更多"""
        self.ic.finance_more_click()

    def test_q_receipt_016(self):
        """电子收据统计——选择状态"""
        self.ic.finance_status_select()

    def test_q_receipt_017(self):
        """电子收据统计——查询"""
        self.ic.finance_search_b_click()

    def test_q_receipt_018(self):
        """电子收据统计——重置"""
        self.ic.finance_reset_b_click()

    def test_q_receipt_019(self):
        """电子收据统计——选择数据"""
        self.ic.finance_data_b_click()

    def test_q_receipt_020(self):
        """电子收据统计——查看明细"""
        self.ic.finance_catdetail_b_click()

    def test_q_receipt_022(self):
        """电子收据统计——获取收费数据"""
        self.ic.finance_data_get()

    def test_q_receipt_023(self):
        """电子收据统计——点击票据明细"""
        self.ic.finance_detail_click()

    def test_q_receipt_024(self):
        """电子收据统计——点击电子票据"""
        self.ic.finance_invoice_click()

    def test_q_receipt_025(self):
        """电子收据统计——点击退款明细"""
        self.ic.finance_refund_click()

    def test_q_receipt_026(self):
        """电子收据统计——点击关闭"""
        self.ic.finance_close_click()

    def test_q_receipt_027(self):
        """电子收据统计——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_r_receipt_001(self):
        """票据管理——票据段统计信息"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_receipt_count()
        self.cp.finance_menu()

    def test_r_receipt_002(self):
        """票据段统计信息——选择票据类型"""
        self.rco.finance_type_click()

    def test_r_receipt_003(self):
        """票据段统计信息——选择项目"""
        self.rco.finance_project_click()

    def test_r_receipt_004(self):
        """票据段统计信息——输入票据起始号码"""
        self.rco.finance_startno_input()

    def test_r_receipt_005(self):
        """票据段统计信息——输入票据结束号码"""
        self.rco.finance_endno_input()

    def test_r_receipt_006(self):
        """票据段统计信息——查询"""
        self.rco.finance_search_click()

    def test_r_receipt_007(self):
        """票据段统计信息——重置"""
        self.rco.finance_reset_click()

    def test_r_receipt_008(self):
        """票据段统计信息——选择数据"""
        self.rco.finance_data_a_click()

    def test_r_receipt_009(self):
        """票据段统计信息——查看明细"""
        self.rco.finance_catdetail_a_click()

    def test_r_receipt_010(self):
        """票据段统计信息——选择数据"""
        self.rco.finance_data_b_click()

    def test_r_receipt_011(self):
        """票据段统计信息——查看详情"""
        self.rco.finance_catdetail_b_click()

    def test_r_receipt_012(self):
        """票据段统计信息——获取数据"""
        self.rco.finance_data_get()

    def test_r_receipt_013(self):
        """票据段统计信息——点击票据明细"""
        self.rco.finance_detail_click()

    def test_r_receipt_014(self):
        """票据段统计信息——关闭窗口"""
        self.rco.finance_close_click()

    def test_r_receipt_015(self):
        """票据段统计信息——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_s_receipt_001(self):
        """票据管理——持有票据统计"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_hold_count()
        self.cp.finance_menu()

    def test_s_receipt_002(self):
        """持有票据统计——选择票据持有人"""
        self.hc.finance_user_input()

    def test_s_receipt_003(self):
        """持有票据统计——选择票据类型"""
        self.hc.finance_type_input()

    def test_s_receipt_004(self):
        """持有票据统计——选择状态"""
        self.hc.finance_status_select()

    def test_s_receipt_005(self):
        """持有票据统计——查询"""
        self.hc.finance_search_click()

    def test_s_receipt_006(self):
        """持有票据统计——重置"""
        self.hc.finance_reset_click()

    def test_s_receipt_007(self):
        """持有票据统计——获取票据信息"""
        self.hc.finance_data_get()

    def test_s_receipt_008(self):
        """持有票据统计——获取票据类型和票据号码保存变量"""
        data = self.hc.finance_data_write()
        self.data.append(data[0])
        self.data.append(data[1])

    def test_s_receipt_009(self):
        """持有票据统计——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()

    def test_t_receipt_001(self):
        """票据管理——票管删除票据"""
        self.cp.finance_click_receipt_management()
        self.cp.finance_manager_remove()
        self.cp.finance_menu()

    def test_t_receipt_002(self):
        """票管删除票据——输入票据类型"""
        self.mr.finance_type_click(self.data[0])

    def test_t_receipt_003(self):
        """票管删除票据——输入票据起始号码"""
        self.mr.finance_startno_input(self.data[1])

    def test_t_receipt_004(self):
        """票管删除票据——输入票据结束号码"""
        self.mr.finance_endno_input(self.data[1])

    def test_t_receipt_005(self):
        """票管删除票据——查询"""
        self.mr.finance_search_click()

    def test_t_receipt_006(self):
        """票管删除票据——删除"""
        self.mr.finance_remove_click()

    def test_t_receipt_007(self):
        """票管删除票据——取消"""
        self.mr.finance_cancel_click()

    def test_t_receipt_008(self):
        """票管删除票据——重置"""
        self.mr.finance_reset_click()

    def test_t_receipt_009(self):
        """票管删除票据——返回首页"""
        self.cp.finance_menu()
        self.cp.finance_click_homepage()


if __name__ == '__main__':
        unittest.main()