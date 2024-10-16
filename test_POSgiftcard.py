import time

import pytest as pytest
from selenium.webdriver.common.by import By

from conftest import *
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.TransactionPage import TransactionPage
from Pages.ProductPage import ProductPage
from Pages.ShippingPage import ShippingPage
from Pages.PaymentPage import PaymentPage
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser_setup")
class Test_POSSgiftcard:
    okbtn = (By.XPATH, "//button[normalize-space()='OK']")

    def setup_class(self):
        self.driver.get(POS_url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.productpage = ProductPage(self.driver)
        self.transaction_page = TransactionPage(self.driver)
        self.shippingpage = ShippingPage(self.driver)
        self.paymentpage = PaymentPage(self.driver)

    def test_giftcard(self):
        self.login_page.loginPOS()
        self.transaction_page.add_customer()
        self.transaction_page.add_giftcard()
        self.paymentpage.add_payments_cash()
        self.base_page.webelement_Click(self.okbtn)
        self.base_page.webelement_Click(self.okbtn)