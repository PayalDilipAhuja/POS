import time

import pytest as pytest

from conftest import *
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.TransactionPage import TransactionPage
from Pages.ProductPage import ProductPage
from Pages.ShippingPage import ShippingPage
from Pages.PaymentPage import PaymentPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser_setup")
class Test_POSSOExisting:
    # Locators:
    Orders = (By.CSS_SELECTOR, "button[id='tab-button-ButtonGrid6'] div[class='icon']")

    def setup_class(self):
        self.driver.get(POS_url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.productpage = ProductPage(self.driver)
        self.transcation_page = TransactionPage(self.driver)
        self.shippingpage = ShippingPage(self.driver)
        self.paymentpage = PaymentPage(self.driver)

    def test_existing_cust(self):
        self.login_page.loginPOS()
        self.base_page.webelement_Click(self.Orders)
        self.productpage.add_product()
        self.transcation_page.add_customer()
        self.shippingpage.select_store()
        time.sleep(10)
        self.paymentpage.add_payments_cardamex()
