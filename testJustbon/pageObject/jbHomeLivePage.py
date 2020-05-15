# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/5/16 11:34
import requests,random,os,time
from public.publicLogs import PublicLogs
from pageObject.basePage import BasePage
log = PublicLogs()

class JbHomeSelectedPage(BasePage):
    """
    嘉宝精选
    """
    click_selected_loc="id=>com.hxdsw.brc:id/home_mid_1"
    click_page1_loc='xpath=>/html/body/div[2]/ul/li[1]'
    click_page2_loc='xpath=>/html/body/div/div[1]/a[1]'
    click_page3_loc='xpath=>//*[@id="JD-2098907"]/a/div[1]/img'
    click_page4_loc='xpath=>//*[@id="J_buy_btn"]'

    #嘉宝精选
    def jbHomeSelected_click_selected(self):
        self.click(self.click_selected_loc)
        log.info(u"首页页面---点击嘉宝精选")

    def jbHomSelected_click_page1(self):
        self.click(self.click_page1_loc)
        time.sleep(2)
        log.info(u"嘉宝精选---点击专享98折")

    def jbHomSelected_click_page2(self):
        self.click(self.click_page2_loc)
        time.sleep(2)
        log.info(u"综合商城---进入家用电器")

    def jbHomSelected_click_page3(self):
        self.click(self.click_page3_loc)
        time.sleep(2)
        log.info(u"综合商城---选择第一个产品")

    def jbHomSelected_click_page4(self):
        self.click(self.click_page4_loc)
        time.sleep(2)
        log.info(u"商品详情---加入购物车")





class JbHomeWaterPage(BasePage):
    """
    送水上门
    """
    click_water_loc ="id=>com.hxdsw.brc:id/home_mid_3"
    click_waterPicture_loc='xpath=>//div[@id="app"]/div/div[3]/ul/a'
    click_addNum_loc='xpath=>//div[@id="app"]/div/div[2]/div[3]/div/span/span[2]'
    click_pay_loc='xpath=>//div[@id="app"]/div/div[2]/nav/a'
    click_giveWater_loc='xpath=>//*[@id="app"]/div/nav/a[2]'
    click_tips_loc='xpath=>//*[@id="app"]/div/div[4]/div/div[3]/div/span'
    click_personal_loc='xpath=>//*[@id="app"]/div/nav/a[3]'
    click_order_loc='xpath=>//*[@id="app"]/div/div[2]/div[2]/a[1]/div'
    click_stayDelivery_loc='xpath=>//*[@id="app"]/div/div[2]/div[2]'
    click_delivery_loc='xpath=>//*[@id="app"]/div/div[2]/div[3]'
    click_deliveryComplete_loc='xpath=>//*[@id="app"]/div/div[2]/div[4]'
    click_deliveryAbnormal_loc='xpath=>//*[@id="app"]/div/div[2]/div[5]'
    click_ticket_loc='xpath=>//*[@id="app"]/div/div[2]/div[2]/a[3]/div'
    click_address_loc="xpath=>//div[@class='group']/a[3]"
    click_newAddress_loc='xpath=>//*[@id="app"]/div/nav/a'
    click_province_loc='xpath=>//*[@id="app"]/div/div[3]/div/div[3]/div[2]'
    click_determineProvince_loc='xpath=>//*[@id="app"]/div/div[4]/div[2]/div[1]/span[1]'
    click_village_loc='xpath=>//*[@id="app"]/div/div[3]/div/div[4]/div[2]'
    click_determineVillage_loc='xpath=>//*[@id="app"]/div/div[4]/div/div[2]/div/div[2]/div[1]'
    input_detailedAddress_loc='xpath=>//*[@id="tangram-suggestion--TANGRAM__1k-input"]'
    input_houseNumber_loc='//*[@id="app"]/div/div[3]/div[1]/div[5]/div[2]/input'
    click_waterStation_loc='xpath=>//*[@id="app"]/div/div[3]/div[2]/div[2]'
    click_confirm_loc='xpath=>//*[@id="app"]/div/nav/a'
    click_edit_loc='xpath=>//*[@id="scrollwarper"]/div[1]/div[2]/div/span[2]/span'
    click_deposit_loc='xpath=>//*[@id="app"]/div/div[2]/div[2]/a[4]/div'

    def jbHomeWater_click_water(self):
        self.click(self.click_water_loc)
        log.info(u"首页页面---点击送水上门")

    #点击水图片
    def jbHomeWater_click_waterPicture(self):
        time.sleep(2)
        self.click(self.click_waterPicture_loc)
        log.info(u"蓝光桶装水页面---点击天然山泉")

    #新增购买数量
    def jbHomeWater_click_addNum(self):
        self.click(self.click_addNum_loc)
        log.info(u"一键购水页面---添加购买数量")

    #去支付
    def jbHomeWater_click_pay(self):
        self.click(self.click_pay_loc)
        log.info(u"一键购水页面---点击去支付")

    #预约送水
    def jbHomeWater_click_giveWater(self):
        self.click(self.click_giveWater_loc)
        log.info(u"个人中心页面---切换到预约送水")

    #关闭提示
    def jbHomeWater_click_tips(self):
        self.click(self.click_tips_loc)
        log.info(u"个人中心页面---关闭提示")

    #个人中心
    def jbHomeWater_click_personal(self):
        self.click(self.click_personal_loc)
        log.info(u"个人中心页面---切换到个人中心")

    #我的订单
    def jbHomeWater_click_order(self):
        self.click(self.click_order_loc)
        log.info(u"个人中心页面---点击我的订单")

    #待配送
    def jbHomeWater_click_stayDelivery(self):
        self.click(self.click_stayDelivery_loc)
        log.info(u"我的订单页面---点击待配送")

    #配送中
    def jbHomeWater_click_deliveryIn(self):
        self.click(self.click_delivery_loc)
        log.info(u"我的订单页面---点击配送中")

    #配送完成
    def jbHomeWater_click_deliveryComplete(self):
        self.click(self.click_deliveryComplete_loc)
        log.info(u"我的订单页面---点击配送完成")

    #配送异常
    def jbHomeWater_click_deliveryAbnormal(self):
        self.click(self.click_deliveryAbnormal_loc)
        log.info(u"我的订单页面---点击配送异常")

    #我的水票
    def jbHomeWater_click_ticket(self):
        self.click(self.click_ticket_loc)
        log.info(u"个人中心页面---点击我的水票")

    #我的地址
    def jbHomeWater_click_address(self):
        self.click(self.click_address_loc)
        log.info(u"个人中心页面---点击我的地址")

    #新增收货地址
    def jbHomeWater_click_newAddress(self):
        self.click(self.click_newAddress_loc)
        log.info(u"选择地址页面---点击新增收货地址")

    #点击省市区
    def jbHomeWater_click_province(self):
        self.click(self.click_province_loc)
        log.info(u"新增编辑收货地址---点击省市区")

    #确定省市区
    def jbHomeWater_click_determineProvince(self):
        self.click(self.click_determineProvince_loc)
        log.info(u"新增编辑收货地址---点击选择的省市区")

    #点击小区
    def jbHomeWater_click_village(self):
        self.click(self.click_village_loc)
        log.info(u"新增编辑收货地址---点击小区")

    #选择小区
    def jbHomeWater_click_determineVillage(self):
        self.click(self.click_determineVillage_loc)
        log.info(u"新增编辑收货地址---点击选择的小区")

    #详细地址
    def jbHomeWater_input_detailedAddress(self,address):
        self.click(self.input_detailedAddress_loc)
        self.send_keys(self.input_detailedAddress_loc,address)
        log.info(u"新增编辑收货地址---输入详细地址:%s"%address)

    # def test(self):
    #     test='xpath=>//*[@id="tangram-suggestion--TANGRAM__5t"]/div/span'
    #     self.click(test)

    #门牌号
    def jbHomeWater_input_houseNumber(self,values):
        self.send_keys(self.input_houseNumber_loc,values)
        log.info(u"新增编辑收货地址---输入门牌号:%s"%values)

    #关联水站
    def jbHomeWater_click_waterStation(self):
        self.click(self.click_waterStation_loc)
        log.info(u"新增编辑收货地址---选择关联水站")

    #确认
    def jbHomeWater_click_confirm(self):
        self.click(self.click_confirm_loc)
        time.sleep(3)
        log.info(u"新增编辑收货地址---点击确认")


    #编辑收货地址
    def jbHomeWater_click_edit(self):
        self.click(self.click_edit_loc)
        log.info(u"选择地址页面---点击编辑按钮")

    #我的押金
    def jbHomeWater_click_deposit(self):
        self.click(self.click_deposit_loc)
        log.info(u"个人中心页面---点击我的押金")



