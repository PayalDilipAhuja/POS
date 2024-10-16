from Pages.TransactionPage import TransactionPage
from conftest import *
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser_setup")
class Test_createorderPOS:
    def setup_class(self):
        self.driver.get(POS_url)

        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.transaction_page = TransactionPage(self.driver)

    def test_createorderPOS(self):
        self.login_page.loginPOS()
        self.login_page.assertion()
