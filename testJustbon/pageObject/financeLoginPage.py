from pageObject.basePage import BasePage
from public.publicLogs import PublicLogs
log = PublicLogs()


class FinanceLoginPage(BasePage):

    input_name = 'xpath=>//div[@class="login_panel"]/div[2]/div[1]/input'
    input_password = 'xpath=>//div[@class="login_panel"]/div[3]/div[1]/input'
    click_login = 'xpath=>//div[@class="login_panel"]/div[4]'

    def finance_input_name(self):
        self.send_keys(self.input_name, 'gaochunlei')
        log.info(u"云平台登录页面--输入账号")

    def finance_input_password(self):
        self.send_keys(self.input_password, 'Gao902913')
        log.info(u"云平台登录页面--输入密码")

    def finance_click_login(self):
        self.click(self.click_login)
        log.info(u"云平台登录页面--点击登录进入")