class JbHomeCheckInPage(BasePage):
    """
    拎包入住
    """
    click_checkIn_loc="id=>com.hxdsw.brc:id/home_mid_4"
    click_rmhd_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[1]"
    click_cggd_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[2]"
    click_zxgj_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[3]"
    click_jpal_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[4]"
    click_jffx_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[5]"
    click_jjsc_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[6]"
    click_xsjs_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[7]"
    click_tgc_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_tab']/android.widget.LinearLayout[8]"

    def jbHomeCheckIn_click_checkIn(self):
        self.click(self.click_checkIn_loc)
        log.info(u"首页页面---点击拎包入住")

    def jbHomeCheckIn_click_rmhd(self):
        self.click(self.click_rmhd_loc)
        log.info(u"拎包入住页面---点击热门活动")

    def jbHomeCheckIn_click_cggd(self):
        self.click(self.click_cggd_loc)
        log.info(u"拎包入住页面---点击参观工地")

    def jbHomeCheckIn_click_zxgj(self):
        self.click(self.click_zxgj_loc)
        log.info(u"拎包入住页面---点击装修管家")

    def jbHomeCheckIn_click_jpal(self):
        self.click(self.click_jpal_loc)
        log.info(u"拎包入住页面---点击精品案例")

    def jbHomeCheckIn_click_jffx(self):
        self.click(self.click_jffx_loc)
        log.info(u"拎包入住页面---点击旧房翻新")

    def jbHomeCheckIn_click_jjsc(self):
        self.click(self.click_jjsc_loc)
        log.info(u"拎包入住页面---点击家具商城")

    def jbHomeCheckIn_click_xsjs(self):
        self.click(self.click_xsjs_loc)
        log.info(u"拎包入住页面---点击选设计师")

    def jbHomeCheckIn_click_tgc(self):
        self.click(self.click_tgc_loc)
        log.info(u"拎包入住页面---点击挑工长")



