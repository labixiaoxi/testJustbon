from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceCustormerRefund(BasePage):

    project = 'xpath=>//span[@class="select2-selection__rendered"]'
    project_input = 'xpath=>//input[@class="select2-search__field"]'
    project_select = 'xpath=>//li[contains(text(),"（成都）香境·香碧歌")]'
    resource = 'xpath=>//input[@name="resourceName"]'
    resource_select = 'xpath=>//div[@title="1-1-1"]'
    account_name = 'xpath=>//input[@name="accountName"]'
    account_select = 'xpath=>//div[@title="物业服务费"]'
    account_back = 'xpath=>//div[@class="input-group-btn"]/button[2]/i'
    start_date = 'id=>accrualDateStartInput'
    today_click = 'id=>laydate_today'
    hours_click = 'xpath=>//ul[@id="laydate_hms"]/li[2]/input'
    minutes_click = 'xpath=>//ul[@id="laydate_hms"]/li[3]/input'
    seconds_click = 'xpath=>//ul[@id="laydate_hms"]/li[4]/input'
    num_select = 'xpath=>//div[@id="laydate_hmsno"]/span[1]'
    end_date = 'id=>accrualDateEndInput'
    date_clear = 'id=>laydate_clear'
    search = 'xpath=>//i[@class="fa fa-search"]'
    reset = 'xpath=>//button[@ng-click="reset()"]'
    refund_select = 'xpath=>//div[@id="mainTable"]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]'
    refundbutton_click = 'xpath=>//button[@btn-authority="refund"]'
    refund_type = 'xpath=>//select[@name="refundPayMode"]'
    penalty_input = 'xpath=>//div[@class="form-group"]/table[2]/tbody/tr[1]/td[4]/input'
    arrears = 'xpath=>//div[@class="form-group"]/table[2]/tbody/tr[2]/td[2]/select'
    refund_money = 'xpath=>//div[@class="form-group"]/table[2]/tbody/tr[2]/td[4]/input'
    refund_date = 'id=>receviceDate'
    today = 'id=>laydate_today'
    refund_remark = 'xpath=>//div[@class="form-group"]/table[2]/tbody/tr[4]/td[2]/textarea'
    close = 'xpath=>//form[@name="reFundForm"]/div[2]/button[2]'


    def finance_click_project(self):
        sleep(3)
        self.click(self.project)
        log.info(u'客户退费页面--点击项目名称')
        sleep(0.5)

    def finance_input_project(self):
        self.send_keys(self.project_input, '香碧歌')
        log.info(u'客户退费页面--输入项目名称')
        sleep(1.5)

    def finance_select_project(self):
        self.click(self.project_select)
        log.info(u'客户退费页面--点击选择项目')
        sleep(0.5)

    def finance_input_resource(self):
        self.send_keys(self.resource, '1-1-1')
        log.info(u'客户退费页面--输入资源名称')
        sleep(1.5)

    def finance_select_resource(self):
        self.click(self.resource_select)
        log.info(u'客户退费页面--选择项目资源')
        sleep(0.5)

    def finance_account_input(self):
        self.send_keys(self.account_name,'物业服务')
        log.info(u'客户收费页面--输入计费科目名称')
        sleep(0.5)

    def finance_account_select(self):
        self.click(self.account_select)
        log.info(u'客户退费页面--选择计费科目')
        sleep(0.5)
        self.click(self.account_back)
        sleep(0.5)

    def finance_starttime_select(self):
        self.click(self.start_date)
        log.info(u'客户退费页面--点击收费起始时间')
        sleep(0.5)
        self.click(self.hours_click)
        self.click(self.num_select)
        log.info(u'客户退费页面--选择时')
        self.click(self.minutes_click)
        self.click(self.num_select)
        log.info(u'客户退费页面--选择分')
        self.click(self.seconds_click)
        self.click(self.num_select)
        log.info(u'客户退费页面--选择秒')
        sleep(0.5)
        self.click(self.date_clear)
        log.info(u'客户退费页面--清空收费起始时间')
        sleep(0.5)

    def finance_endtime_select(self):
        self.click(self.end_date)
        log.info(u'客户退费页面--点击收费结束时间')
        sleep(0.5)
        self.click(self.today_click)
        sleep(0.5)

    def finance_refund_search(self):
        self.click(self.search)
        log.info(u'客户退费页面--查询欠费信息')
        sleep(4)

    def finance_reset_click(self):
        self.click(self.reset)
        log.info(u'客户退费页面--点击重置')
        sleep(0.5)

    def finance_refund_select(self):
        self.click(self.refund_select)
        log.info(u'客户退费页面--点击第一条退费信息')
        sleep(0.5)

    def finance_refundbutton_click(self):
        self.click(self.refundbutton_click)
        log.info(u'客户退费页面--点击退费')
        sleep(1.5)

    def finance_refundtype_click(self):
        self.click(self.refund_type)
        log.info(u'客户退费页面--点击退费方式')
        sleep(0.5)

    def finance_refundtype_select(self):
        self.select(self.refund_type, 1)
        log.info(u'客户退费页面--点击退费方式现金')
        sleep(0.5)
        self.select(self.refund_type, 2)
        log.info(u'客户退费页面--点击退费方式换票未收现')
        sleep(0.5)

    def finance_penalty_input(self):
        self.send_keys(self.penalty_input, 10)
        log.info(u'客户退费页面--输入退滞纳金额')
        sleep(0.5)

    def finance_arrear_click(self):
        self.click(self.arrears)
        log.info(u'客户退费页面--点击是否恢复欠费')
        sleep(0.5)

    def finance_arrear_select(self):
        self.select(self.arrears, 0)
        log.info(u'客户退费页面--是否恢复欠费选择是')
        sleep(0.5)
        self.select(self.arrears, 1)
        log.info(u'客户退费页面--是否恢复欠费选择否')
        sleep(0.5)

    def finance_money_input(self):
        self.send_keys(self.refund_money, 100)
        log.info(u'客户退费页面--输入退款金额')
        sleep(0.5)

    def finance_refund_date(self):
        self.click(self.refund_date)
        sleep(0.5)
        self.click(self.today)
        log.info(u'客户退费页面--选择退款时间')
        sleep(0.5)

    def finance_refund_remark(self):
        self.send_keys(self.refund_remark, '这是退款备注')
        log.info(u'客户退费页面--输入退款备注')
        sleep(0.5)

    def finance_refund_close(self):
        self.click(self.close)
        log.info(u'客户退费页面--关闭退费窗口')
        sleep(1)