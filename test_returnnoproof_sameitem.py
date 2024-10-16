import time

import pytest as pytest

from Pages.PaymentPage import PaymentPage
from Pages.ShippingPage import ShippingPage
from Pages.TransactionPage import TransactionPage
from conftest import *
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage

from Pages.ProductPage import ProductPage

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser_setup")
class Test_return:
    # Locators:
    Orders = (By.CSS_SELECTOR, "button[id='tab-button-ButtonGrid6'] div[class='icon']")
    ordernotext = (By.XPATH,
                   "//input[@class='numpad-control-input primaryFontColor numpad-control-input-placeholder numpad-control-input-readonly']")
    enterbtn = (By.XPATH, "//button[@title='Enter']")
    returnbtn = (By.XPATH, "//button[@id='returnButton']")
    # checkbox = (By.XPATH, "//button[@class='expandButton iconChevronDown icon-14x14 win-interactive']")
    # checkbox = (By.XPATH , "//div[@role='option']//div[@class='win-selectioncheckmark']")
    checkbox = (By.XPATH, "//div[@class='win-itembox']")
    # arrowbtn = (By.XPATH , "//div[@class='h6 iconChevronRight icon-24x24 icon height48 width48 center accentColorImportant']")
    arrowbtn = (By.XPATH, "//div[@data-bind='click: $root.viewModel.setReturnReasonForLine.bind($root.viewModel)']")
    Faultyoptn = (By.XPATH, "//div[(@class= 'h4 margin0') and contains(., 'Faulty')]")
    return2 = (By.XPATH, "(//button[@id='return'])[1]")

    onlinepaymentreturn = (By.XPATH, "//button[@aria-label='Online payment return']")
    Sendbtn = (By.XPATH, "//button[(@class= 'okButton primaryButton') and contains(., 'Send')]")
    okbtn = (By.XPATH, "//button[normalize-space()='OK']")
    returnnoproofbtn = (By.XPATH , "//button[@title='Return - No proof of purchase']")

    def setup_class(self):
        self.driver.get(POS_url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.productpage = ProductPage(self.driver)
        self.transaction_page = TransactionPage(self.driver)
        self.shippingpage = ShippingPage(self.driver)
        self.paymentpage = PaymentPage(self.driver)

    a = "cash"
    b = "card"
    c = "gift_card"
    d = "seasalt_reward_points"

    @pytest.mark.parametrize("payment_method", [a])
    def test_return(self,payment_method):


        # POS
        self.login_page.loginPOS()
        self.transaction_page.add_customer()
        self.productpage.choose_product(3)
        time.sleep(5)
        self.transaction_page.returnnoproofofpurchases_exchangesameitem()
        if payment_method == "card":
            self.paymentpage.card()
        elif payment_method == "cash":
            self.paymentpage.cash()
        elif payment_method == "gift_card":
            self.paymentpage.giftcard()
        elif payment_method == "seasalt_reward_points":
            self.paymentpage.seasaltrewardpoints()
        self.base_page.webelement_Click(self.okbtn)
        self.base_page.webelement_Click(self.okbtn)
        self.base_page.webelement_Click(self.okbtn)
