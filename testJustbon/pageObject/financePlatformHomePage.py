from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
from time import sleep
log = PublicLogs()


class FinancePlatformHomePage(BasePage):

    click_platform_iknow = 'xpath=>//div[@class="txt-center"]/button'
    click_finance = 'xpath=>//ul[@class="ips-page-header-navigation"]/li[11]/a'
    click_iknow = 'id=>headerBlockBtn'

    def finance_click_platform_iknow(self):
        self.click(self.click_platform_iknow)
        log.info(u"平台首页--点击我知道了")
        sleep(1)

    def finance_click_finance(self):
        self.click(self.click_finance)
        log.info(u"平台首页--点击综合收费")
        sleep(12)

    def finance_click_iknow(self):
        self.switch_to_window(1)
        sleep(4)
        log.info(u"平台首页--切换浏览器页面")
        self.click(self.click_iknow)
        log.info(u"收费系统主页--点击我知道了")
        sleep(1)