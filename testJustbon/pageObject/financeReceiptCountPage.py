from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()

class FinanceReceiptCount(BasePage):

    type_input = 'xpath=>//input[@ng-model="receiptTypeName"]'
    type_click = 'xpath=>//div[@ui-grid="gridOptions"]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]'
    project_click = 'xpath=>//div[@name="projectId"]/div[2]/div[1]/button'
    clear_click = 'xpath=>//button[contains(text(),"清空")]'
    project_input = 'xpath=>//input[@aria-label="Search"]'
    project_select = 'xpath=>//span[contains(text(),"（成都）香境·香碧歌")]'
    startno_input ='xpath=>//input[@ng-model="searchFormObject.startNum"]'
    endno_input = 'xpath=>//input[@ng-model="searchFormObject.endNum"]'
    search_click = 'xpath=>//button[@ng-click="search()"]'
    reset_click = 'xpath=>//button[@ng-click="reset()"]'
    data_a_click = 'xpath=>//div[@id="mainTable"]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]'
    catdetail_a_click = 'xpath=>//span[contains(text(),"查看明细")]'
    data_b_click = 'xpath=>//div[@role="rowheader"]/div[1]/div[1]/div[1]'
    catdetail_b_click = 'xpath=>//span[contains(text(),"查看详情")]'
    data_get = '//div[@class="pull-left"]/table/tbody/tr'
    detail_click = 'xpath=>//a[contains(text(),"票据明细")]'
    close_click = 'xpath=>//button[@class="close"]'

    def finance_type_click(self):
        self.send_keys(self.type_input, '徐州分公司增值税普通发票')
        sleep(0.5)
        self.click(self.type_click)
        log.info(u'票据段统计信息--选择票据类型')
        sleep(0.5)

    def finance_project_click(self):
        self.click(self.project_click)
        sleep(0.5)
        self.click(self.clear_click)
        sleep(0.5)
        self.send_keys(self.project_input, '香碧歌')
        sleep(0.5)
        self.click(self.project_select)
        log.info(u'票据段统计信息--选择项目')
        sleep(0.5)
        self.click(self.clear_click)
        sleep(0.5)

    def finance_startno_input(self):
        self.send_keys(self.startno_input, 1)
        log.info(u'票据段统计信息--输入起始号码')
        sleep(0.5)

    def finance_endno_input(self):
        self.send_keys(self.endno_input, 99999999)
        log.info(u'票据段统计信息--输入结束号码')
        sleep(0.5)

    def finance_search_click(self):
        self.click(self.search_click)
        log.info(u'票据段统计信息--查询')
        sleep(5)

    def finance_reset_click(self):
        self.click(self.reset_click)
        log.info(u'票据段统计信息--重置')
        sleep(0.5)

    def finance_data_a_click(self):
        self.click(self.data_a_click)
        log.info(u'票据段统计信息--选择数据')
        sleep(0.5)

    def finance_catdetail_a_click(self):
        self.click(self.catdetail_a_click)
        log.info(u'票据段统计信息--查看明细')
        sleep(2)

    def finance_data_b_click(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        sleep(3)
        self.click(self.data_b_click)
        log.info(u'票据段统计信息--选择数据')
        sleep(0.5)

    def finance_catdetail_b_click(self):
        self.click(self.catdetail_b_click)
        log.info(u'票据段统计信息--查看详情')
        sleep(2)

    def finance_data_get(self):
        n = self.driver.find_elements_by_xpath(self.data_get)
        if len(n) > 0:
            log.info(u'票据段统计信息--查看数据正确')
            sleep(0.5)

    def finance_detail_click(self):
        self.click(self.detail_click)
        log.info(u'票据段统计信息--点击票据明细')
        sleep(0.5)

    def finance_close_click(self):
        self.click(self.close_click)
        log.info(u'票据段统计信息--关闭窗口')
        sleep(0.5)
        self.driver.close()
        sleep(0.5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(0.5)