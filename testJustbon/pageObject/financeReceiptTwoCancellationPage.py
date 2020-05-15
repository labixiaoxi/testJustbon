from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceTwoCancellation(BasePage):

    remark_input = 'xpath=>//textarea[@name="remark"]'
    add_click = 'xpath=>//button[contains(text(),"添加")]'
    data_long = 'xpath=>//div[@id="modal-body"]/div/div[1]/div[1]/div/div[2]/div/div/div'
    data_a_click = 'xpath=>//div[@id="modal-body"]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div/div/div'
    type_a_text = 'xpath=>//div[@id="modal-body"]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div'
    status_a_text = 'xpath=>//div[@id="modal-body"]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div'
    startno_a_text = 'xpath=>//div[@id="modal-body"]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div'
    endno_a_text = 'xpath=>//div[@id="modal-body"]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[4]/div'
    count_a_text = 'xpath=>//div[@id="modal-body"]/div/div[1]/div[2]/div[2]/div/div[1]/div/div[5]/div'
    submit_click = 'xpath=>//button[contains(text(),"确定")]'
    cancel_click = 'xpath=>//button[contains(text(),"取消")]'
    data_b_click = 'xpath=>//div[@id="businessContainer"]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div/div/div'
    type_b_text = 'xpath=>//div[@id="businessContainer"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[1]'
    status_b_text = 'xpath=>//div[@id="businessContainer"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]'
    startno_b_text = 'xpath=>//div[@id="businessContainer"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[3]'
    endno_b_text = 'xpath=>//div[@id="businessContainer"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[4]'
    count_b_text = 'xpath=>//div[@id="businessContainer"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[5]'
    remove_click = 'xpath=>//button[contains(text(),"删除")]'

    def finance_remark_input(self):
        self.send_keys(self.remark_input, '填入申请原因')
        log.info(u'票据二级核销--填写申请原因')
        sleep(0.5)

    def finance_add_click(self):
        self.click(self.add_click)
        log.info(u'票据二级核销--添加')
        sleep(0.5)

    #def finance_data_a_click(self):

        # self.click(self.data_a_click)
        # log.info(u'票据二级核销--选择数据')
        # sleep(0.5)

    # def finance_type_a_text(self):
    #     ta = self.find_element(self.type_a_text).text
    #     return ta
    #
    # def finance_status_a_text(self):
    #     sa = self.find_element(self.status_a_text).text
    #     return sa
    #
    # def finance_startno_a_text(self):
    #     sna = self.find_element(self.startno_a_text).text
    #     return sna
    #
    # def finance_endno_a_text(self):
    #     ea = self.find_element(self.endno_a_text).text
    #     return ea
    #
    # def finance_count_a_text(self):
    #     ca = self.find_element(self.count_a_text).text
    #     return ca

    # def finance_submit_click(self):
    #     self.click(self.submit_click)
    #     log.info(u'票据二级核销--确定')
    #     sleep(0.5)
    #
    # def finance_data_b_click(self):
    #     self.click(self.data_b_click)
    #     log.info(u'票据二级核销--选择已选择的数据')
    #     sleep(0.5)
    #
    # def finance_type_b_text(self):
    #     tb = self.find_element(self.type_b_text).text
    #     return tb
    #
    # def finance_status_b_text(self):
    #     sb = self.find_element(self.status_b_text).text
    #     return sb
    #
    # def finance_startno_b_text(self):
    #     snb = self.find_element(self.startno_b_text).text
    #     return snb
    #
    # def finance_endno_b_text(self):
    #     eb = self.find_element(self.endno_b_text).text
    #     return eb
    #
    # def finance_count_b_text(self):
    #     cb = self.find_element(self.count_b_text).text
    #     return cb
    #
    def finance_cancel_click(self):
        self.click(self.cancel_click)
        log.info(u'票据二级核销--取消')
        sleep(0.5)
    #
    # def finance_remove_click(self):
    #     self.click(self.remove_click)
    #     log.info(u'票据二级核销--删除')
    #     sleep(0.5)