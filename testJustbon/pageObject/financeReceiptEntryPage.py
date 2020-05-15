from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceReceiptEntry(BasePage):

    sn = 999
    en = 1456
    range_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[1]/button[2]'
    project_a_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/i'
    project_b_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/i'
    project_c_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/ul/li/i'
    project_d_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[2]/div[1]/ul/li/ul/li[1]/ul/li/ul/li/a'
    remark_input = 'xpath=>//textarea[@name="remark"]'
    add_click = 'xpath=>//button[contains(text(),"添加")]'
    type_click = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[2]'
    type_select_a = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[2]/div/div/div[1]/button[2]'
    type_select_b = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[2]/div/div/div[2]/div/ul/li/i'
    type_input = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[2]/div/div/input[1]'
    typename_click = 'xpath=>//div[@ng-show="showGrid"]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div'
    startno_click = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[3]'
    startno_input = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[3]/input'
    endno_click = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[4]'
    endno_input = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[4]/input'
    number_count = 'xpath=>//table[@id="receipt-type-grid"]/tbody/tr/td[5]'
    data_select = 'xpath=>//div[@id="businessContainer"]/div[2]/div/table/tbody/tr/td[1]/label/span'
    remove_click = 'xpath=>//button[contains(text(),"删除")]'

    def finance_range_click(self):
        self.click(self.range_click)
        log.info(u'申请票据入库--选择使用范围')
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
        log.info(u'申请票据入库--选择项目')
        sleep(0.5)

    def finance_remark_input(self):
        self.send_keys(self.remark_input, '申请原因录入')
        log.info(u'申请票据入库--输入申请原因')
        sleep(0.5)

    def finance_add_click(self):
        self.click(self.add_click)
        log.info(u'申请票据入库--添加')
        sleep(0.5)

    def finance_type_click(self):
        self.click(self.type_click)
        sleep(0.5)
        self.click(self.type_select_a)
        sleep(0.5)
        self.click(self.type_select_b)
        sleep(0.5)
        log.info(u'申请票据入库--选择票据类型结构树')
        sleep(0.5)

    def finance_type_input(self):
        self.send_keys(self.type_input, '温江分公司')
        log.info(u'申请票据入库--输入票据类型')
        sleep(0.5)

    def finance_typename_click(self):
        self.click(self.typename_click)
        log.info(u'申请票据入库--选择票据类型')
        sleep(0.5)

    def finance_startno_click(self):
        self.click(self.startno_click)
        log.info(u'申请票据入库--点击票据起始号码')
        sleep(0.5)

    def finance_startno_input(self):
        self.send_keys(self.startno_input, self.sn)
        log.info(u'申请票据入库--输入票据起始号码')
        sleep(0.5)

    def finance_endno_click(self):
        self.click(self.endno_click)
        log.info(u'申请票据入库--点击结束号码')
        sleep(0.5)

    def finance_endno_input(self):
        self.send_keys(self.endno_input, self.en)
        log.info(u'申请票据入库--输入票据结束号码')
        sleep(0.5)

    def finance_sno_input(self):
        sno = self.en - self.sn + 1
        return sno

    def finance_number_count(self):
        cn = self.find_element(self.number_count).text
        cn = int(cn)
        return cn

    def finance_data_select(self):
        self.click(self.data_select)
        log.info(u'申请票据入库--选择票据类型数据')
        sleep(0.5)

    def finance_remove_click(self):
        self.click(self.remove_click)
        log.info(u'申请票据入库--删除')
        sleep(0.5)