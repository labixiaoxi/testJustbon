# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/8 11:27
import requests,json,time,selenium
from appium import webdriver
from public.publicOperate import PublicOperate

capabilities={}
capabilities['platformName']='Android'
capabilities['platformDevice']="6.0.1"
capabilities['deviceName']="5376f2f6"
capabilities['appPackage']="com.hxdsw.brc"
capabilities['appActivity']="com.hxdsw.brc.ui.AppStart"
# capabilities['app']="..\\apk\\test-v3.5.0.builder20190417.apk"
capabilities['unicodeKeyboard'] = True                              #输入中文
capabilities['resetKeyboard'] = True                                #屏蔽软键盘
capabilities['noReset'] = True                                      #防止再次安装apk
# capabilities['recreateChromeDriverSessions']=True
# capabilities['showChromedriverLog']=True
capabilities['automationName']='UiAutomator2'                       #toast消息的参数
capabilities['chromeOptions']={'androidProcess':'com.hxdsw.brc'}
# capabilities['chromedriverExecutable']="C:\\Users\\Chenyang Yue\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\win\\chromedriver.exe"

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',capabilities)
time.sleep(10)
driver.find_element_by_id('com.justbon.oa:id/rl_module_more').click()
result = driver.find_element_by_xpath('xpath=>//*[@resource-id="com.justbon.oa:id/rv_modules"]/android.widget.LinearLayout[%s]/android.widget.TextView'%i)











