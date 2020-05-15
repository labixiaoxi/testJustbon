from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
import re
log = PublicLogs()


class FinanceInvoiceCount(BasePage):

    company_click = 'xpath=>//input[@name="structureName"]/following-sibling::div[1]/button[2]/i'
    company_select = 'xpath=>//li[@aria-level="1"]'
    project_click = 'xpath=>//div[@name="projectId"]/div[2]/div[1]/button'
    clear_click = 'xpath=>//button[contains(text(),"清空")]'
    project_input = 'xpath=>//input[@aria-label="Search"]'
    project_select = 'xpath=>//span[contains(text(),"（成都）香境·香碧歌")]'
    stratno_a_input = 'xpath=>//input[@ng-model="params.startNo"]'
    endno_a_input = 'xpath=>//input[@ng-model="params.endNo"]'
    search_a_click = 'xpath=>//button[@ng-click="search()"]'
    reset_a_click = 'xpath=>//button[@ng-click="reset()"]'
    data_a_click = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]'
    catdetail_a_click = 'xpath=>//span[contains(text(),"查看明细")]'
    resource_input = 'xpath=>//input[@name="resourceName"]'
    resource_click = 'xpath=>//div[@title="1-1-3"]'
    resource_clear = 'xpath=>//div[@class="clear right"]'
    starttime_click = 'xpath=>//button[@id="createTimeStartBtn"]'
    lasstmonth_click = 'xpath=>//div[@id="laydate_MM"]/a[1]'
    day_click = 'xpath=>//td[@d="1" and @class="laydate_click"]'
    endtime_click = 'xpath=>//input[@id="createTimeEnd"]'
    sure_click = 'xpath=>//a[@id="laydate_ok"]'
    maxno_get = 'xpath=>//div[@class="form-control bold ng-binding"]'
    startno_b_input = 'xpath=>//input[@ng-model="params.startNo"]'
    endno_b_input = 'xpath=>//input[@ng-model="params.endNo"]'
    more_click = 'xpath=>//form[@name="searchForm"]/div[4]/i'
    more = 'fa fa-chevron-down'
    status_select = 'xpath=>//select[@ng-model="params.status"]'
    search_b_click = 'xpath=>//button[@ng-click="search()"]'
    reset_b_click = 'xpath=>//button[@ng-click="reset()"]'
    data_b_click = 'xpath=>//div[@id="searchPart"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]'
    catdetail_b_click = 'xpath=>//span[contains(text(),"查看明细")]'
    data_get = '//div[@id="mainTable"]/div[1]/div[1]/div[1]/div[2]/div[1]/div'
    detail_click = 'xpath=>//a[contains(text(),"票据明细")]'
    invoice_click = 'xpath=>//a[contains(text(),"电子发票")]'
    refund_click = 'xpath=>//a[contains(text(),"退款明细")]'
    close_click = 'xpath=>//button[@class="close"]'

    def finance_company_click(self):
        self.click(self.company_click)
        sleep(0.5)
        self.click(self.company_select)
        log.info(u'电子收据统计--选择组织机构')
        sleep(0.5)

    def finance_project_click(self):
        self.click(self.project_click)
        sleep(0.5)
        self.click(self.clear_click)
        sleep(0.5)
        self.send_keys(self.project_input, '香碧歌')
        sleep(0.5)
        self.click(self.project_select)
        log.info(u'电子收据统计--选择项目')
        sleep(0.5)

    def finance_startno_a_input(self):
        self.clear(self.stratno_a_input)
        sleep(0.5)
        self.send_keys(self.stratno_a_input, 111111)
        sleep(0.5)
        self.clear(self.stratno_a_input)
        log.info(u'电子收据统计--输入起始号码')
        sleep(0.5)

    def finance_endno_a_input(self):
        self.clear(self.endno_a_input)
        sleep(0.5)
        self.send_keys(self.endno_a_input, 999999)
        sleep(0.5)
        self.clear(self.endno_a_input)
        log.info(u'电子收据统计--输入结束号码')
        sleep(0.5)

    def finance_search_a_click(self):
        self.click(self.search_a_click)
        log.info(u'电子收据统计--查询')
        sleep(6)

    def finance_reset_a_click(self):
        self.click(self.reset_a_click)
        log.info(u'电子收据统计--重置')
        sleep(0.5)

    def finance_data_a_click(self):
        self.click(self.data_a_click)
        log.info(u'电子收据统计--选择数据')
        sleep(0.5)

    def finance_catdetail_a_click(self):
        self.click(self.catdetail_a_click)
        log.info(u'电子收据统计--查看明细')
        sleep(3)

    def finance_resource_click(self):
        self.send_keys(self.resource_input, '1-1-3')
        sleep(1)
        self.click(self.resource_click)
        sleep(0.5)
        self.click(self.resource_clear)
        log.info(u'电子收据统计--选择资源')
        sleep(0.5)

    def finance_starttime_click(self):
        self.click(self.starttime_click)
        sleep(0.5)
        self.click(self.lasstmonth_click)
        sleep(0.5)
        self.click(self.day_click)
        log.info(u'电子收据统计--选择开票时间起')
        sleep(0.5)

    def finance_endtime_click(self):
        self.click(self.endtime_click)
        sleep(0.5)
        self.click(self.sure_click)
        log.info(u'电子收据统计--选择开票时间止')
        sleep(0.5)

    def finance_maxno_get(self):
        n = self.find_element(self.maxno_get).text
        m = re.findall('[0-9]+', n)
        num = int(m[0])
        return num

    def finance_startno_b_input(self):
        self.clear(self.startno_b_input)
        sleep(0.5)
        self.send_keys(self.startno_b_input, self.finance_maxno_get())
        log.info(u'电子收据统计--输入票据起始号码')
        sleep(0.5)

    def finance_endno_b_input(self):
        self.clear(self.endno_b_input)
        sleep(0.5)
        self.send_keys(self.endno_b_input, self.finance_maxno_get())
        log.info(u'电子收据统计--输入票据结束号码')
        sleep(0.5)

    def finance_more_click(self):
        get_c = self.find_element(self.more_click).get_attribute('class')
        if get_c == self.more:
            self.click(self.more_click)
            log.info(u'电子收据统计--展开更多')
            sleep(0.5)
        else:
            pass

    def finance_status_select(self):
        self.select(self.status_select, 2)
        log.info(u'电子收据统计--选择作废状态')
        sleep(0.5)
        self.select(self.status_select, 1)
        log.info(u'电子收据统计--选择使用状态')
        sleep(0.5)
        self.select(self.status_select, 0)
        log.info(u'电子收据统计--选择默认状态')
        sleep(0.5)

    def finance_search_b_click(self):
        self.click(self.search_b_click)
        log.info(u'电子收据统计--查询')
        sleep(5)

    def finance_reset_b_click(self):
        self.click(self.reset_b_click)
        log.info(u'电子收据统计--重置')
        sleep(0.5)

    def finance_data_b_click(self):
        self.click(self.data_a_click)
        log.info(u'电子收据统计--选择数据')
        sleep(0.5)

    def finance_catdetail_b_click(self):
        self.click(self.catdetail_b_click)
        log.info(u'电子收据统计--查看明细')
        sleep(4)

    def finance_data_get(self):
        c = self.driver.find_elements_by_xpath(self.data_get)
        if len(c) > 0:
            log.info(u'电子收据统计--查看收费信息正确')
            sleep(0.5)

    def finance_detail_click(self):
        self.click(self.detail_click)
        log.info(u'电子收据统计--点击票据明细')
        sleep(0.5)

    def finance_invoice_click(self):
        self.click(self.invoice_click)
        log.info(u'电子收据统计--点击电子发票')
        sleep(0.5)

    def finance_refund_click(self):
        self.click(self.refund_click)
        log.info(u'电子收据统计--点击退款明细')
        sleep(0.5)

    def finance_close_click(self):
        self.click(self.close_click)
        log.info(u'电子收据统计--点击关闭')
        sleep(0.5)