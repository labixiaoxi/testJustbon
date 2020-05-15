# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/4/24 9:17
import requests
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
log = PublicLogs()

class JbHomeHeadersPage(BasePage):
    """
    主页面头部信息
    """
    add_loc="id=>com.hxdsw.brc:id/tv_project"
    assert_add_loc=u"id=>com.hxdsw.brc:id/tv_project"
    click_replace_add_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/lv_list"]/android.widget.LinearLayout[2]'
    assert_LimitRow_small_loc=u"id=>com.hxdsw.brc:id/bn_limt_num1"
    assert_LimitRow_large_loc=u"id=>com.hxdsw.brc:id/bn_limt_num2"
    click_advertisement_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/bannerContainer"]/android.support.v4.view.ViewPager/android.widget.ImageView'
    assert_home_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/ll_tab_content"]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.TextView'
    #头部地址
    def homeHeaders_click_add(self):
        self.click(self.add_loc)
        log.info(u"首页页面---点击左上角项目")

    def homeHeaders_click_replace_add(self):
        self.click(self.click_replace_add_loc)
        log.info(u"首页页面---更换项目")

    #头部地址内容
    def homeHeaders_assert_add(self):
        result=self.text(self.assert_add_loc)
        log.info(u"首页页面---断言内容---项目名称:%s"%result)
        return result

    #车辆限行
    def homeHeaders_assert_LimitRow_small(self):
        result=self.text(self.assert_LimitRow_small_loc)
        log.info(u"首页页面---断言内容---车辆限行:%s"%result)
        return result

    #车辆限行
    def homeHeaders_assert_LimitRow_large(self):
        result=self.text(self.assert_LimitRow_large_loc)
        log.info(u"首页页面---断言内容---车辆限行:%s"%result)
        return result

    def homeHeaders_click_advertisement(self):
        self.click(self.click_advertisement_loc)
        log.info(u"首页页面---点击轮播广告")

    def homeHeaders_assert_home(self):
        result = self.text(self.assert_home_loc)
        return result



    def homeHeader_LimitRow_small(self):
        self.url="http://api.justbon.com/weather/queryWeatherInfo.json"
        self.data={"location":"103.965315,30.747719"}
        self.headers={"User-Agent": "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; vivo Y66 Build/MMB29M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                "userId": "2016081014421271859",
                "version": "260",
                "token": "F48C60E726BB0970FF1C35AA01AF2B75",
                "osVersion": "android,6.0.1",
                "imei": "87fa6426-9c95-314a-a2c6-69e4d0d8da87",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "device":"vivo Y66",
                "Content-Type": "application/json;charset=utf-8",
                "Content-Length": "33",
                "Host": "api.justbon.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Cookie":"SERVERID=ae4bddfe118991dadf9bef966aa11aa6|1556190420|1556190420"}
        res=requests.post(url=self.url,json=self.data,headers=self.headers)
        result = res.json()['xx']['xxnum']
        if "," in result:
            small = result.split(",")[0]
            return small
        else:
            log.error(u"response:%s"%(res.content))
            log.error(u"接口返回异常")

    def homeHeader_LimitRow_large(self):
        self.url="http://api.justbon.com/weather/queryWeatherInfo.json"
        self.data={"location":"103.965315,30.747719"}
        self.headers={"User-Agent": "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; vivo Y66 Build/MMB29M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                "userId": "2016081014421271859",
                "version": "260",
                "token": "F48C60E726BB0970FF1C35AA01AF2B75",
                "osVersion": "android,6.0.1",
                "imei": "87fa6426-9c95-314a-a2c6-69e4d0d8da87",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "device":"vivo Y66",
                "Content-Type": "application/json;charset=utf-8",
                "Content-Length": "33",
                "Host": "api.justbon.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Cookie":"SERVERID=ae4bddfe118991dadf9bef966aa11aa6|1556190420|1556190420"}
        res=requests.post(url=self.url,json=self.data,headers=self.headers)
        result = res.json()['xx']['xxnum']
        if "," in result:
            small = result.split(",")[1]
            return small
        else:
            log.error(u"response:%s"%(res.content))
            log.error(u"接口返回异常")













