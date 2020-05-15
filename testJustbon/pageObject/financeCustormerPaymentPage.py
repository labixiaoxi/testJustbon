from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinanceCustormerPayment(BasePage):

    home_menu = 'xpath=>//div[@ng-click="disablePopover()"]'
    home_page = 'xpath=>//i[@class="icon-home"]'
    payment_management = 'xpath=>//div[@class="page-sidebar-wrapper ng-scope"]/div[1]/div[1]/ul[1]/li[9]/a'
    custormer_charge = 'xpath=>//div[@class="page-sidebar-wrapper ng-scope"]/div[1]/div[1]/ul[1]/li[9]/ul/li[1]'
    custormer_refund = 'xpath=>//div[@class="page-sidebar-wrapper ng-scope"]/div[1]/div[1]/ul[1]/li[9]/ul/li[3]'
    payment_inquiry = 'xpath=>//div[@class="page-sidebar-wrapper ng-scope"]/div[1]/div[1]/ul[1]/li[9]/ul/li[4]'
    pay_money_click = 'xpath=>//div[@class="page-sidebar-wrapper ng-scope"]/div[1]/div[1]/ul[1]/li[11]/a'
    pay_money_apply = 'xpath=>//div[@class="page-sidebar-wrapper ng-scope"]/div[1]/div[1]/ul[1]/li[11]/ul/li[1]'
    receipt_management = 'xpath=>//span[contains(text(),"票据管理")]'
    receipttype_management = 'xpath=>//a[contains(text(),"票据类型管理")]'
    receipt_entry = 'xpath=>//a[contains(text(),"申请票据入库")]'
    receipt_use = 'xpath=>//a[contains(text(),"申请票据领用")]'
    one_cancellation = 'xpath=>//a[contains(text(),"票据一级核销")]'
    two_cancellation = 'xpath=>//a[contains(text(),"票据二级核销")]'
    receipt_back = 'xpath=>//a[contains(text(),"申请票据退回")]'
    receipt_remove = 'xpath=>//a[contains(text(),"申请票据删除")]'
    receipt_cancel = 'xpath=>//a[contains(text(),"票据作废/恢复")]'
    invoice_count = 'xpath=>//a[contains(text(),"电子收据统计")]'
    receipt_count = 'xpath=>//a[contains(text(),"票据段统计信息")]'
    hold_count = 'xpath=>//a[contains(text(),"持有票据统计")]'
    manager_remove = 'xpath=>//a[contains(text(),"票管删除票据")]'


    def finance_menu(self):
        self.click(self.home_menu)
        sleep(1)

    def finance_click_homepage(self):
        self.click(self.home_page)
        log.info(u'菜单栏--点击首页')
        sleep(3)

    def finance_click_payment_management(self):
        self.click(self.payment_management)
        log.info(u'主页--点击实收管理')
        sleep(1)

    def finance_click_custormer_charge(self):
        self.click(self.custormer_charge)
        log.info(u'主页--点击客户收费')
        sleep(3)

    def finance_click_custormer_refund(self):
        self.click(self.custormer_refund)
        log.info(u'主页--点击客户退费')
        sleep(3)

    def finance_click_payment_inquiry(self):
        self.click(self.payment_inquiry)
        log.info(u'主页--点击实收查询')
        sleep(8)

    def finance_click_paymoney_apply(self):
        self.click(self.pay_money_click)
        log.info(u'主页--点击财务交款')
        sleep(1.5)

    def finance_click_pay_money(self):
        self.click(self.pay_money_apply)
        log.info(u'主页--点击交款申请')
        sleep(5)

    def finance_click_receipt_management(self):
        self.click(self.receipt_management)
        log.info(u'主页--点击票据管理')
        sleep(1)

    def finance_click_receipt_type_management(self):
        self.click(self.receipttype_management)
        log.info(u'主页--点击票据类型管理')
        sleep(5)

    def finance_click_receipt_entry(self):
        self.click(self.receipt_entry)
        log.info(u'主页--点击申请票据入库')
        sleep(5)

    def finance_click_receipt_use(self):
        self.click(self.receipt_use)
        log.info(u'主页--点击申请票据领用')
        sleep(5)

    def finance_click_one_cancellation(self):
        self.click(self.one_cancellation)
        log.info(u'主页--点击票据一级核销')
        sleep(5)

    def finance_click_two_cancellation(self):
        self.click(self.two_cancellation)
        log.info(u'主页--点击票据二级核销')
        sleep(5)

    def finance_receipt_back(self):
        self.click(self.receipt_back)
        log.info(u'主页--点击申请票据退回')
        sleep(5)

    def finance_receipt_remove(self):
        self.click(self.receipt_remove)
        log.info(u'主页--点击申请票据删除')
        sleep(5)

    def finance_receipt_cancel(self):
        self.click(self.receipt_cancel)
        log.info(u'主页--点击票据作废/恢复')
        sleep(5)

    def finance_invoice_count(self):
        self.click(self.invoice_count)
        log.info(u'主页--点击电子收据统计')
        sleep(5)

    def finance_receipt_count(self):
        self.click(self.receipt_count)
        log.info(u'主页--点击票据段统计信息')
        sleep(5)

    def finance_hold_count(self):
        self.click(self.hold_count)
        log.info(u'主页--点击持有票据统计')
        sleep(5)

    def finance_manager_remove(self):
        self.click(self.manager_remove)
        log.info(u'主页--票管删除票据')
        sleep(5)