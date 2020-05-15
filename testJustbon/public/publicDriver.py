# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/8 10:46
import os,time
from appium import webdriver
from public.publicPhone import PublicPhone
from public.publicLogs import  PublicLogs
from public.publicCmd import PublicCmd
from public.publicApk import PublicApk
log =PublicLogs()

def publicDrivers():
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    # post = str(PublicCmd().device_post_list(4727)-1)
    capabilities={}
    capabilities['platformName']='Android'                              #平台
    # capabilities['platformVersion']=PublicPhone().system_version()[0]    #设备id
    # capabilities['deviceName']=PublicCmd().get_device_user()[0]         #设备名称
    # capabilities['appPackage']=PublicApk().getAppInfo()[0]              #包名
    # capabilities['appActivity']=PublicApk().getAppInfo()[1]             #类名

    capabilities['platformVersion']=PublicPhone().system_version()[0]    #设备id
    capabilities['deviceName']=PublicCmd().get_device_user()[0]         #设备名称
    capabilities['appPackage']="com.hxdsw.brc"             #包名
    capabilities['appActivity']="com.hxdsw.brc.ui.AppStart"             #类名

    # capabilities['app']=PATH("..\\apk\\https_debug.apk")#aap路径
    capabilities['unicodeKeyboard'] = True                              #输入中文
    capabilities['resetKeyboard'] = True                                #屏蔽软键盘
    capabilities['noReset'] = True                                      #防止再次安装apk
    # capabilities['automationName']='UiAutomator2'                       #toast消息的参数
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',capabilities)
    time.sleep(5)
    log.info(u"获取成功")
    return driver






