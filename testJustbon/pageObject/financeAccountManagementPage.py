from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceAccountManagement(BasePage):

    project = 'xpath=>//span[@class="select2-selection select2-selection--single"]'
    project_input = 'xpath=>//input[@class="select2-search__field"]'
    project_select = 'xpath=>//li[contains(text(),"（成都）香境·香碧歌")]'
    resource = 'xpath=>//input[@class="form-control ng-pristine ng-untouched ng-invalid ng-invalid-required"]'
    resource_select = 'xpath=>//div[@title="1-1-3"]'
    chargr_type = 'xpath=>//select[@ng-model="baseFormObject.chargeType"]'
    source = 'xpath=>//select[@class="form-control ng-pristine ng-untouched ng-valid"]'
    account1 = 'xpath=>//div[@id="onceFormObject.accountId"]/div[1]/button[2]/i'
    account2 = 'xpath=>//form[@name="onceForm"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/ul/li/i'
    account3 = 'xpath=>//li[@id="4800453"]/i'
    account4 = 'xpath=>//a[@id="708128908_anchor"]'
    account_select = 'xpath=>//div[@title="营业员工牌费"]'
    type = 'xpath=>//form[@name="onceForm"]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/label[1]/span[1]'
    money = 'xpath=>//input[@name="fee"]'
    startdate = 'id=>startDateInput'
    date_select = 'id=>laydate_today'
    enddate = 'id=>endDateInput'
    remark = 'xpath=>//textarea[@class="form-control ng-pristine ng-untouched ng-valid"]'
    cost = 'xpath=>//div[@class="fade-in-up ng-scope"]/div[3]/div[1]/button[2]'
    cancel = 'xpath=>//button[@data-bb-handler="cancel"]'

    def finance_click_project(self):
        sleep(5)
        self.click(self.project)
        log.info(u"批量计费管理页面--点击项目名称")
        sleep(0.5)

    def finance_input_project(self):
        self.send_keys(self.project_input, '香碧歌')
        log.info(u"批量计费管理页面--输入项目名称")
        sleep(0.5)

    def finance_click_project_select(self):
        self.click(self.project_select)
        log.info(u"批量计费管理页面--选择项目")
        sleep(2)

    def finance_input_resource(self):
        self.send_keys(self.resource, '1-1-3')
        log.info(u"批量计费管理页面--输入资源名称")
        sleep(1.5)

    def finance_click_resource(self):
        self.click(self.resource_select)
        log.info(u"批量计费管理页面--选择资源")
        sleep(2)

    def finance_select_charge_type(self):
        self.select(self.chargr_type, 0)
        log.info(u"批量计费管理页面--选择计费类型")
        sleep(0.5)

    def finance_click_source(self):
        self.click(self.source)
        log.info(u"批量计费管理页面--选择费用来源")
        sleep(0.5)

    def finance_click_account(self):
        self.click(self.account1)
        sleep(0.5)
        self.click(self.account2)
        sleep(0.5)
        self.click(self.account3)
        sleep(0.5)
        self.click(self.account4)
        sleep(0.5)
        log.info(u"批量计费管理页面--选择计费科目")

    def finance_click_type(self):
        self.click(self.type)
        log.info(u"批量计费管理页面--选择计费方式")

    def finance_input_money(self):
        self.send_keys(self.money, '150')
        log.info(u"批量计费管理页面--输入欠费金额")

    def finance_click_startdate(self):
        self.click(self.startdate)
        self.click(self.date_select)
        log.info(u"批量计费管理页面--选择开始时间")

    def finance_click_enddate(self):
        self.click(self.enddate)
        self.click(self.date_select)
        log.info(u"批量计费管理页面--选择结束时间")

    def finance_input_remark(self):
        self.send_keys(self.remark, '自动化测试')
        log.info(u"批量计费管理页面--输入欠费描述")

    def finance_click_cost(self):
        self.click(self.cost)
        log.info(u"批量计费管理页面--点击计费")
        sleep(1.5)

    def finance_click_cancel(self):
        self.click(self.cancel)
        log.info(u"批量计费管理页面--点击取消")
        sleep(1)
