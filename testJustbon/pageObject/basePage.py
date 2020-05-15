# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/8 10:45
import os,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from public.publicLogs import PublicLogs
from selenium.webdriver.support import expected_conditions as EC
from public.publicYaml import PublicGetYaml
from public.publicOperate import PublicOperate
log = PublicLogs()
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.operare= PublicOperate(self.driver)

    def find_element(self,element):
        """
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(By.ID,loc))
        WebDriverWait:参数driver实例
                          timeout:超时时间
                          poll_frequency:循环去查询的间隙时间，默认0.5秒
                          until:元素出现,until可以运用匿名函数
        """
        try:
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(type,loc))
            # return self.driver.find_element(type,loc)
            if "=>" in element:
                type = element.split("=>")[0]
                loc = element.split("=>")[1]
                if type =='id':
                    return WebDriverWait(self.driver,10).until(lambda x:x.find_element(By.ID,loc))
                if type =='ids':
                    return WebDriverWait(self.driver,10).until(lambda x:x.find_elements(By.ID,loc))
                if type =='name':
                    return WebDriverWait(self.driver,10).until(lambda x:x.find_element(By.NAME,loc))
                if type =='class_name':
                    return WebDriverWait(self.driver,10).until(lambda x:x.find_element(By.CLASS_NAME,loc))
                if type =='xpath':
                    return WebDriverWait(self.driver,10).until(lambda x:x.find_element(By.XPATH,loc))
                if type=='uia':
                    return WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_android_uiautomator(loc))
        except:
            log.error(u"页面中未能找到 %s 元素"%(element))

    #输入
    def send_keys(self,element,value):
        try:
            self.find_element(element).clear()
            self.find_element(element).send_keys(value)
            time.sleep(1)
        except:
            log.error(u"页面中未能找到 %s 元素"%(element))
            self.operare.screenshot()

    #点击
    def click(self,element):
        try:
            self.find_element(element).click()
            time.sleep(1)
        except:
            log.error(u"页面中未能找到 %s 元素"%(element))
            self.operare.screenshot()

    #
    def clicks(self,element,values):
        try:
            self.find_element(element)[values].click()
        except:
            log.error(u"页面中未能找到 %s 元素"%(element))
            self.operare.screenshot()

    #文本
    def text(self,element):
        try:
            return self.find_element(element).text
        except:
            log.error(u"页面中未能找到 %s 元素"%(element))
            self.operare.screenshot()

    #下拉列表
    def select(self,element,index):
        try:
            s = self.find_element(element)
            Select(s).select_by_index(index)
        except:
            log.error(u"页面中未能找到 %s 元素"%(element))
            self.operare.screenshot()

    #搜索键
    def search(self,element):
        #调搜狗输入法
        os.system("adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME")
        self.click(element)
        self.driver.keyevent(66)
        #屏幕输入法
        os.system("adb shell ime set io.appium.settings/.UnicodeIME")

    #切换h5
    def get_switch_h5(self):
        time.sleep(3)
        self.driver.switch_to.context('WEBVIEW_com.hxdsw.brc')
        # self.driver.switch_to.context(self.driver.contexts[1])
        log.info(u"原生页面切换进入h5页面")

    #切换h5,商城
    def get_switch_h5_shop(self):
        self.driver.switch_to.context(u'WEBVIEW_com.android.quicksearchbox')
        log.info(u"原生页面切换进入h5页面")

    #切换原生
    def get_switch_android(self):
        self.driver.switch_to.context(self.driver.contexts[0])
        log.info(u"h5页面切换原生页面")


    def get_cookies(self):
        with open("config/cookies.json","w") as f:
            f.write(self.driver.get_cookies())


    def get_toast(self,driver,text):
        try:
            toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
            WebDriverWait(driver,10).until(EC.presence_of_element_located(toast_element))
            log.info(u"查找到toast消息---%s"%(text))
            return True
        except:
            log.error(u"未查找到toast消息---%s"%(text))
            return False

    #输入URL并进入
    def get_url(self, url):
        self.driver.get(url)

    #进入frame页面
    def switch_to(self, locate):
        self.driver.switch_to.frame(locate)

    #退出frame到顶层
    def switch_to_out(self):
        self.driver.switch_to.default_content()

    #切换浏览器页面
    def switch_to_window(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    #清除数据
    def clear(self, locate):
        self.find_element(locate).clear()