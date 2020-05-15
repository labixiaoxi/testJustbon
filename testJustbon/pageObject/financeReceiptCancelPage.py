from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceReceiptCancel(BasePage):

    type_input = 'xpath=>//input[@name="receiptType" and @ng-model="receiptTypeName"]'
    type_click = 'xpath=>//div[@title="徐州分公司增值税普通发票"]'
    close_type = 'xpath=>//form[@name="searchForm"]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/i'
    startno_input = 'xpath=>//input[@name="startNo"]'
    endno_input = 'xpath=>//input[@name="endNo"]'
    remark_input ='xpath=>//textarea[@name="remark"]'
    resume_click = 'xpath=>//button[contains(text(),"恢复")]'
    nullify_click = 'xpath=>//button[contains(text(),"作废")]'
    submit_click = 'xpath=>//button[contains(text(),"确认")]'
    cancel_click = 'xpath=>//button[contains(text(),"取消")]'
    reset_click = 'xpath=>//button[contains(text(),"重置")]'
    cat_click = 'xpath=>//button[contains(text(),"查看收费记录")]'
    data = 'xpath=>//div[@id="mainTable"]/div[1]/div[1]/div[1]/div[2]/div[1]/div'
    detail_click = 'xpath=>//a[contains(text(),"票据明细")]'
    close_button = 'xpath=>//button[@aria-label="Close"]'

    def finance_type_input(self):
        self.send_keys(self.type_input, '徐州分公司增值税普通发票')
        log.info(u'票据作废/恢复--输入票据类型')
        sleep(1)

    def finance_type_click(self):
        self.click(self.type_click)
        sleep(0.5)
        self.click(self.close_type)
        log.info(u'票据作废/恢复--选择票据类型')
        sleep(1)

    def finance_startno_input(self):
        self.clear(self.startno_input)
        sleep(0.5)
        self.send_keys(self.startno_input, 4098527)
        log.info(u'票据作废/恢复--输入起始号码')
        sleep(0.5)

    def finance_endno_input(self):
        self.clear(self.endno_input)
        sleep(0.5)
        self.send_keys(self.endno_input, 4098527)
        log.info(u'票据作废/恢复--输入起始号码')
        sleep(0.5)

    def finance_remark_input(self):
        self.clear(self.remark_input)
        sleep(0.5)
        self.send_keys(self.remark_input, '测试票据作废/恢复备注录入')
        log.info(u'票据作废/恢复--备注录入')
        sleep(0.5)

    def finance_resume_click(self):
        self.click(self.resume_click)
        log.info(u'票据作废/恢复--点击恢复')
        sleep(0.5)

    def finance_nullify_click(self):
        self.click(self.nullify_click)
        log.info(u'票据作废/恢复--点击作废')
        sleep(0.5)

    # def finance_submit_click(self):
    #     self.click(self.submit_click)
    #     log.info(u'票据作废/恢复--确认按钮')
    #     sleep(0.5)

    def finance_cancel_click(self):
        self.click(self.cancel_click)
        log.info(u'票据作废/恢复--点击取消')
        sleep(0.5)

    def finance_reset_click(self):
        self.click(self.reset_click)
        log.info(u'票据作废/恢复--点击重置')
        sleep(0.5)

    def finance_cat_click(self):
        self.click(self.cat_click)
        log.info(u'票据作废/恢复--点击查看收费记录')
        sleep(6)

    def finance_data_get(self):
        num = self.driver.find_elements(self.data)
        if len(num) > 0:
            log.info(u'票据作废/恢复--获取票据关联收费数据成功')
            sleep(0.5)
        else:
            log.info(u'票据作废/恢复--获取票据管理收费数据失败')
            sleep(0.5)

    def finance_detail_click(self):
        self.click(self.detail_click)
        log.info(u'票据作废/恢复--点击票据明细')
        sleep(0.5)

    def finance_close_click(self):
        self.click(self.close_button)
        log.info(u'票据作废/恢复--点击关闭')
        sleep(0.5)