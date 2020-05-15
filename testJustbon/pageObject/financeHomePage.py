from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep

log = PublicLogs()

class FinanceHomePage(BasePage):

    account_management = 'xpath=>//ul[@class="page-sidebar-menu page-header-fixed"]/li[6]/a'
    batch_charging_management = 'xpath=>//ul[@class="page-sidebar-menu page-header-fixed"]/li[6]/ul/li[5]'

    def finance_click_account_management(self):
        self.click(self.account_management)
        log.info(u'收费系统主页--点击计费管理')

    def finance_click_batch_charging_management(self):
        self.click(self.batch_charging_management)
        log.info(u'收费系统主页--点击批量计费管理')
        sleep(2)