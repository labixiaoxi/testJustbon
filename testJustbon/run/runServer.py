# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/5/23 9:58
import os
import sys
sys.path.append("D:\\code\\testJb")
import platform
from public.publicCmd import PublicCmd
from public.publicLogs import PublicLogs
log = PublicLogs
class AppiumServer:
    def __init__(self):
        self.server = PublicCmd()

    def start_server(self):
        if platform.system() == 'Windows':
            print (u"----------start_appium---------------------------")
            self.server.server_command()

if __name__ == '__main__':
    appium = AppiumServer()
    appium.start_server()
