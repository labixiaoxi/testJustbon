# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/10 11:50
import os
from public.publicLogs import PublicLogs
from public.publicExcel import PublicExcel
log=PublicLogs()
import warnings
warnings.simplefilter("ignore", ResourceWarning)
class PublicPhone(object):
    def __init__(self):
        self.excel=PublicExcel("../report/locust.xls")

    def system_version(self):
        '''
        手机系统版本
        :return:
        '''
        return_version=os.popen("adb shell getprop ro.build.version.release").readlines() #设备版本
        return_model=os.popen("adb shell getprop ro.product.model").readlines()           #型号
        return_brand=os.popen("adb shell getprop ro.product.brand").readlines()           #品牌
        return_device=os.popen("adb shell getprop ro.product.device").readlines()         #设备名
        return_webview = os.popen('adb shell dumpsys package com.google.android.webview | find "versionName"').readlines()
        try:
            version = return_version[0].split('\r')[0]
            model = return_model[0].split('\r')[0]
            brand = return_brand[0].split('\r')[0]
            device = return_device[0].split('\r')[0]
            webview = return_webview[0].split('=')[1]
            log.info(u"设备:%s , 型号:%s, 品牌:%s, 设备名:%s,view版本:%s"%(version,model,brand,device,webview))
            return version,model,brand,device,webview
        except:
            log.info("设备连接异常或设备连接多个")

    def system_phone_pix(self):
        """
        获取分辨率
        :return:

        """
        pix = os.popen("adb shell wm size")
        result= pix.readline().split("Physical size: ")[1]
        log.info("手机分辨率:"+result)
        return result


    def write_excel(self):
        write_excel = {"8":self.system_version()[1],
                       "9":self.system_version()[2],
                       "10":self.system_phone_pix(),
                       "11":self.system_version()[0],
                       "12":self.system_version()[4]
                       }
        for key,values in write_excel.items():
            self.excel.write_excel(0,int(key),1,values)

if __name__ == '__main__':
    phone = PublicPhone()
    print (phone.system_version())
    # print (phone.system_phone_pix())
    # phone.write_excel()
