from autotest_price.price_android.price_page.base_page import BasePage


class TravelReminder(BasePage):
    # εΊθ‘ζι
    def travel_reminder(self):
        weather = self.find(by="id", locator="fwatTvWeaDesc").text
        return weather