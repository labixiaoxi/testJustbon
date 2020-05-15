from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceReceiptRemove(BasePage):

    range_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[1]/button[2]'
    project_a_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/i'
    project_b_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/i'
    project_c_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/ul/li/i'
    project_d_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/ul/li/ul/li/a'
    add_click = 'xpath=>//div[@id="businessContainer"]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]'
    submit_click = 'xpath=>//button[contains(text(),"确定")]'
    cancel_click = 'xpath=>//button[contains(text(),"取消")]'
    remove_click = 'xpath=>//button[contains(text(),"删除")]'

    def finance_range_click(self):
        self.click(self.range_click)
        log.info(u'申请票据删除--选择使用范围')
        sleep(0.5)

    def finance_project_click(self):
        self.click(self.project_a_click)
        sleep(0.5)
        self.click(self.project_b_click)
        sleep(0.5)
        self.click(self.project_c_click)
        sleep(0.5)
        self.click(self.project_d_click)
        sleep(0.5)
        log.info(u'申请票据删除--选择项目')
        sleep(0.5)

    def finance_add_click(self):
        self.click(self.add_click)
        log.info(u'申请票据删除--添加')
        sleep(3)

    def finance_submit_click(self):
        self.click(self.submit_click)
        log.info(u'申请票据删除--确定')
        sleep(0.5)

    def finance_cancel_click(self):
        self.click(self.cancel_click)
        log.info(u'申请票据删除--取消')
        sleep(0.5)

    def finance_remove_click(self):
        self.click(self.remove_click)
        log.info(u'申请票据删除--删除')
        sleep(0.5)