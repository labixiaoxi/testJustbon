from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()

class FinancenCustormerCharge(BasePage):

    project = 'xpath=>//span[@class="select2-selection__rendered"]'
    project_input = 'xpath=>//input[@class="select2-search__field"]'
    project_select = 'xpath=>//li[contains(text(),"（成都）香境·香碧歌")]'
    resource = 'xpath=>//input[@name="resourceName"]'
    resource_select = 'xpath=>//div[@title="1-1-3"]'
    fee_select = 'xpath=>//div[@class="portlet-body"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]'
    payment_type_select = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[2]/form//div[1]/div[1]/div[1]/select'
    receipt_write_select ='xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[2]/form//div[1]/div[2]/div[1]/select'
    penalty_select = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[2]/form//div[1]/div[3]/div[1]/select'
    fixedbill_select = 'xpath=>//div[@id="invoiceRadio"]/label[1]/span'
    nofixedbill_select = 'xpath=>//div[@id="invoiceRadio"]/label[2]/span'
    invoice_select = 'xpath=>//div[@id="invoiceRadio"]/label[3]/span'
    time_click = 'xpath=>//input[@id="chargeDate"]'
    time_select = 'id=>laydate_today'
    receipt_remark_input = 'xpath=>//div[@class="portlet-body"]/div[2]/div[2]/form//div[2]/div[3]/div[1]/input'
    invoice_remark_input = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[2]/form/div[2]/div[4]/div[1]/textarea'

    def finance_click_project(self):
        sleep(3)
        self.click(self.project)
        log.info(u'客户收费页面--点击项目名称')
        sleep(0.5)

    def finance_input_project(self):
        self.send_keys(self.project_input, '香碧歌')
        log.info(u'客户收费页面--输入项目名称')
        sleep(1.5)

    def finance_select_project(self):
        self.click(self.project_select)
        log.info(u'客户收费页面--点击选择项目')
        sleep(0.5)

    def finance_input_resource(self):
        self.send_keys(self.resource, '1-1-3')
        log.info(u'客户收费页面--输入资源名称')
        sleep(1.5)

    def finance_select_resource(self):
        self.click(self.resource_select)
        log.info(u'客户收费页面--选择项目资源')
        sleep(5)

    def finance_select_fee(self):
        self.click(self.fee_select)
        log.info(u'客户收费页面--选择第一条欠费信息')
        sleep(0.5)

    def finance_click_payment_type(self):
        self.click(self.payment_type_select)
        log.info(u'客户收费页面--点击付款方式')
        sleep(0.5)

    def finance_select_payment_type(self):
        self.select(self.payment_type_select, 5)
        log.info(u'客户收费页面--选择付款方式现金')
        sleep(0.5)

    def finance_click_receipt(self):
        self.click(self.receipt_write_select)
        log.info(u'客户收费页面--点击是否开票')
        sleep(0.5)

    def finance_select_receipt(self):
        self.select(self.receipt_write_select, 0)
        log.info(u'客户收费页面--是否开票选择是')
        sleep(0.5)

    def finance_click_penalty(self):
        self.click(self.penalty_select)
        log.info(u'客户收费页面--点击是否收取滞纳金')
        sleep(0.5)

    def finance_select_penalty(self):
        self.click(self.penalty_select)
        log.info(u'客户收费页面--收取滞纳金选择否')
        sleep(0.5)

    def finance_click_fixed(self):
        self.click(self.fixedbill_select)
        log.info(u'客户收费页面--点击定额票据')
        sleep(0.5)

    def finance_click_nofixed(self):
        self.click(self.nofixedbill_select)
        log.info(u'客户收费页面--点击非定额票据')
        sleep(0.5)

    def finance_click_invoice(self):
        self.click(self.invoice_select)
        log.info(u'客户收费页面--点击电子票据')
        sleep(0.5)

    def finance_click_time(self):
        self.click(self.time_click)
        log.info(u'客户收费页面--点击收费时间')
        sleep(0.5)

    def finance_select_time(self):
        self.click(self.time_select)
        log.info(u'客户收费页面--点击今天')
        sleep(0.5)

    def finance_input_remark(self):
        self.send_keys(self.receipt_remark_input, '这是票据备注')
        log.info(u'客户收费页面--输入票据备注')
        sleep(0.5)

    def finance_input_inivoice_remark(self):
        self.send_keys(self.invoice_remark_input, '这是电子发票备注')
        log.info(u'客户收费页面--输入电子发票备注')
        sleep(1)