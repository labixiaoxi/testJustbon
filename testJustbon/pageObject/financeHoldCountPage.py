from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
import csv
log = PublicLogs()

class FinanceHoldCount(BasePage):

    user_input = 'xpath=>//input[@name="structureName"]'
    user_click = 'xpath=>//div[@title="（成都）漫城小区"]'
    type_input = 'xpath=>//input[@ng-model="receiptTypeName"]'
    type_click = 'xpath=>//div[@ng-show="showGrid"]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]'
    type_clear = 'xpath=>//div[@data-toggle="dropdown"]/button[1]'
    status_click = 'xpath=>//span[@role="combobox"]'
    status_select = 'xpath=>//span[@class="select2-results"]/ul/li[3]'
    search_click = 'xpath=>//button[@ng-click="search()"]'
    reset_click = 'xpath=>//button[@ng-click="reset()"]'
    data_get = '//div[@id="mainTable"]/div[1]/div[1]/div[1]/div[2]/div[1]/div'
    status_get = 'xpath=>//div[@id="mainTable"]/div[1]/div[2]/div[2]/div[1]/div[%d]/div[1]/div[5]/div'
    num_get = 'xpath=>//div[@id="mainTable"]/div[1]/div[2]/div[2]/div[1]/div[%d]/div[1]/div[2]/div'
    type_get = 'xpath=>//div[@id="mainTable"]/div[1]/div[2]/div[2]/div[1]/div[%d]/div[1]/div[1]/div'

    def finance_user_input(self):
        self.send_keys(self.user_input, '唐利10')
        sleep(5)
        self.click(self.user_click)
        log.info(u'持有票据统计--选择票据持有人')
        sleep(0.5)

    def finance_type_input(self):
        self.send_keys(self.type_input, '手工收据')
        sleep(2)
        self.click(self.type_click)
        log.info(u'持有票据统计--选择票据类型')
        sleep(0.5)
        self.click(self.type_clear)
        log.info(u'持有票据统计--清除票据类型')
        sleep(0.5)

    def finance_status_select(self):
        self.click(self.status_click)
        sleep(0.5)
        self.click(self.status_select)
        log.info(u'持有票据统计--选择票据状态')
        sleep(0.5)

    def finance_search_click(self):
        self.click(self.search_click)
        log.info(u'持有票据统计--查询')
        sleep(5)

    def finance_reset_click(self):
        self.click(self.reset_click)
        log.info(u'持有票据统计--重置')
        sleep(0.5)

    def finance_data_get(self):
        n = self.driver.find_elements_by_xpath(self.data_get)
        if len(n) > 0:
            log.info(u'持有票据统计--已查询到票据信息')
            sleep(0.5)

    def finance_data_write(self):
        l = []
        for i in range(1, 31):
            t = self.find_element(self.status_get % i).text
            if t == '领用':
                ty = self.find_element(self.type_get % i).text
                num = self.find_element(self.num_get % i).text
                # l.append(ty)
                # l.append(num)
                log.info(u'持有票据统计--已获取到领用状态票据的信息，票管删除票据模块使用')
                sleep(1)
                return ty, num
                # with open(r"C:\Users\admin\Desktop\a.csv", 'w') as f:
                #     writer = csv.writer(f)
                #     writer.writerow(l)
                #     break