class JbHomeHousePage(BasePage):
    """
    房屋租售
    """
    click_house_loc="id=>com.hxdsw.brc:id/home_mid_2"
    click_icon_loc="id=>com.hxdsw.brc:id/tv_action"
    click_my_housing_resources_loc="id=>com.hxdsw.brc:id/my_house"
    click_my_publish_parking_loc="id=>com.hxdsw.brc:id/my_parkin_space"
    click_my_screenShops_loc="id=>com.hxdsw.brc:id/my_shops"
    click_search_loc="id=>com.hxdsw.brc:id/rl_search_house"
    input_content_loc="id=>com.hxdsw.brc:id/et_search"
    click_content_name_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_village"]/android.widget.LinearLayout[1]'
    click_first_screenHouse_loc='xpath=>//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout'
    click_screenHouse_loc="id=com.hxdsw.brc:id/tv_type"
    click_screenFlats_loc=""
    click_screenOffice_loc=""
    click_screenParking_loc=""
    click_screenShops_loc=""
    click_list_house_loc="xpath=>//*[@resource-id='android:id/list']/android.widget.RelativeLayout[1]"
    assert_title_loc="id=>com.hxdsw.brc:id/tv_title"
    click_title_result_loc="id=>com.hxdsw.brc:id/tv_title"
    click_houseName1_loc="id=>com.hxdsw.brc:id/text"
    click_houseName2_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rcl_village"]/android.widget.LinearLayout[1]'
    click_newHouse_loc="id=>com.hxdsw.brc:id/tv_new_house"
    click_secondHandHouse_loc="id=>com.hxdsw.brc:id/tv_second_hand_house"
    click_rentHouse_loc="id=>com.hxdsw.brc:id/tv_rent_house"
    click_publishHouse_loc="id=>com.hxdsw.brc:id/tv_public_house"
    click_findHouse_loc="id=>com.hxdsw.brc:id/tv_find_house"
    input_findHouse_title_loc="id=>com.hxdsw.brc:id/et_rent_title"
    click_price_loc="id=>com.hxdsw.brc:id/rl_price_bar"
    click_screenPrice_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/ll_container']/android.widget.TextView[2]"
    click_publish_screenHouse_loc="id=>com.hxdsw.brc:id/rl_residential"
    click_publish_flats_loc="id=>com.hxdsw.brc:id/rl_apartment"
    click_publish_office_loc="id=>com.hxdsw.brc:id/rl_office_building"
    click_publish_parking_loc="id=>com.hxdsw.brc:id/rl_parking_space"
    click_publish_shops_loc="id=>com.hxdsw.brc:id/rl_shops"
    input_leaseHouse_title_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/sv_content"]/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.EditText'
    input_leaseHouse_price_loc="id=>com.hxdsw.brc:id/et_house_price"
    click_leaseHouse_province_city_loc="id=>com.hxdsw.brc:id/tv_province"
    click_leaseHouse_province_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rv_province"]/android.widget.TextView[4]'
    click_leaseHouse_city_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rv_city"]/android.widget.TextView[5]'
    click_leaseHouse_area_loc='xpath=>//*[@resource-id="com.hxdsw.brc:id/rv_county"]/android.widget.TextView[1]'
    click_leaseHouse_village_loc="id=>com.hxdsw.brc:id/tv_project"
    input_leaseHouse_village_loc='id=>com.hxdsw.brc:id/et_search'
    click_leaseHouse_village_name_loc='id=>com.hxdsw.brc:id/text'
    input_leaseHouse_pay_loc="id=>com.hxdsw.brc:id/tv_pay_type"
    click_leaseHouse_selectPay_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[1]"
    input_leaseHouse_built_loc="id=>com.hxdsw.brc:id/et_build_time"
    click_leaseHouse_renovation_loc="id=>com.hxdsw.brc:id/rb_normal_decoration"
    click_leaseHouse_apartment_loc="id=>com.hxdsw.brc:id/tv_house_layout"
    click_leaseHouse_selectApartment_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[3]"
    click_leaseHouse_orientation_loc="id=>com.hxdsw.brc:id/tv_house_orientation"
    click_leaseHouse_selectOrientation_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[3]"
    input_leaseHouse_area_loc="id=>com.hxdsw.brc:id/et_house_area"
    input_leaseHouse_floor_loc="id=>com.hxdsw.brc:id/et_floor"
    input_leaseHouse_floorAll_loc="id=>com.hxdsw.brc:id/et_floor_sum"
    click_leaseHouse_pictrue_loc="id=>com.hxdsw.brc:id/iv_img1"
    click_leaseHouse_gallery_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[1]"
    click_leaseHouse_album_loc="xpath=>//*[@resource-id='android.miui:id/resolver_grid']/android.widget.LinearLayout[1]"
    click_leaseHouse_photo_loc="xpath=>//*[@resource-id='com.miui.gallery:id/grid']/android.widget.RelativeLayout[1]"
    click_leaseHouse_parking_loc="id=>com.hxdsw.brc:id/tv_parking_space_type"
    click_leaseHouse_select_parking_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[1]"
    click_leaseHouse_shops_floor_loc="id=>com.hxdsw.brc:id/tv_floor"
    click_leaseHouse_select_shops_floor_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[1]"
    click_leaseHouse_release_loc="id=>com.hxdsw.brc:id/action_btn"
    click_leaseParking_parking_type_loc="id=>com.hxdsw.brc:id/tv_parking_space_type"
    click_leaseParking_selectParking_type_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[1]"
    click_leaseParking_floor_type_loc="id=>com.hxdsw.brc:id/tv_floor"
    click_leaseParking_selectFloor_type_loc='xpath=>//*[@resource-id="android:id/select_dialog_listview"]/android.widget.TextView[2]'
    click_sell_loc="id=>com.hxdsw.brc:id/rb_sell"
    click_seek_screenOffice_price_loc="id=>com.hxdsw.brc:id/tv_price_interval"
    click_select_seek_screenOffice_price_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[1]"
    click_select_seek_area_loc="xpath=>//*[@resource-id='android:id/select_dialog_listview']/android.widget.TextView[1]"
    click_pzxx_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_recommend']/android.widget.RelativeLayout[1]"
    click_tzsw_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_recommend']/android.widget.RelativeLayout[2]"
    click_jxcw_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_recommend']/android.widget.RelativeLayout[3]"
    click_zzfw_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/gv_recommend']/android.widget.RelativeLayout[4]"
    click_findHouse_title_loc="id=>com.hxdsw.brc:id/et_rent_title"
    click_findHouse_areas_loc="id=>com.hxdsw.brc:id/tv_house_area"


    def jbHomeCheck_click_house(self):
        self.click(self.click_house_loc)
        log.info(u"首页页面---点击房屋租售")

    #右上角图标
    def jbHomeCheck_click_icon(self):
        self.click(self.click_icon_loc)
        log.info("房屋租售页面---点击右上角图标")

    #我的房源
    def jbHomeCheck_click_my_housing_resources(self):
        self.click(self.click_my_housing_resources_loc)
        log.info("房屋租售页面---点击我的房源")

    #我的车位
    def jbHomeCheck_click_my_publish_parking(self):
        self.click(self.click_my_publish_parking_loc)
        log.info("房屋租售页面---点击我的车位")

    #我的商铺
    def jbHomeCheck_click_my_screenShops(self):
        self.click(self.click_my_screenShops_loc)
        log.info("房屋租售页面---点击我的商铺")

    #搜索栏
    def  jbHomeCheck_click_search(self):
        self.click(self.click_search_loc)
        log.info(u"房屋租售页面---点击搜索栏")

    #搜索栏输入内容
    def jbHomeCheck_input_content(self,content):
        self.send_keys(self.input_content_loc,content)
        time.sleep(1)
        self.search(self.input_content_loc)
        log.info(u"搜索页面---输入内容:%s"%content)

    #选择输入的内容
    def jbHomeCheck_click_content_name(self):
        self.click(self.click_content_name_loc)
        log.info(u"搜索页面---选择搜索的内容")

    #第一个住宅
    def jbHomeCheck_click_first_screenHouse(self):
        self.click(self.click_first_screenHouse_loc)
        log.info("搜索小区页面---点击第一个住宅")

    #住宅
    def jbHomeCheck_click_screenHouse(self):
        self.click(self.click_screenHouse_loc)
        log.info(u"搜索页面---点击住宅")

    #切换到公寓
    def jbHomeCheck_click_screenFlats(self):
        self.click(self.click_screenFlats_loc)
        log.info(u"搜索页面---点击公寓")

    #切换到写字楼
    def jbHomeCheck_click_screenOffice(self):
        self.click(self.click_screenOffice_loc)
        log.info(u"搜索页面---点击住宅")

    #切换到车位
    def jbHomeCheck_click_screenParking(self):
        self.click(self.click_screenParking_loc)
        log.info(u"搜索页面---点击车位")

    #切换到商铺
    def jbHomeCheck_click_screenShops(self):
        self.click(self.click_screenShops_loc)
        log.info(u"搜索页面---点击商铺")

    #点击第一个房屋
    def jbHomeCheck_click_list_house(self):
        try:
            self.click(self.click_list_house_loc)
            log.info(u"搜索页面---点击第一个房屋")
        except:
            log.info(u"搜索页面---页面无数据")

    #获取"搜索小区"名称
    def jbHomeCheck_assert_title(self):
        result = self.text(self.assert_title_loc)
        log.info(u"搜索小区页面---页面标题:%s"%result)


    #搜索小区调软键盘点击搜索键
    def jbHomeCheck_click_title_result(self):
        self.search(self.click_title_result_loc)
        log.info(u"搜索小区页面---调软件盘点击搜索键")



    def jbHomeCheck_click_houseName(self):
        try:
            #搜索列表只有1个
            self.click(self.click_houseName1_loc)
            log.info(u"搜索小区页面---点击搜索第一个结果")
        except:
            #搜索列表有很多
            self.click(self.click_houseName2_loc)
            log.info(u"搜索小区页面---点击搜索第一个结果")


    #买新房
    def jbHomeCheck_click_newHouse(self):
        self.click(self.click_newHouse_loc)
        log.info(u"房屋租售---点击买新房")

    #二手房
    def jbHomeCheck_click_secondHandHouse(self):
        self.click(self.click_secondHandHouse_loc)
        log.info(u"房屋租售---点击二手房")

    #出租房
    def jbHomeCheck_click_rentHouse(self):
        self.click(self.click_rentHouse_loc)
        log.info(u"房屋租售---点击出租房")

    #发布资源
    def jbHomeCheck_click_publishHouse(self):
        self.click(self.click_publishHouse_loc)
        log.info(u"房屋租售---点击发布资源")

    #帮我找
    def jbHomeCheck_click_findHouse(self):
        self.click(self.click_findHouse_loc)
        log.info(u"房屋租售---点击帮我找")

    # #帮我找_住宅_标题
    # def jbHomeCheck_input_findHouse_title(self,content):
    #     self.send_keys(self.input_findHouse_title_loc,content)
    #     log.info("输入标题:{}".format(content))
    #
    # #帮我找_住宅_面积
    # def jbHomeCheck_click_findHouse_areas(self):
    #     self.click(self.click_findHouse_areas_loc)


    #不限价格
    def jbHomeCheck_click_price(self):
        self.click(self.click_price_loc)
        log.info(u"买新房页面---点击不限价格")

    #选择价格
    def jbHomeCheck_click_screenPrice(self):
        self.click(self.click_screenPrice_loc)
        log.info(u"买新房页面---筛选价格:30万以下")

    #发布类别_住宅
    def jbHomeCheck_click_publish_screenHouse(self):
        self.click(self.click_publish_screenHouse_loc)
        log.info(u"选择发布类别页面---点击住宅")

    #发布类别_公寓
    def jbHomeCheck_click_publish_flats(self):
        self.click(self.click_publish_flats_loc)
        log.info(u"选择发布类别页面---点击公寓")

    #发布类别_写字楼
    def jbHomeCheck_click_publish_office(self):
        self.click(self.click_publish_office_loc)
        log.info(u"选择发布类别页面---点击写字楼")

    #发布类别_车位
    def jbHomeCheck_click_publish_parking(self):
        self.click(self.click_publish_parking_loc)
        log.info(u"选择发布类别页面---点击车位")

    #发布类别_商铺
    def jbHomeCheck_click_publish_shops(self):
        self.click(self.click_publish_shops_loc)
        log.info(u"选择发布类别页面---点击商铺")

    #住宅出租填写标题
    def jbHomeCheck_input_leaseHouse_title(self,title):
        self.send_keys(self.input_leaseHouse_title_loc,title)
        log.info(u"填写标题:%s"%title)

    #住宅出租填写价格
    def jbHomeCheck_input_leaseHouse_price(self,price):
        self.send_keys(self.input_leaseHouse_price_loc,price)
        log.info(u"填写价格:%s"%price)

    #点击省市区
    def JbHomeCheck_click_leaseHouse_province_city(self):
        self.click(self.click_leaseHouse_province_city_loc)
        log.info(u"点击省市区")

    #选择省
    def jbHomeCheck_click_leaseHouse_province(self):
        self.click(self.click_leaseHouse_province_loc)
        log.info(u"选择:四川省")

    #选择市
    def jbHomeCheck_click_leaseHouse_city(self):
        self.click(self.click_leaseHouse_city_loc)
        log.info(u"选择:成都市")

    #选择区
    def jbHomeCheck_click_leaseHouse_area(self):
        self.click(self.click_leaseHouse_area_loc)
        log.info(u"选择:成华区")

    #点击所在小区
    def jbHomeCheck_click_leaseHouse_village(self):
        self.click(self.click_leaseHouse_village_loc)
        log.info(u"点击所在小区")

    #输入小区名字
    def jbHomeCheck_input_leaseHouse_village(self,village_name):
        self.send_keys(self.input_leaseHouse_village_loc,village_name)
        log.info(u"输入小区名字:%s"%village_name)

    #选择填写的小区名字
    def jbHomeCheck_click_leaseHouse_village_name(self):
        self.click(self.click_leaseHouse_village_name_loc)
        log.info(u"点击填写的小区")

    #点击支付方式
    def jbHomeCheck_input_leaseHouse_pay(self):
        self.click(self.input_leaseHouse_pay_loc)
        log.info(u"点击支付方式")

    #选择支付方式
    def jbHomeCheck_click_leaseHouse_selectPay(self):
        self.click(self.click_leaseHouse_selectPay_loc)
        log.info(u"选择支付方式:月付(押1)")

    #输入建成年份
    def jbHomeCheck_input_leaseHouse_built(self,built_time):
        self.send_keys(self.input_leaseHouse_built_loc,built_time)
        log.info(u"输入建成年份:%s"%built_time)

    #选择装修情况
    def jbHomeCheck_click_leaseHouse_renovation(self):
        self.click(self.click_leaseHouse_renovation_loc)
        log.info(u"选择普通装修")

    #点击户型
    def jbHomeCheck_click_leaseHouse_apartment(self):
        self.click(self.click_leaseHouse_apartment_loc)
        log.info(u"点击户型")

    #选择户型
    def jbHomeCheck_click_leaseHouse_selectApartment(self):
        self.click(self.click_leaseHouse_selectApartment_loc)
        log.info(u"选择户型:3室2厅1卫")

    #点击朝向
    def jbHomeCheck_click_leaseHouse_orientation(self):
        self.click(self.click_leaseHouse_orientation_loc)
        log.info(u"点击朝向")

    #选择朝向
    def jbHomeCheck_click_leaseHouse_selectOrientation(self):
        self.click(self.click_leaseHouse_selectOrientation_loc)
        log.info(u"选择朝向:南北")

    #点击面积
    def jbHomeCheck_click_leaseHouse_areas(self):
        time.sleep(1)
        self.click(self.input_leaseHouse_area_loc)
        log.info(u"点击面积")

    #输入面积
    def jbHomeCheck_input_leaseHouse_area(self,content):
        self.send_keys(self.input_leaseHouse_area_loc,content)
        log.info(u"输入面积:%s"%content)

    #点击所在楼层
    def jbHomeCheck_click_leaseHouse_floor(self):
        self.click(self.input_leaseHouse_floor_loc)
        log.info(u"点击所在楼层")

    #输入所在楼层
    def jbHomeCheck_input_leaseHouse_floor(self,content):
        self.send_keys(self.input_leaseHouse_floor_loc,content)
        log.info(u"输入所在楼层:%s"%content)

    #点击总楼层
    def jbHomeCheck_click_leaseHouse_floorAll(self):
        self.click(self.input_leaseHouse_floorAll_loc)
        log.info(u"输入总楼层")

    #输入总楼层
    def jbHomeCheck_input_leaseHouse_floorAll(self,content):
        self.send_keys(self.input_leaseHouse_floorAll_loc,content)
        log.info(u"输入总楼层:%s"%content)

    #点击上传图片
    def jbHomeCheck_click_leaseHouse_picture(self):
        time.sleep(2)
        self.click(self.click_leaseHouse_pictrue_loc)
        log.info("点击上传图片")

    #图库
    def jbHomeCheck_click_leaseHouse_gallery(self):
        self.click(self.click_leaseHouse_gallery_loc)
        log.info("点击图库")

    #相册
    def jbHomeCheck_click_leaseHouse_album(self):
        self.click(self.click_leaseHouse_album_loc)
        log.info("点击相册")

    #选择第一张照片
    def jbHomeCheck_click_leaseHouse_photo(self):
        self.click(self.click_leaseHouse_photo_loc)
        log.info("选择第一张照片")

    #车位类型
    def jbHomeCheck_click_leaseHouse_parking(self):
        self.click(self.click_leaseHouse_parking_loc)
        log.info("点击车位类型")

    #选择车位类型
    def jbHomeCheck_click_leaseHouse_select_parking(self):
        self.click(self.click_leaseHouse_select_parking_loc)
        log.info("选择车位类型")

    #商铺_所在楼层
    def jbHomeCheck_click_leaseHouse_shops_floor(self):
        self.click(self.click_leaseHouse_shops_floor_loc)
        log.info("点击所在楼层")

    #商铺_选择所在楼层
    def jbHomeCheck_click_leaseHouse_select_shops_floor(self):
        self.click(self.click_leaseHouse_select_shops_floor_loc)
        log.info("点击所在楼层")


    #点击车位类型
    def jbHomeCheck_click_leaseParking_parking_type(self):
        self.click(self.click_leaseParking_parking_type_loc)
        log.info(u"出租页面---点击车位类型")

    #选择车位类型
    def jbHomeCheck_click_leaseParking_selectParking_type(self):
        self.click(self.click_leaseParking_selectParking_type_loc)
        log.info(u"出租页面---选择车位类型:标准车位")

    #点击所在楼层
    def jbHomeCheck_click_leaseParking_floor_type(self):
        self.click(self.click_leaseParking_floor_type_loc)
        log.info(u"出租页面---点击所在楼层")

    #选择负一层
    def jbHomeCheck_click_leaseParking_selectFloor_type(self):
        self.click(self.click_leaseParking_selectFloor_type_loc)
        log.info(u"出租页面---选择所在楼层:负一层")

    #出售
    def jbHomeCheck_click_sell(self):
        self.click(self.click_sell_loc)
        log.info(u"房屋租售---点击出售")

    #求租_公寓
    def jbHomeCheck_click_explore_market_potential(self):
        self.click(self.click_sell_loc)
        log.info(u"点击求售")

    #求租_住宅_点击价格范围
    def jbHomeCheck_click_seek_screenOffice_price(self):
        self.click(self.click_seek_screenOffice_price_loc)
        log.info("点击价格范围")

    #求租_住宅_选择价格范围
    def jbHomeCheck_click_select_seek_screenOffice_price(self):
        self.click(self.click_select_seek_screenOffice_price_loc)
        log.info("选择价格范围")

    #求租_住宅_选择面积
    def jbHomeCheck_click_select_seek_area(self):
        self.click(self.click_select_seek_area_loc)
        log.info("选择面积")

    #发布
    def jbHomeCheck_click_leaseHouse_release(self):
        self.click(self.click_leaseHouse_release_loc)
        log.info(u"点击发布")

    #品质新盘
    def jbHomeCheck_click_pzxx(self):
        self.click(self.click_pzxx_loc)
        log.info(u"房屋出售---点击品质新盘")

    #投资首选
    def jbHomeCheck_click_tzsx(self):
        self.click(self.click_tzsw_loc)
        log.info(u"房屋出售---点击投资首选")

    #精选车位
    def jbHomeCheck_click_jxcw(self):
        self.click(self.click_jxcw_loc)
        log.info(u"房屋出售---点击精选车位")

    #增值服务
    def jbHomeCheck_click_zzfw(self):
        self.click(self.click_zzfw_loc)
        log.info(u"房屋出售---点击增值服务")

    #帮我找_标题
    def jbHomeCheck_input_findHouse_title(self,content):
        self.send_keys(self.click_findHouse_title_loc,content)
        log.info("输入标题:{}".format(content))

    #帮我找_面积
    def jbHomeCheck_click_findHouse_areas(self):
        self.click(self.click_findHouse_areas_loc)
        log.info("点击面积")

