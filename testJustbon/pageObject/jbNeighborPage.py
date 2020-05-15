# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2020/4/1 11:00
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
from config import getLoginElement as element
import time
log = PublicLogs()
class JbNeighborPage(BasePage):
    """
    邻里
    """
    click_forum_post_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/fragment_main_listview']/android.widget.LinearLayout[1]"
    click_fabulous_loc="id=>com.hxdsw.brc:id/tv_praise"
    click_content_loc="id=>com.hxdsw.brc:id/easy_photo_detail_et_comment"
    input_content_loc="id=>com.hxdsw.brc:id/easy_photo_detail_et_comment"
    click_comment_loc="id=>com.hxdsw.brc:id/bt_comment"
    click_posting_loc="id=>com.hxdsw.brc:id/card_push"
    # input_posting_content_loc="id=>com.hxdsw.brc:id/publish_easy_photo_tv_content"
    input_posting_content_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/scroll_ll']/android.widget.LinearLayout/android.widget.RelativeLayout"
    click_picture_icon_loc="id=>com.hxdsw.brc:id/publish_easy_photo_ll_photo"
    click_picture_loc="id=>com.hxdsw.brc:id/dialog_photo_exist_photo"
    click_album_loc="id=>android.miui:id/masklayout"
    click_photo_loc="xpath=>//*[@resource-id='com.miui.gallery:id/grid']/android.widget.RelativeLayout[1]"
    click_release_loc="id=>com.hxdsw.brc:id/bt_publish"
    click_activity_loc="id=>com.hxdsw.brc:id/active"
    click_activity1_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/fragment_party_list']/android.widget.LinearLayout[1]"
    click_market_loc="id=>com.hxdsw.brc:id/market"
    click_markst_post_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/fragment_main_listview']/android.widget.LinearLayout[1]"
    click_market_posting_loc="id=>com.hxdsw.brc:id/iv_card_push"
    input_market_price_loc="id=>input_market_price_loc"
    click_market_classification_loc="id=>com.hxdsw.brc:id/tv_select_class"
    click_market_select_classification_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rclv_kind']/android.widget.LinearLayout[1]"
    input_market_phone_loc="id=>com.hxdsw.brc:id/et_phone_num"
    click_market_release_loc="id=>com.hxdsw.brc:id/bt_publish"

    #业主论坛---点击第一个帖子
    def jbNeighbor_click_forum_post(self):
        self.click(self.click_forum_post_loc)
        log.info("业主论坛页面---点击第一个帖子")

    #业主论坛---点赞
    def jbNeighbor_click_fabulous(self):
        self.click(self.click_fabulous_loc)
        log.info("帖子详情页面---点赞")

    #业主论坛---评论输入内容
    def jbNeighbor_click_content(self):
        self.send_keys(self.click_content_loc)
        log.info("帖子详情页面---点击文本框")

    #业主论坛---评论输入内容
    def jbNeighbor_input_content(self,content):
        self.send_keys(self.input_content_loc,content)
        log.info("帖子详情页面---输入内容:{}".format(content))

    #业主论坛---点击评论
    def jbNeighbor_click_comment(self):
        self.click(self.click_comment_loc)
        log.info("帖子详情页面---点击评论")

    #业主论坛---我要发帖
    def jbNeighbor_click_posting(self):
        self.click(self.click_posting_loc)
        log.info("业主论坛页面---点击我要发帖")

    #点击发帖内容
    def jbNeighbor_click_posting_content(self):
        self.click(self.input_posting_content_loc)
        log.info("发帖页面---点击发帖内容")

    #输入发帖内容
    def jbNeighbor_input_posting_content(self,content):
        self.send_keys(self.input_posting_content_loc,content)
        log.info("发帖页面---输入发帖内容:{}".format(content))

    #点击上传图片图标
    def jbNeighbor_click_picture_icon(self):
        self.click(self.click_picture_icon_loc)
        log.info("发帖页面---点击上传图片图标")

    #点击图片
    def jbNeighbor_click_picture(self):
        self.click(self.click_picture_loc)
        log.info("发帖页面---点击图片")

    #点击相册
    def jbNeighbor_click_album(self):
        self.click(self.click_album_loc)
        log.info("发帖页面---点击相册")

    #选择第一张照片
    def jbNeighbor_click_photo(self):
        self.click(self.click_photo_loc)
        log.info("相册页面---选择第一个照片")

    #立即发布
    def jbNeighbor_click_release(self):
        self.click(self.click_release_loc)
        log.info("发帖页面---点击立即发布")

    #社区活动
    def jbNeighbor_click_activity(self):
        self.click(self.click_activity_loc)
        log.info("邻里页面---点击社区活动")

    #选择第一个活动
    def jbNeighbor_click_activity1(self):
        self.click(self.click_activity1_loc)
        log.info("社区活动页面---点击第一个活动")

    #点击跳蚤市场
    def jbNeighbor_click_market(self):
        self.click(self.click_market_loc)
        log.info("邻里页面---点击跳蚤市场")

    #点击第一个市场帖子
    def jbNeighbor_click_market_post(self):
        self.click(self.click_markst_post_loc)
        log.info("跳蚤市场页面---点击第一个帖子")

    #跳蚤市场发帖
    def jbNeighbor_click_market_posting(self):
        self.click(self.click_market_posting_loc)
        log.info("跳蚤市场页面---点击我要发帖")

    #价格
    def jbNeighbor_input_market_price(self,content):
        self.send_keys(self.input_market_price_loc,content)
        log.info("发布跳蚤市场页面---输入价格:{}".format(content))

    #分类
    def jbNeighbor_click_market_classification(self):
        self.click(self.click_market_classification_loc)
        log.info("发布跳蚤市场页面---点击分类")

    #选择分类
    def jbNeighbor_click_market_select_classification(self):
        self.click(self.click_market_select_classification_loc)
        log.info("选择分类页面---选择分类")

    #手机号
    def jbNeighbor_input_market_phone(self,content):
        self.send_keys(self.input_market_phone_loc,content)
        log.info("发布跳蚤市场页面---输入手机号:{}".format(content))

    #确认发布
    def jbNeighbor_click_market_release(self):
        self.click(self.click_market_release_loc)
        log.info("发布跳蚤市场页面---点击确认发布")























































