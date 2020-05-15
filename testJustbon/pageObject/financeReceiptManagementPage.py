from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceReceiptTypeManagement(BasePage):

    typetree_click = 'xpath=>//div[@id="receiptTypeTree"]/ul/li/ul/li[3]/ul/li[3]/a'
    receipttype_a_click = 'xpath=>//div[@id="receiptTypeTree"]/ul/li/i'
    receipttype_b_click = 'xpath=>//div[@id="receiptTypeTree"]/ul/li/ul/li[3]/i'
    receipttype_c_click = 'xpath=>//div[@id="receiptTypeTree"]/ul/li/ul/li[3]/ul/li[3]/i'
    receipttype_d_click = 'xpath=>//div[@id="receiptTypeTree"]/ul/li/ul/li[3]/ul/li[3]/ul/li[%d]'
    receipttype_add = 'xpath=>//span[contains(text(),"增加")]'
    typename_input = 'xpath=>//div[@id="newModal"]/div/div/form/div[2]/div/div[1]/div/input'
    number_input = 'xpath=>//div[@id="newModal"]/div/div/form/div[2]/div/div[2]/div/input'
    sort_click = 'xpath=>//div[@id="newModal"]/div/div/form/div[2]/div/div[3]/div/select'
    amount_input = 'xpath=>//div[@id="newModal"]/div/div/form/div[2]/div/div[4]/div/input'
    add_cancel_click = 'xpath=>//div[@id="newModal"]/div/div/form/div[3]/button[1]'
    receipttype_modify = 'xpath=>//span[contains(text(),"修改")]'
    typename_modify = 'xpath=>//form[@name="editForm"]/div[2]/div/div[1]/div/input'
    number_modify = 'xpath=>//form[@name="editForm"]/div[2]/div/div[2]/div/input'
    sort_modify = 'xpath=>//form[@name="editForm"]/div[2]/div/div[3]/div/select'
    modify_cancel_click = 'xpath=>//form[@name="editForm"]/div[3]/button[1]'
    status_get = 'xpath=>//div[@class="ui-grid-contents-wrapper"]/div[2]/div[2]/div/div[%d]/div/div[4]/div'
    count_get = '//div[@class="ui-grid-contents-wrapper"]/div[2]/div[2]/div/div'
    remove_click = 'xpath=>//span[contains(text(),"删除")]'
    forbidden_click = 'xpath=>//span[contains(text(),"禁用")]'
    use_click= 'xpath=>//span[contains(text(),"启用")]'
    close_click = 'xpath=>//div[@id="laydate_box"]/following-sibling::div[1]/div/div/div[2]/button[1]'
    nametext_input = 'xpath=>//div[@class="search-form-container"]/form/div[1]/div[1]/div/input'
    numbertext_input = 'xpath=>//div[@class="search-form-container"]/form/div[1]/div[2]/div/input'
    sort_select = 'xpath=>//div[@class="search-form-container"]/form/div[1]/div[3]/div/select'
    search_click = 'xpath=>//form[@name="searchForm"]/div[2]/div[2]/div/button'

    def finance_receipttype_click(self):
        self.click(self.receipttype_a_click)
        sleep(0.5)
        self.click(self.receipttype_b_click)
        sleep(0.5)
        self.click(self.receipttype_c_click)
        sleep(0.5)
        self.click(self.typetree_click)
        sleep(0.5)
        log.info(u'票据类型管理--选择票据目录')
        sleep(1)

    def finance_receipttype_add(self):
        self.click(self.receipttype_add)
        log.info(u'票据类型管理--增加')
        sleep(0.5)

    def finance_typename_input(self):
        self.send_keys(self.typename_input, '票据类型输入')
        log.info(u'票据类型管理--填入票据类型名称')
        sleep(0.5)

    def finance_number_input(self):
        self.send_keys(self.number_input, 'cs-000001')
        log.info(u'票据类型管理--填入票据编码')
        sleep(0.5)

    def finance_sort_click(self):
        self.click(self.sort_click)
        log.info(u'票据类型管理--点击分类')
        sleep(0.5)
        self.select(self.sort_click, 2)
        sleep(0.5)

    def finance_amount_input(self):
        self.send_keys(self.amount_input, 100)
        log.info(u'票据类型管理--输入定额发票金额')
        sleep(0.5)

    def finance_cancel_click(self):
        self.click(self.add_cancel_click)
        log.info(u'票据类型管理--关闭增加窗口')
        sleep(1)

    def finance_receipttype_modify(self):
        self.click(self.receipttype_modify)
        log.info(u'票据类型管理--修改')
        sleep(0.5)

    def finance_typename_modify(self):
        self.clear(self.typename_modify)
        self.send_keys(self.typename_modify, '票据类型名称变更')
        log.info(u'票据类型管理--修改票据类型名称')
        sleep(0.5)

    def finance_number_modify(self):
        self.clear(self.number_modify)
        self.send_keys(self.number_modify, 'cs-100001')
        log.info(u'票据类型管理--修改编码')
        sleep(0.5)

    def finance_sort_modify(self):
        self.select(self.sort_modify, 1)
        log.info(u'票据类型管理--修改分类')
        sleep(0.5)

    def finance_modify_cancel_click(self):
        self.click(self.modify_cancel_click)
        log.info(u'票据类型管理--取消关闭修改窗口')
        sleep(0.5)

    def finance_status_get(self):
        global loc
        for i in range(1, 59):
            self.find_element(self.receipttype_d_click % i).click()
            sleep(0.5)
            s = self.driver.find_elements_by_xpath(self.count_get)
            for j in range(1, len(s)+1):
                loc = self.find_element(self.status_get % j).get_attribute('title')
                if int(loc) == 0:
                    self.click(self.status_get % j)
                    log.info(u'票据类型管理--选择草稿数据')
                    sleep(1)
                    break
            if int(loc) == 0:
                break

    def finance_remove_click(self):
        self.click(self.remove_click)
        log.info(u'票据类型管理--删除')
        sleep(1)

    def finance_forbidden_click(self):
        self.click(self.forbidden_click)
        log.info(u'票据类型管理--禁用')
        sleep(1)

    def finance_use_click(self):
        self.click(self.use_click)
        log.info(u'票据类型管理--启用')
        sleep(1)

    def finance_close(self):
        self.click(self.close_click)
        log.info(u'票据类型管理--取消')
        sleep(1)

    def finance_nametext_input(self):
        self.send_keys(self.nametext_input, '票据类型名称')
        log.info(u'票据类型管理--填入名称')
        self.clear(self.nametext_input)
        sleep(0.5)

    def finance_numbertext_input(self):
        self.send_keys(self.numbertext_input, '1234567890')
        log.info(u'票据类型管理--填入编码')
        self.clear(self.numbertext_input)
        sleep(0.5)

    def finance_sort_select(self):
        self.select(self.sort_select, 1)
        log.info(u'票据类型管理--选择分类')
        sleep(0.5)

    def finance_search_click(self):
        self.click(self.search_click)
        log.info(u'票据类型管理--查询')
        sleep(0.5)