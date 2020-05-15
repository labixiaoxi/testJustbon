from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinancePaymentInquiry(BasePage):

    company_click = 'xpath=>//button[@class="btn-sm btn input-disable-select-btn"]'
    company_select = 'xpath=>//div[@id="searchPart"]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a'
    company_clear = 'xpath=>//button[@class="btn btn-sm input-disable-select-btn"]'
    project = 'xpath=>//button[@class="btn dropdown-toggle btn-default bs-placeholder"]'
    project_input = 'xpath=>//div[@class="bs-searchbox"]/input'
    project_select = 'xpath=>//span[contains(text(),"（成都）富丽城")]'
    resource = 'xpath=>//input[@name="resourceName"]'
    resource_select = 'xpath=>//div[@title="FL3-1-201"]'
    resouece_clear = 'xpath=>//div[@class="search-form-container"]/form/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]'
    account_input = 'xpath=>//input[@name="accountName"]'
    account_select = 'xpath=>//div[@title="物业服务费"]'
    account_clear = 'xpath=>//div[@class="search-form-container"]/form/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/button[1]'
    status_select = 'xpath=>//select[@name="status"]'
    show_more_click = 'xpath=>//i[@class="fa fa-chevron-down"]'
    pay_mode = 'xpath=>//select[@name="payMode"]'
    start_date = 'id=>accrualDateStartInput'
    today_click = 'id=>laydate_today'
    hours_click = 'xpath=>//ul[@id="laydate_hms"]/li[2]/input'
    minutes_click = 'xpath=>//ul[@id="laydate_hms"]/li[3]/input'
    seconds_click = 'xpath=>//ul[@id="laydate_hms"]/li[4]/input'
    num_select = 'xpath=>//div[@id="laydate_hmsno"]/span[1]'
    end_date = 'id=>accrualDateEndInput'
    date_clear = 'id=>laydate_clear'
    receiptnum_input = 'xpath=>//div[@id="searchPart"]/div[1]/div[1]/form/div[2]/div[4]/div[1]/input'
    paytype_click = 'xpath=>//select[@name="payType"]'
    money_input = 'xpath=>//input[@name="amountReal"]'
    search_click = 'xpath=>//button[@ng-click="search()"]'
    reset_click = 'xpath=>//button[@ng-click="reset()"]'
    receipt_long = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[%d]/div[1]/div[7]'
    money_text = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[%d]/div[1]/div[10]'
    paymode_text = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[%d]/div[1]/div[11]'
    status_text = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[%d]/div[1]/div[16]'
    nofixed_bill_print = 'xpath=>//div[@class="col-md-10"]/button[1]'
    nofixed_receipt_click = 'id=>nonQuotaInvoiceBtn'
    next_page_click = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[2]/div[1]/div[1]/button[3]'
    nofixed_receipt_select = 'xpath=>//div[@id="open_ticket_modal"]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]'
    recevicedate_click ='id=>receviceDateInput'
    nofixed_close = 'xpath=>//div[@id="open_ticket_modal"]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]'
    fixed_receipt_click = 'xpath=>//div[@class="col-md-10"]/button[3]'
    fixed_receipt_select = 'xpath=>//div[@id="quotaTicketTable"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]'
    fixed_close = 'xpath=>//div[@id="relate_ticket_modal"]/div[1]/div[1]/div[3]/button[1]'
    invoice_click = 'xpath=>//div[@class="col-md-10"]/button[11]'
    invoce_remark_input = 'xpath=>//div[@class="modal-body ng-scope"]/textarea'
    invoice_close = 'xpath=>//button[@class="btn btn-default btn-sm"]'


    def finance_company_click(self):
        self.click(self.company_click)
        log.info(u'实收查询页面--点击组织机构')
        sleep(0.5)
        self.click(self.company_select)
        log.info(u'实收查询页面--选择组织机构')
        sleep(0.5)
        self.click(self.company_clear)
        log.info(u'实收查询页面--清除组织机构')
        sleep(0.5)

    def finance_project_select(self):
        self.click(self.project)
        log.info(u'实收查询页面--点击项目名称')
        sleep(0.5)
        self.send_keys(self.project_input, '富丽城')
        log.info(u'实收查询页面--输入项目名称')
        sleep(1.5)
        self.click(self.project_select)
        log.info(u'实收查询页面--选择项目')
        sleep(0.5)

    def finance_resource_select(self):
        self.send_keys(self.resource, 'FL3-1-201')
        log.info(u'实收查询页面--输入资源名称')
        sleep(1.5)
        self.click(self.resource_select)
        log.info(u'实收查询页面--选择资源')
        sleep(0.5)
        self.click(self.resouece_clear)
        sleep(0.5)

    def finance_account_select(self):
        self.send_keys(self.account_input,'物业服务')
        log.info(u'实收查询页面--输入计费科目')
        sleep(1.5)
        self.click(self.account_select)
        log.info(u'实收查询页面--选择计费科目')
        sleep(0.5)
        self.click(self.account_clear)
        sleep(0.5)

    def finance_status_select(self):
        self.click(self.status_select)
        log.info(u'实收查询页面--点击状态')
        sleep(0.5)
        self.select(self.status_select, 2)
        log.info(u'实收查询页面--选择退费中状态')
        sleep(0.5)
        self.select(self.status_select, 3)
        log.info(u'实收查询页面--选择作废状态')
        sleep(0.5)
        self.select(self.status_select, 1)
        log.info(u'实收查询页面--选择正常状态')
        sleep(0.5)

    def finance_showmore_click(self):
        self.click(self.show_more_click)
        log.info(u'实收查询页面--显示更多查询条件')
        sleep(0.5)

    def finance_paymode_select(self):
        self.click(self.pay_mode)
        log.info(u'实收查询页面--点击付款方式')
        sleep(0.5)
        self.select(self.pay_mode, 2)
        log.info(u'实收查询页面--选择付款方式：APP支付-银联')
        sleep(0.5)
        # self.select(self.pay_mode, 3)
        # log.info(u'实收查询页面--选择付款方式：折扣')
        # sleep(0.5)
        # self.select(self.pay_mode, 4)
        # log.info(u'实收查询页面--选择付款方式：抹零')
        # sleep(0.5)
        # self.select(self.pay_mode, 5)
        # log.info(u'实收查询页面--选择付款方式：职能代收')
        # sleep(0.5)
        # self.select(self.pay_mode, 6)
        # log.info(u'实收查询页面--选择付款方式：关联交易')
        # sleep(0.5)
        # self.select(self.pay_mode, 7)
        # log.info(u'实收查询页面--选择付款方式：二维码支付')
        # sleep(0.5)
        # self.select(self.pay_mode, 8)
        # log.info(u'实收查询页面--选择付款方式：抵扣卡充值')
        # sleep(0.5)
        # self.select(self.pay_mode, 9)
        # log.info(u'实收查询页面--选择付款方式：现金')
        # sleep(0.5)
        # self.select(self.pay_mode, 10)
        # log.info(u'实收查询页面--选择付款方式：银行托收')
        # sleep(0.5)
        # self.select(self.pay_mode, 11)
        # log.info(u'实收查询页面--选择付款方式：POS单')
        # sleep(0.5)
        # self.select(self.pay_mode, 12)
        # log.info(u'实收查询页面--选择付款方式：抵扣券')
        # sleep(0.5)
        # self.select(self.pay_mode, 13)
        # log.info(u'实收查询页面--选择付款方式：转账收入')
        # sleep(0.5)
        # self.select(self.pay_mode, 14)
        # log.info(u'实收查询页面--选择付款方式：减免')
        # sleep(0.5)
        # self.select(self.pay_mode, 15)
        # log.info(u'实收查询页面--选择付款方式：换票未收现')
        # sleep(0.5)
        # self.select(self.pay_mode, 17)
        # log.info(u'实收查询页面--选择付款方式：其他')
        # sleep(0.5)
        # self.select(self.pay_mode, 16)
        # log.info(u'实收查询页面--选择付款方式：预付款抵扣')
        # sleep(0.5)
        self.select(self.pay_mode, 1)
        log.info(u'实收查询页面--选择付款方式：APP支付')
        sleep(0.5)

    def finance_startdate_select(self):
        self.click(self.start_date)
        log.info(u'实收查询页面--选择开始时间')
        sleep(0.5)
        self.click(self.date_clear)
        log.info(u'实收查询页面--清空开始时间')
        sleep(0.5)

    def finance_enddate_select(self):
        self.click(self.end_date)
        log.info(u'实收查询页面--选择截止时间')
        sleep(0.5)
        self.click(self.today_click)
        log.info(u'实收查询页面--选择今天')
        sleep(0.5)

    def finance_receipt_input(self):
        self.send_keys(self.receiptnum_input,12345678)
        log.info(u'实收查询页面--输入票据号码')
        sleep(0.5)
        self.clear(self.receiptnum_input)
        log.info(u'实收查询页面--清空票据号码')
        sleep(0.5)

    def finance_paytype_select(self):
        self.click(self.paytype_click)
        log.info(u'实收查询页面--点击缴费类型')
        sleep(0.5)
        self.select(self.paytype_click, 2)
        log.info(u'实收查询页面--选择缴费类型：划账')
        sleep(0.5)
        # self.select(self.paytype_click, 3)
        # log.info(u'实收查询页面--选择缴费类型：退款')
        # sleep(0.5)
        # self.select(self.paytype_click, 4)
        # log.info(u'实收查询页面--选择缴费类型：欠费调账')
        # sleep(0.5)
        # self.select(self.paytype_click, 5)
        # log.info(u'实收查询页面--选择缴费类型：充值')
        # sleep(0.5)
        # self.select(self.paytype_click, 6)
        # log.info(u'实收查询页面--选择缴费类型：转账')
        # sleep(0.5)
        # self.select(self.paytype_click, 7)
        # log.info(u'实收查询页面--选择缴费类型：托收')
        # sleep(0.5)
        # self.select(self.paytype_click, 8)
        # log.info(u'实收查询页面--选择缴费类型：APP支付')
        # sleep(0.5)
        # self.select(self.paytype_click, 9)
        # log.info(u'实收查询页面--选择缴费类型：滞纳金减免')
        # sleep(0.5)
        # self.select(self.paytype_click, 10)
        # log.info(u'实收查询页面--选择缴费类型：折扣')
        # sleep(0.5)
        # self.select(self.paytype_click, 11)
        # log.info(u'实收查询页面--选择缴费类型：抹零')
        # sleep(0.5)
        self.select(self.paytype_click, 0)
        log.info(u'实收查询页面--选择缴费类型：默认')
        sleep(0.5)

    def finance_money_input(self):
        self.send_keys(self.money_input, 100)
        log.info(u'实收查询页面--输入金额')
        sleep(0.5)
        self.clear(self.money_input)
        log.info(u'实收查询页面--清除金额')
        sleep(0.5)

    def finance_search_click(self):
        self.click(self.search_click)
        log.info(u'实收查询页面--点击查询')
        sleep(3)

    def finance_nofixed_make(self):
        for i in range(1, 31):
            l = (self.receipt_long % i)                                                 #获取票据号有值
            s = self.find_element(l).text                                               #获取票据号
            if len(s) == 0:
                ll = self.find_element(self.paymode_text % i).text                      #获取付款方式
                mm = self.find_element(self.money_text % i).text                        #获取金额
                mmf = float(mm)
                if len(ll) != 0 and mmf > 0:
                    self.click(l)
                    log.info(u'实收查询页面--选择实收信息')
                    sleep(0.5)
                    break

    def finance_nofixed_click(self):
        self.click(self.nofixed_bill_print)
        log.info(u'实收查询页面--点击非定额票据')
        sleep(12)

    def finance_nofixed_select(self):
        self.click(self.nofixed_receipt_click)
        log.info(u'实收查询页面--展开非定额票据')
        sleep(4)
        self.click(self.nofixed_receipt_select)
        log.info(u'实收查询页面--选择非定额票据')
        sleep(0.5)

    def finance_recevicedate_select(self):
        self.click(self.recevicedate_click)
        log.info(u'实收查询页面--点击开票日期')
        sleep(0.5)
        self.click(self.today_click)
        log.info(u'实收查询页面--选择今天')
        sleep(0.5)

    def finance_nofixed_close(self):
        self.click(self.nofixed_close)
        log.info(u'实收查询页面--点击关闭')
        sleep(1)

    def finance_fixed_click(self):
        self.click(self.fixed_receipt_click)
        log.info(u'实收查询页面--点击补开定额票据')
        sleep(10)

    def finance_fixed_select(self):
        self.click(self.fixed_receipt_select)
        log.info(u'实收查询页面--选择定额票据')
        sleep(0.5)

    def finance_fixed_close(self):
        self.click(self.fixed_close)
        log.info(u'实收查询页面--点击取消')
        sleep(0.5)

    def finance_invoice_click(self):
        self.click(self.invoice_click)
        log.info(u'实收查询页面--点击补开电子收据')
        sleep(2)

    def finance_invoice_remark_input(self):
        self.send_keys(self.invoce_remark_input, '补开电子收据备注')
        log.info(u'实收查询页面--输入电子收据备注')
        sleep(0.5)

    def finance_invoice_close(self):
        self.click(self.invoice_close)
        log.info(u'实收查询页面--点击关闭')
        sleep(0.5)