class JbHomeParcelPage(BasePage):
    """
    我的邮包
    """
    click_parcel_loc="id=>com.hxdsw.brc:id/home_mid_5"

    def jbHomeParcel_click_parcel(self):
        self.click(self.click_parcel_loc)
        log.info(u"首页页面---点击我的邮包")

class JbHomePreferentialPage(BasePage):
    """
    每日特惠
    """
    click_preferential_loc = "id=>com.hxdsw.brc:id/home_mid_6"
    click_product_loc='xpath=>/html/body/div[5]/div[1]/div/ul/li[2]/a/div[1]/img'
    click_purchase_loc='xpath=>/html/body/div[2]/a[2]'
    click_submitOrder_loc='xpath=>//*[@id="os_1561513861"]'

    #每日特惠
    def jbHomePreferential_click_preferential(self):
        self.click(self.click_preferential_loc)
        log.info(u"首页页面---点击每日特惠")

    #第二个产品
    def jbHomePreferential_click_product(self):
        self.click(self.click_product_loc)
        log.info(u"每日特惠页面---点击第二个产品")

    #立即购买
    def jbShop_click_purchase(self):
        self.click(self.click_purchase_loc)
        log.info(u"商品详情页面---点击立即购买")

    #提交订单
    def jbShop_click_submitOrder(self):
        self.click(self.click_submitOrder_loc)
        log.info(u"订单确认页面---点击提交订单")


