from time import sleep

from autotest_price.price_android.price_page.base_page import BasePage
from autotest_price.price_android.price_page.my.toolbox.appointment import Appointment
from autotest_price.price_android.price_page.my.toolbox import Baike
from autotest_price.price_android.price_page.my.toolbox import BeautyChooseCar
from autotest_price.price_android.price_page.my.toolbox import BorrowCash
from autotest_price.price_android.price_page.my.toolbox import Calculator
from autotest_price.price_android.price_page.my.toolbox import CarReplacement
from autotest_price.price_android.price_page.my.toolbox import CarValuation
from autotest_price.price_android.price_page.my.toolbox import ConditionSelection
from autotest_price.price_android.price_page.my.toolbox import DealPrice
from autotest_price.price_android.price_page.my.toolbox import DialIndicator
from autotest_price.price_android.price_page.my.toolbox import FourStepCarSelection
from autotest_price.price_android.price_page.my.toolbox import IllegalInquiry
from autotest_price.price_android.price_page.my.toolbox import LicenseScoring
from autotest_price.price_android.price_page.my.toolbox import LocalCarMarket
from autotest_price.price_android.price_page.my.toolbox import LotteryQuery
from autotest_price.price_android.price_page.my.toolbox import ModelComparison
from autotest_price.price_android.price_page.my.toolbox import NearbyDealers
from autotest_price.price_android.price_page.my.toolbox.new_car import NewCar
from autotest_price.price_android.price_page.my.toolbox.price_cut_ranking import PriceCutRanking
from autotest_price.price_android.price_page.my.toolbox import SalesRanking
from autotest_price.price_android.price_page.my.toolbox import SecondHandCar
from autotest_price.price_android.price_page.my.toolbox import SellCar
from autotest_price.price_android.price_page.my.toolbox import TakePhotos
from autotest_price.price_android.price_page.my.toolbox import TravelReminder


class ToolBoxMore(BasePage):
    sleep(3)

    # ???????????????
    def goto_cal(self):
        self.find(by="xpath", locator='//*[@text="???????????????"]').click()
        return Calculator(self._driver)

    # ????????????
    def goto_model_comparison(self):
        self.find(by="xpath", locator="//*[@text='????????????']").click()
        return ModelComparison(self._driver)

    # ????????????
    def goto_four_step_car_selection(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return FourStepCarSelection(self._driver)

    # ????????????
    def goto_sales_ranking(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return SalesRanking(self._driver)

    # ???????????????
    def goto_nearby_dealers(self):
        self.find(by="xpath", locator='//*[@text="???????????????"]').click()
        return NearbyDealers(self._driver)

    # ????????????
    def goto_deal_price(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return DealPrice(self._driver)

    # ????????????
    def goto_second_car(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return SecondHandCar(self._driver)

    # ????????????
    def goto_new_car(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return NewCar(self._driver)

    # ????????????
    def goto_condition_selection(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return ConditionSelection(self._driver)

    # ????????????
    def goto_baike(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return Baike(self._driver)

    # ????????????
    def goto_price_cut_ranking(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return PriceCutRanking(self._driver)

    # ????????????
    def goto_local_car_market(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return LocalCarMarket(self._driver)

    # ????????????
    def goto_beauty_choose_car(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return BeautyChooseCar(self._driver)

    # ????????????
    def goto_take_photos(self):
        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        return TakePhotos(self._driver)

    # ?????????
    def goto_borrow_cash(self):
        self.find(by="xpath", locator='//*[@text="?????????"]').click()
        return BorrowCash(self._driver)

    # ????????????
    def goto_illegal_inquiry(self):
        sleep(3)
        # ua_scroll = 'new UiScrollable(new UiSelector().className("android.support.v7.widget.RecyclerView"))' \
        #             '.scrollIntoView(new UiSelector().text("????????????"))'
        # self._driver.find_element_by_android_uiautomator(ua_scroll).click()

        self.find(by="xpath", locator='//*[@text="????????????"]').click()
        # self.base_scroll("text", "????????????").click()

        # self.base_srcoll_up_down(by="xpath", locator='//*[@text="????????????"]', rx=0.5, ry1=0.8, ry2=0.3, num=100).click()
        return IllegalInquiry(self._driver)

    # ????????????
    def goto_lottery_query(self):
        self.base_scroll("text", "????????????").click()
        return LotteryQuery(self._driver)

    # ???????????????
    def goto_car_replacement(self):
        self.base_scroll("text", "???????????????").click()
        return CarReplacement(self._driver)

    # ????????????
    def goto_sell_car(self):
        self.base_scroll("text", "????????????").click()
        return SellCar(self._driver)

    # ????????????
    def goto_license_scoring(self):
        self.base_scroll("text", "????????????").click()
        return LicenseScoring(self._driver)

    # ????????????
    def goto_travel_reminder(self):
        self.base_scroll("text", "????????????").click()
        return TravelReminder(self._driver)

    # ???????????????
    def goto_dial_indicator(self):
        self.base_scroll("text", "???????????????").click()
        return DialIndicator(self._driver)

    # ????????????
    def goto_appointment(self):
        self.base_scroll("text", "????????????").click()
        return Appointment(self._driver)

    # ????????????
    def goto_car_valuation(self):
        self.base_scroll("text", "????????????").click()
        return CarValuation(self._driver)
