# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/5/23 9:58
from public.publicApk import PublicApk
class RunLogcat:
    def get_logcat(self):
        print (u"----------start_logcat---------------------------")
        PublicApk().getlogcatInfo()

if __name__ == '__main__':
    run = RunLogcat()
    run.get_logcat()