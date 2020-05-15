# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/4/8 10:46
import os,time
from public.publicLogs import PublicLogs
log=PublicLogs()
import warnings
warnings.simplefilter("ignore", ResourceWarning)

class PublicOperate:
    def __init__(self,driver):
        self.driver=driver

    def get_back(self):
        '''
        :return:返回键
        '''
        os.popen('adb shell input keyevent 4')
        time.sleep(2)
        log.info(u"原生页面操作返回")

    def get_search(self):
        """
        搜索键
        :return:
        """
        return self.driver.press_keycode(84)

    def get_window_size(self):
        '''
        :return:返回屏幕的大小
        '''
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)
    def swipe_up(self):
        '''
        :return:向上滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.5)
            y1=int(l[0]*0.8)
            y2=int(l[1]*0.2)
            self.driver.swipe(x1,y1,x1,y2,1000)
            log.info(u"向上滑动")
            time.sleep(1)
        except:
            log.error(u"上滑动异常")

    def swipe_down(self):
        '''
        :return:向下滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.5)
            y1=int(l[0]*0.3)
            y2=int(l[1]*0.8)
            self.driver.swipe(x1,y1,x1,y2,1000)
            log.info(u"向下滑动")
        except:
            log.error(u"下滑动异常")

    def swipe_right(self):
        '''
        :return:向右滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.2)
            x2=int(l[0]*0.8)
            y1=int(l[1]*0.5)
            self.driver.swipe(x1,y1,x2,y1,1000)
            log.info(u"向右滑动")
        except:
            log.error(u"右滑动异常")

    def swipe_left(self):
        '''
        :return:向左滑动
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.8)
            x2=int(l[0]*0.2)
            y1=int(l[1]*0.5)
            self.driver.swipe(x1,y1,x2,y1,1000)
            log.info(u"向左滑动")
        except:
            log.error(u"左滑动异常")

    def swipe_click(self):
        '''
        :return:坐标点击
        '''
        try:
            l=self.get_window_size()
            x1=int(l[0]*0.5)
            y1=int(l[1]*0.3)
            self.driver.swipe(x1,y1,x1,y1,1000)
            log.info(u"坐标点击")
        except:
            log.error(u"点击异常")

    def screenshot(self):
        '''
        :return:截图
        '''
        nowtime=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
        filename="../img/%s.png"%nowtime
        self.driver.get_screenshot_as_file(filename)