import time

import pytest as pytest
from selenium.webdriver import Keys

from Pages.D365HomePage import D365HomePage
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
class Test_tc15:
    #Locators
    Submit = (By.XPATH, '//*[@id="form-validate"]/div/div/div[1]/button/span')
    D365Name = (By.NAME, "SalesTable_SalesName")
    D365Email = (By.NAME, "ContactInfo_Email")
    D365Phone = (By.NAME, "ContactInfo_Phone")
    Campain = (By.NAME, "Campaign_smmCampaignId")
    D365_Filter_Table = (By.XPATH, "/html/body/div[22]/ul/li[1]")
    Orders = (By.CSS_SELECTOR, "button[id='tab-button-ButtonGrid6'] div[class='icon']")
    Credential = (By.XPATH , '//*[@id="tilesHolder"]/div[1]/div/div[1]/div/div[2]')
    D365_Filter = (By.XPATH, "//input[(@name= 'QuickFilterControl_Input')]")
    D365_Sales_order2 = (By.XPATH, '//*[@id="salestablelistpage_3_SalesOrder_button"]/span')
    Recap_btn = (By.ID, "salestablelistpage_3_MCRRecap_label")
    Ordernofinal = (By.XPATH, '//*[@id="MCRSalesOrderRecap_4_SalesOrderSummaryHeader_SalesTable_SalesId"]')

    #D365pass = (By.NAME, "passwd")
    def setup_class(self):
        self.driver.get(POS_url)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.productpage = ProductPage(self.driver)
        self.transcation_page = TransactionPage(self.driver)
        self.shippingpage = ShippingPage(self.driver)
        self.paymentpage = PaymentPage(self.driver)
        self.d365homepage = D365HomePage(self.driver)
        #self.d365orderpage = D365OrderDetailsPage(self.driver)
        self.base_page = BasePage(self.driver)

    def test_existing_cust(self):
        self.login_page.loginPOS()
        self.base_page.webelement_Click(self.Orders)
        self.productpage.add_product()
        self.transcation_page.add_customer()
        self.shippingpage.select_store()
        time.sleep(10)
        self.paymentpage.add_payments()
        #self.transcation_page.change_status()
        ordernumber = self.transcation_page.change_status2()
        print(ordernumber)
        #D365
        self.driver.get(D365_url)
        time.sleep(2)
        #self.login_page.loginD365("Payal.Uttamani@seasaltcornwall.co.uk", "gAce4u5uxlR$")
        self.login_page.loginD365()
        #self.base_page.webelementEnter(self.D365pass, "gAce4u5uxlR$")
        self.d365homepage.D365HomePagefn()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.D365_Filter))
        element.send_keys(ordernumber)
        element.send_keys(Keys.ENTER)
        self.base_page.webelement_Click(self.D365_Filter_Table)
        time.sleep(2)
        self.base_page.webelement_Click(self.D365_Sales_order2)
        time.sleep(2)
        self.base_page.webelement_Click(self.Recap_btn)
        time.sleep(5)
        self.base_page.webelement_Click(self.Ordernofinal)
        time.sleep(2)