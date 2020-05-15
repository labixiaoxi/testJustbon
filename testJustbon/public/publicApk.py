# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/8 10:46

import os,re,yaml,datetime
from public.publicLogs import PublicLogs
from public.publicExcel import PublicExcel
log=PublicLogs()
class PublicApk(object):
    def __init__(self):
        self.excel = PublicExcel("../report/locust.xls")

    def pathYaml(self):
        with open('../config/path.yaml','rb') as f:
            result=f.read()
            path=yaml.load(result,Loader=yaml.FullLoader)
            return path

    def getAppInfo(self):
        path=os.path.abspath(os.path.dirname(__file__))+"\\"
        aapt_path=path+self.pathYaml()['path']['aapt']
        apk_path=path+self.pathYaml()['path']['apk']
        get_info_command = "%s dump badging %s" % (aapt_path,apk_path)
        log.info(u"获取包名和类名的命令:"+get_info_command)
        output = os.popen(get_info_command).read()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'[\s\S]*launchable-activity: name='(\S+)'").match(output) #通过正则匹配，获取包名，版本号，版本名称
        if not match:
            raise Exception(u"命令错误,获取失败")
        packagename = match.group(1)
        activityName = match.group(4)
        versionCode = match.group(3)
        versionName = match.group(2)
        log.info( u" 包名：%s ,类名：%s 版本号：%s , 版本名称：%s " % (packagename, activityName,versionCode, versionName))
        write_excel = {"13":packagename,
                       "14":activityName,
                       "2":versionCode
               }
        for key,values in write_excel.items():
            self.excel.write_excel(0,int(key),1,values)
        self.excel.write_excel(1,5,5,datetime.datetime.now())
        return packagename,activityName

    def getlogcatInfo(self):
        path = os.path.dirname(__file__)+"\..\\logs\\logcat.log"
        return os.popen("adb logcat |find 'com.platform.jhj' >%s"%path)


if __name__ == '__main__':
    apk=PublicApk()
    apk.getAppInfo()
    # apk.getlogcatInfo()
