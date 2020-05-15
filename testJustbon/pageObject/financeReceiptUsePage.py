from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceReceiptUse(BasePage):

    num = 999
    range_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[1]/button[2]'
    project_a_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/i'
    project_b_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/i'
    project_c_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/ul/li/i'
    project_d_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/ul/li/ul/li/a'
    remark_input = 'xpath=>//textarea[@name="reason"]'
    add_click = 'xpath=>//button[contains(text(),"添加")]'
    typetree_click = 'xpath=>//div[@data-toggle="dropdown"]/button[2]/i'
    typetree_select_a = 'xpath=>//div[@data-toggle="dropdown"]/following-sibling::div[1]/div/ul/li/i'
    typetree_select_b = 'xpath=>//div[@data-toggle="dropdown"]/following-sibling::div[1]/div/ul/li/ul/li[3]/i'
    type_click = 'xpath=>//div[@class="portlet-body"]/table/tbody/tr/td[2]'
    type_input = 'xpath=>//input[@placeholder="请输入票据类型"]'
    typename_click = 'xpath=>//div[@ng-show="showGrid"]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div'
    count_click = 'xpath=>//div[@class="portlet-body"]/table/tbody/tr/td[3]'
    count_input = 'xpath=>//td[@class="inner-count"]/div/input'
    data_click = 'xpath=>//tr[@class="ng-scope"]/td[1]/label/span'
    remove_click = 'xpath=>//button[contains(text(),"删除")]'

    def finance_range_click(self):
        self.click(self.range_click)
        log.info(u'申请票据领用--选择使用范围')
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
        log.info(u'申请票据领用--选择项目')
        sleep(0.5)

    def finance_remark_input(self):
        self.send_keys(self.remark_input, '申请原因录入')
        log.info(u'申请票据领用--输入申请原因')
        sleep(0.5)

    def finance_add_click(self):
        self.click(self.add_click)
        log.info(u'申请票据领用--添加')
        sleep(0.5)

    def finance_type_click(self):
        self.click(self.type_click)
        sleep(0.5)
        self.click(self.typetree_click)
        sleep(0.5)
        self.click(self.typetree_select_a)
        sleep(0.5)
        self.click(self.typetree_select_b)
        sleep(0.5)
        log.info(u'申请票据领用--选择票据类型结构树')
        sleep(0.5)

    def finance_typename_click(self):
        self.click(self.typename_click)
        log.info(u'申请票据领用--选择票据类型')
        sleep(0.5)

    def finance_type_input(self):
        self.clear(self.type_input)
        sleep(0.5)
        self.send_keys(self.type_input, '温江分公司')
        log.info(u'申请票据领用--输入票据类型')
        sleep(1)

    def finance_count_click(self):
        self.click(self.count_click)
        log.info(u'申请票据领用--点击申请数量')
        sleep(0.5)

    def finance_count_input(self):
        self.clear(self.count_input)
        sleep(0.5)
        self.send_keys(self.count_input, self.num)
        log.info(u'申请票据领用--输入申请数量')
        sleep(0.5)

    def finance_remove_click(self):
        self.click(self.data_click)
        sleep(0.5)
        self.click(self.remove_click)
        log.info(u'申请票据领用--删除')
        sleep(0.5)