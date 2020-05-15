from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()

class FinancePaymoneyApply(BasePage):

    project = 'xpath=>//span[@class="select2-selection__rendered"]'
    project_input = 'xpath=>//input[@class="select2-search__field"]'
    project_select = 'xpath=>//li[contains(text(),"（成都）香境·香碧歌")]'
    remark_input = 'xpath=>//textarea[@name="remark"]'
    account_detail_click = 'xpath=>//uib-tab-heading[contains(text(),"计费科目明细")]'
    account_total_click = 'xpath=>//uib-tab-heading[contains(text(),"计费科目汇总")]'
    receipt_total_click = 'xpath=>//uib-tab-heading[contains(text(),"票据使用汇总")]'
    detail_click = 'xpath=>//uib-tab-heading[contains(text(),"基本明细")]'

    def finance_project_click(self):
        self.click(self.project)
        log.info(u'交款申请页面--点击项目名称')
        sleep(0.5)
        self.send_keys(self.project_input, '香碧歌')
        log.info(u'交款申请页面--输入项目名称')
        sleep(1.5)
        self.click(self.project_select)
        log.info(u'交款申请页面--选择项目')
        sleep(5)

    def finance_remark_input(self):
        self.send_keys(self.remark_input, '交款流程备注')
        log.info(u'交款申请页面--输入备注')
        sleep(2)

    def finance_account_detail_click(self):
        self.click(self.account_detail_click)
        log.info(u'交款申请页面--点击计费科目明细')
        sleep(2)

    def finance_account_total_click(self):
        self.click(self.account_total_click)
        log.info(u'交款申请页面--点击计费科目汇总')
        sleep(2)

    def finance_receipt_total_click(self):
        self.click(self.receipt_total_click)
        log.info(u'交款申请页面--点击票据使用汇总')
        sleep(2)

    def finance_detail_click(self):
        self.click(self.detail_click)
        log.info(u'交款申请页面--点击基本明细')
        sleep(2)