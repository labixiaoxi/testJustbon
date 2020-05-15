from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
import csv
log = PublicLogs()

class FinanceManagerRemove(BasePage):

    type_input = 'xpath=>//input[@ng-model="receiptTypeName"]'
    type_click = 'xpath=>//div[@title="%s"]'
    startno_input = 'xpath=>//input[@ng-model="searchFormObject.startNum"]'
    endno_input = 'xpath=>//input[@ng-model="searchFormObject.endNum"]'
    search_click = 'xpath=>//button[@ng-click="search()"]'
    reset_click = 'xpath=>//button[@ng-click="reset()"]'
    remove_click = 'xpath=>//span[contains(text(),"删除")]'
    cancel_click ='xpath=>//button[@data-bb-handler="cancel"]'

    def finance_type_click(self, text):
        self.send_keys(self.type_input, text)
        sleep(0.5)
        self.click(self.type_click % text)
        log.info(u'票管删除票据--选择票据类型')
        sleep(0.5)

    def finance_startno_input(self, text):
        self.clear(self.startno_input)
        sleep(0.5)
        self.send_keys(self.startno_input, text)
        log.info(u'票管删除票据--输入起始号码')
        sleep(0.5)

    def finance_endno_input(self, text):
        self.clear(self.endno_input)
        sleep(0.5)
        self.send_keys(self.endno_input, text)
        log.info(u'票管删除票据--输入结束号码')
        sleep(0.5)

    def finance_search_click(self):
        self.click(self.search_click)
        log.info(u'票管删除票据--查询')
        sleep(5)

    def finance_reset_click(self):
        self.click(self.reset_click)
        log.info(u'票管删除票据--重置')
        sleep(0.5)

    def finance_remove_click(self):
        self.click(self.remove_click)
        log.info(u'票管删除票据--删除')
        sleep(1)

    def finance_cancel_click(self):
        self.click(self.cancel_click)
        log.info(u'票管删除票据--取消')
        sleep(0.5)

    # def finance_data_read(self, text):
    #     with open(r"C:\Users\admin\Desktop\a.csv", 'r') as f:
    #         data = csv.reader(f)
    #         s = list(data)[0][text]
    #         return s