class JbHomePeripheryPage(BasePage):
    """
    周边商圈
    """
    click_periphery_loc="id=>com.hxdsw.brc:id/home_mid_7"
    click_business_product_loc='xpath=>//*[@id="sub_bm_tag_jbsy_list"]/ul[1]/a/ul/table/tbody/tr/td[2]/li'
    click_service_loc='xpath=>//*[@id="bm_tag_sh"]'

    click_service_product_loc='xpath=>//*[@id="sub_bm_tag_sh_list"]/ul[1]'
    click_food_loc='xpath=>//*[@id="bm_tag_cy"]'
    click_food_product_loc='xpath=>//*[@id="sub_bm_tag_cy_list"]/ul[1]/a/ul/li'
    click_entertainment_loc='xpath=>//*[@id="bm_tag_xx"]'
    click_entertainment_product_loc='xpath=>//*[@id="sub_bm_tag_xx_list"]/ul[1]'
    click_education_loc='xpath=>//*[@id="bm_tag_tel"]'
    click_education_product_loc='xpath=>//*[@id="sub_bm_tag_tel_list"]/ul[1]'

    #周报商圈
    def jbHomePeriphery_click_periphery(self):
        self.click(self.click_periphery_loc)
        log.info(u"首页页面---点击周报商圈")

    #嘉宝商业第一个产品
    def jbHomePeriphery_click_business_product(self):
        self.click(self.click_business_product_loc)
        log.info(u"周边商圈页面---嘉宝商业---点击第一个产品")

    #生活服务
    def jbHomePeriphery_click_service(self):
        self.click(self.click_service_loc)
        log.info(u"周边商圈页面---点击生活服务")

    #生活服务第一个产品
    def jbHomePeriphery_click_service_product(self):
        self.click(self.click_service_product_loc)
        log.info(u"周边商圈页面---生活服务---点击第一个产品")

    #餐饮美食
    def jbHomePeriphery_click_food(self):
        self.click(self.click_food_loc)
        log.info(u"周边商圈页面---点击餐饮美食")

    #餐饮美食第一个产品
    def jbHomePeriphery_click_food_product(self):
        self.click(self.click_food_product_loc)
        log.info(u"周边商圈页面---餐饮美食---点击第一个产品")

    #休闲娱乐
    def jbHomePeriphery_click_entertainment(self):
        self.click(self.click_entertainment_loc)
        log.info(u"周边商圈页面---点击休闲娱乐")

    #休闲娱乐第一个产品
    def jbHomePeriphery_click_entertainment_product(self):
        self.click(self.click_entertainment_product_loc)
        log.info(u"周边商圈页面---休闲娱乐---点击第一个产品")

    #教育培训
    def jbHomePeriphery_click_education(self):
        self.click(self.click_education_loc)
        log.info(u"周边商圈页面---点击教育培训")

    #教育培训第一个产品
    def jbHomePeriphery_click_education_product(self):
        self.click(self.click_education_product_loc)
        log.info(u"周边商圈页面---教育培训---点击第一个产品")


