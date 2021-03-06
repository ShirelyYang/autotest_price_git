from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage


class LocalCarMarket(BasePage):
    # 本地优惠
    def local_offer(self):
        # 先选择而热门城市，例如:北京
        self.find(by="id", locator="tv_tv_right1").click()
        sleep(3)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.8, num=100).click()
        # 点击本地优惠tab
        self.find(by="xpath", locator='//*[@text="本地优惠"]').click()
        # 选择品牌
        # self.found(by="xpath", locator='//*[@text="选择品牌"]').click()
        # self.base_scroll("text", "哈弗").click()
        brands = self.finds(by="id", locator="android:id/icon")
        print(brands)
        brands[1].click()
        # 马上抢
        discount = self.find(by="id", locator='icmcTvInfo')
        discount_content = discount.text
        discount.click()
        activity = self.find(by="xpath", locator='//*[@resource-id="topBodu"]/android.view.View[2]')
        return discount_content, activity.text

    # 切换城市
    def change_city(self):
        self.find(by="id", locator="tv_tv_right1").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.6, num=100)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="贵州"]', rx=0.2, ry1=0.6, ry2=0.4, num=100).click()
        self.find(by="xpath", locator='//*[@text="黔南"]').click()
        self.find(by="id", locator="icmpTvBtn").click()
        # self.found(by="id", locator="ask_name").send_keys("测试")
        # self.found(by="id", locator="ask_tel").send_keys("13888888888")
        # self.found(by="id", locator="askprice_txt_bottom").click()
        # fapr_tv_title = self.found(by="id", locator="fapr_tv_title")
        sleep(3)
        info = self.find(by="id", locator="askprice_txt_bottom").text
        self.find(by="id", locator="ask_close").click()
        return info

    # 金牌顾问
    def gold_advisor(self):
        # 先选择而热门城市，例如:北京
        self.find(by="id", locator="tv_tv_right1").click()
        sleep(2)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.8, num=100).click()
        # 点击本金牌顾问tab
        self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/title_container"]//*[@class="android.widget.ImageView"]').click()

    # 金牌顾问-详情
    def gold_advisor_details(self):
        self.gold_advisor()
        alsTvName = self.find(by="id", locator="alsTvName")
        name = alsTvName.text
        alsTvName.click()
        sale_name = self.find(by="id", locator="sale_name").text
        return name, sale_name

    # 金牌顾问-打电话
    def gold_advisor_tel(self):
        pass

    # 金牌顾问-更多
    def gold_advisor_more(self):
        # self.gold_advisor()
        alsTvName = self.find(by="id", locator="alsTvName")
        name = alsTvName.text
        self.find(by="id", locator="isabTvMore").click()
        name_more = self.find(by="id", locator="alsTvName").text
        return name, name_more

    # 金牌顾问-附近门店-详情
    def nearby_stores_details(self):
        self.gold_advisor()
        # self.base_scroll("resourceId", "isanTvTitle")
        self.base_srcoll_up_down(by="id", locator="isanTvTitle", rx=0.5, ry1=0.8, ry2=0.4, num=100)
        store = self.find(by="id", locator="isabTvName")
        store_name = store.text
        store.click()
        dealer_name = self.find(by="id", locator="dealer_name").text
        return store_name, dealer_name

    # 金牌顾问-附近门店-销售详情
    def nearby_advisor_details(self):
        name = self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/isanCl"]//*[@class="android.widget.LinearLayout"]//*[@class="android.widget.TextView"]')
        name_text = name.text
        name.click()
        sale_name = self.find(by="id", locator="sale_name").text
        return name_text, sale_name

    # 金牌顾问-附近门店-导航
    def nearby_stores_map(self):
        addr = self.find(by="id", locator="isanTvAddr").text
        self.find(by="id", locator="isanTvDistance").click()
        sleep(3)
        addr_map = self.find(by="id", locator="r1c2").text
        return addr, addr_map

    # 金牌顾问-附近门店-更多
    def nearby_stores_more(self):
        addr = self.find(by="id", locator="isanTvAddr").text
        store_name = self.find(by="id", locator="isabTvName").text
        self.find(by="id", locator="isanTvMore").click()
        addr_more = self.find(by="xpath", locator=f'//*[@text="{store_name}"]/../*[@resource-id="com.yiche.price:id/dealer_address"]').text
        return addr, addr_more

    # 金牌顾问-选择品牌
    def gold_advisor_brand(self):
        self.find(by="xpath", locator='//*[@text="选择品牌"]').click()
        self.base_scroll("text", "奔驰").click()
        self.find(by="id", locator="alsIvImg").click()
        dealer_name = self.find(by="id", locator="dealer_name").text
        return dealer_name

    # 小视频
    def small_video(self):
        self.find(by="xpath", locator='//*[@text="小视频"]').click()
        user_name_tv = self.find(by="id", locator="user_name_tv")
        user_name = user_name_tv.text
        user_name_tv.click()
        sale_name = self.find(by="id", locator="fsviTvSaleName").text
        return user_name, sale_name

    # 4S保养-详情
    def maintenance(self):

        self.find(by="id", locator="tv_tv_right1").click()
        sleep(3)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.8, num=100).click()

        self.find(by="xpath", locator='//*[@text="4S店保养"]').click()
        # 选择品牌
        self.find(by="xpath", locator='//*[@text="选择品牌"]').click()
        self.base_scroll("text", "哈弗").click()
        mtTvPrice = self.find(by="id", locator="mtTvPrice")
        price = mtTvPrice.text
        mtTvPrice.click()
        sleep(3)
        title_center_txt = self.find(by="id", locator="title_center_txt").text
        return title_center_txt

    # 4S保养-马上抢
    def grab(self):
        # self.found(by="id", locator="tv_tv_right1").click()
        # sleep(2)
        # self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.8, num=100).click()
        # self.found(by="xpath", locator='//*[@text="4S店保养"]').click()

        self.find(by="id", locator="mtTvBtn").click()
        sleep(3)
        title = self.find(by="id", locator="title_center_txt").text
        return title

    # 4S预约
    def booking(self):
        self.find(by="id", locator="tv_tv_right1").click()
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="北京"]', rx=0.2, ry1=0.3, ry2=0.6, num=100)
        self.base_srcoll_up_down(by="xpath", locator='//*[@text="贵州"]', rx=0.2, ry1=0.6, ry2=0.4, num=100).click()
        self.find(by="xpath", locator='//*[@text="黔南"]').click()

        # self.found(by="xpath", locator='//*[@text="4S店保养"]').click()

        # 点击预约按钮
        self.find(by="id", locator="mtOrderTvBtn").click()
        sleep(3)
        title = self.find(by="id", locator="title_center_txt").text
        return title

    # 本地成交价
    def del_price(self):

        self.find(by="xpath", locator='//*[@text="4S店保养"]').click()

        self.find(by="xpath", locator='//*[@text="本地成交价"]').click()
        # 选择品牌
        self.find(by="xpath", locator='//*[@text="选择品牌"]').click()
        self.base_scroll("text", "哈弗").click()
        # 查成交价
        car = self.find(by="id", locator="localPTvName").text
        self.find(by="id", locator="localPTvBtn").click()
        price = self.find(by="id", locator="car_bg_price").text
        if "*" in price:
            self.find(by="id", locator="fagTvPhone").send_keys("13888888888")
            self.find(by="id", locator="fagTvSubmit").click()
            sleep(3)
        # car_bg_price = self.found(by="id", locator="car_bg_price").text
        car_name = self.find(by="id", locator="car_name").text
        self.find(by="id", locator="owner_close").click()
        return car, car_name

    # 糖豆-本地热榜
    def hot_list_car(self):
        # self.base_scroll("resourceId", "fcmIv1").click()
        self.find(by="id", locator="fcmIv1").click()
        # 轿车
        car = self.find(by="id", locator="localcarmarket_salerank_serialname_txt")
        car_name = car.text
        car.click()
        car_brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        self.back()
        return car_name, car_brandtype_serial_name

    # SUV
    def hot_list_suv(self):
        self.find(by="xpath", locator='//*[@text="SUV"]').click()
        suv = self.find(by="id", locator="localcarmarket_salerank_serialname_txt")
        suv_name = suv.text
        suv.click()
        suv_brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        self.back()
        return suv_name, suv_brandtype_serial_name

    # MPV
    def hot_list_mpv(self):
        self.find(by="xpath", locator='//*[@text="MPV"]').click()
        mpv = self.find(by="id", locator="localcarmarket_salerank_serialname_txt")
        mpv_name = mpv.text
        mpv.click()
        mpv_brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        self.back()
        return mpv_name, mpv_brandtype_serial_name

    # 新能源
    def hot_list_new_energy(self):
        self.find(by="xpath", locator='//*[@text="新能源"]').click()
        new_energy = self.find(by="id", locator="localcarmarket_salerank_serialname_txt")
        new_energy_name = new_energy.text
        new_energy.click()
        new_energy_brandtype_serial_name = self.find(by="id", locator="brandtype_serial_name").text
        self.back()
        return new_energy_name, new_energy_brandtype_serial_name

    # 本地热榜-询底价
    def hot_list_ask_price(self):
        self.find(by="xpath", locator='//*[@text="SUV"]').click()
        self.find(by="id", locator="localcarmarket_salerank_askprice_txt").click()
        sleep(3)
        info = self.find(by="id", locator="askprice_txt_bottom").text
        self.find(by="id", locator="ask_close").click()
        return info

    # 糖豆-附近经销商
    def nearby_dealers(self):
        self.find(by="id", locator="fcmIv2").click()
        self.find(by="id", locator="tv_brand").click()
        self.base_scroll("text", "大众").click()
        dealer = self.find(by="id", locator="dealer_name")
        dealer_name = dealer.text
        dealer.click()
        dealer_detail = self.find(by="id", locator="dealer_name").text
        self.back()
        return dealer_name, dealer_detail

    # 糖豆-二手车
    def second_hand_car(self):
        self.find(by="id", locator="fcmIv3").click()
        auglTvName = self.find(by="id", locator="auglTvName")
        car_name = auglTvName.text
        auglTvName.click()
        fulTvName = self.find(by="id", locator="fulTvName").text
        self.back()
        return car_name, fulTvName

    # 糖豆-本地降价
    def price_cut(self):
        self.find(by="id", locator="fcmIv4").click()
        car = self.find(by="id", locator="localcarmarket_promotion_serialname_txt")
        car_name = car.text
        car.click()
        brand = self.find(by="id", locator="brandtype_serial_name").text
        self.back()
        return car_name, brand