class JbHomeDeliciousPage(BasePage):
    """
    香槟美食汇
    """
    click_Delicious_loc="id=>com.hxdsw.brc:id/home_mid_5"
    click_search1_loc="id=>com.hxdsw.brc:id/tv_search"
    input_content_loc="id=>com.hxdsw.brc:id/et_key_word"
    click_search2_loc="id=>com.hxdsw.brc:id/tv_search"
    click_collection_loc="id=>com.hxdsw.brc:id/tv_action"
    click_collection_shop_loc="xpath=>//*[@resource-id='android:id/list']/android.widget.LinearLayout[1]"
    click_classification1_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[1]"
    click_classification2_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[2]"
    click_classification3_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[3]"
    click_classification4_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[4]"
    click_classification5_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[5]"
    click_classification6_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[6]"
    click_classification7_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[7]"
    click_classification8_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[8]"
    click_classification9_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[9]"
    click_classification10_loc="xpath=>//*[@resource-id='com.hxdsw.brc:id/rv_list']/android.widget.FrameLayout[10]"

    click_score_sort_loc="id=>com.hxdsw.brc:id/rl_score"
    click_latest_online_loc="id=>com.hxdsw.brc:id/rl_new"
    click_all_classification_loc="id=>com.hxdsw.brc:id/tv_category_all"

    #香槟美食汇
    def jbHomeDelicious_click_delicious(self):
        self.click(self.click_Delicious_loc)
        log.info("首页页面---点击香槟美食汇")

    #点击搜索
    def jbHomeDelicious_click_search1(self):
        self.click(self.click_search1_loc)
        log.info("香槟美食汇页面---点击搜索")

    #输入店铺名进行搜索
    def jbHomeDelicious_click_content(self):
        self.click(self.input_content_loc)
        log.info("搜索页面---点击搜索文本框")

    #输入店铺名进行搜索
    def jbHomeDelicious_input_content(self,content):
        self.send_keys(self.input_content_loc,content)
        log.info("搜索页面---输入内容{}".format(content))

    #点击搜索
    def jbHomeDelicious_click_search2(self):
        self.click(self.click_search2_loc)
        log.info("搜索页面---点击搜索")

    #我的搜藏
    def jbHomeDelicious_click_collection(self):
        self.click(self.click_collection_loc)
        log.info("香槟美食汇页面---点击收藏")

    #选择第一个搜藏店铺
    def jbHomeDelicious_click_collection_shop(self):
        self.click(self.click_collection_shop_loc)
        log.info("我的收藏页面---点击第一个收藏店铺")
        time.sleep(5)

    #点击第一个分类(就吃火锅)
    def jbHomeDelicous_click_classification1(self):
        self.click(self.click_classification1_loc)
        log.info("香槟美食汇页面---点击就吃火锅")

    #点击烤系列
    def jbHomeDelicous_click_classification2(self):
        self.click(self.click_classification2_loc)
        log.info("香槟美食汇页面---点击烤系列")

    #点击撸个串
    def jbHomeDelicous_click_classification3(self):
        self.click(self.click_classification3_loc)
        log.info("香槟美食汇页面---点击撸个串")

    #点击热卤小吃
    def jbHomeDelicous_click_classification4(self):
        self.click(self.click_classification4_loc)
        log.info("香槟美食汇页面---点击热卤小吃")

    #点击抗疫专区
    def jbHomeDelicous_click_classification5(self):
        self.click(self.click_classification5_loc)
        log.info("香槟美食汇页面---点击抗疫专区")

    #点击轻奢中餐
    def jbHomeDelicous_click_classification6(self):
        self.click(self.click_classification6_loc)
        log.info("香槟美食汇页面---点击轻奢中餐")

    #点击商务宴请
    def jbHomeDelicous_click_classification7(self):
        self.click(self.click_classification7_loc)
        log.info("香槟美食汇页面---点击商务宴请")

    #点击网红打卡
    def jbHomeDelicous_click_classification8(self):
        self.click(self.click_classification8_loc)
        log.info("香槟美食汇页面---点击网红打卡")

    #点击春季汤锅
    def jbHomeDelicous_click_classification9(self):
        self.click(self.click_classification9_loc)
        log.info("香槟美食汇页面---点击春季汤锅")

    #异域料理
    def jbHomeDelicous_click_classification10(self):
        self.click(self.click_classification10_loc)
        log.info("香槟美食汇页面---点击异域料理")

    #点击评分由高到低排序
    def jbHomeDelicous_click_score_sort(self):
        self.click(self.click_score_sort_loc)
        log.info("分类详情页面---点击评分由高到低")

    #点击最新上线排序
    def jbHomeDelicous_click_latest_online(self):
        self.click(self.click_latest_online_loc)
        log.info("分类详情页面---点击最新上线")

    #点击全部分类
    def jbHomeDelicous_click_all_classification(self):
        self.click(self.click_all_classification_loc)
        log.info("香槟美食汇页面---点击全部分类")


































