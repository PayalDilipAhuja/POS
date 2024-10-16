import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class TransactionPagePOS(BasePage):
    # Locators:
    Orders = (By.CSS_SELECTOR, "button[id='tab-button-ButtonGrid6'] div[class='icon']")
    Create_cust_order = (By.XPATH, "//button[@title='Create customer order']")
    Add_Product = (By.XPATH, "//button[@id='addProductButton']")

    Navigation_Pane = (By.CSS_SELECTOR,
                       "button[class='headerSplitViewToggleButton iconGlobalNavButton win-splitviewpanetoggle "
                       "win-disposable']")
    Add_customerbtn = (By.ID, "addCustomerButton")
    Search_bar = (By.CSS_SELECTOR, "input[placeholder='Search']")
    # Customer = (By.XPATH , "//*[@id="element__137"]/div/div[1]")
    Ship_all_products = (By.CSS_SELECTOR, "button[title='Ship all products']")
    Store_collection_btn = (By.XPATH, "//div[contains(text(),'Store collection-Col')]")
    Store_name = (By.XPATH, "//li[normalize-space()='St. Ives']")
    OK_button = (By.XPATH, "//button[normalize-space()='OK']")
    Payments_tab = (By.XPATH, "//button[normalize-space()='Payments']")
    Add_Payment_btn = (By.XPATH, "//button[@id='addPaymentButton']")
    Card_Amex = (By.CSS_SELECTOR, "div[aria-label='Card (Amex Ecom)'] div[class='col grow pad12 padBottom0']")
    Enter_button = (By.CSS_SELECTOR,
                    "button[class='flexGrow100 accentBackground enter'] div[class='h1 marginBottom0 iconReturnKey "
                    "button-content-return'")
    Send_Button = (By.XPATH, " //button[normalize-space()='Send']")
    Close_button = (By.XPATH, "//button[normalize-space()='Close']")

    Add_to_sale = (By.XPATH, "//button[@id='CustomerSearch_addSelectedCustomerToCartCommand']//span["
                             "@class='win-commandimage']")
    CARD = (By.CSS_SELECTOR, "button[title='CARD']")
    Clicktocollectorder = (By.CSS_SELECTOR , "button[title='Click and collect order lines']")
    Filter_icon2 = (By.XPATH , "//button[@id='CartView_FilterCommand']")
    Add_to_filter = (By.XPATH, "//div[contains(text(),'Add Filter')]")
    Dropdown = (By.XPATH , '//*[@id="filterDropdown"]/span[1]')
    OK_button2= (By.XPATH , "//button[normalize-space()='OK']")
    Apply_btn = (By.XPATH, '//*[@id="Button1"]')
    Text_Area = (By.XPATH,"//textarea[@id='textInputDialogContent']")

    DOM = (By.CSS_SELECTOR , "button[title='DOM'] div[class='h4 margin0']")
    Filter_iconDOM = (By.XPATH , "//button[@id='filterFulfillmentLine']//span[@class='win-commandimage']")
    Add_Filter_DOM = (By.XPATH , "//button[@id='addRefiner']//div[@class='row centerY']")
    Order_no_DOM = (By.XPATH , "//div[contains(@class, 'h4 ellipsis') and contains(., 'Order number')]")
    Orderno_text = (By.XPATH , "//input[@id='textInputDialogContent']")
    OK_btn_dom = (By.XPATH , "//button[normalize-space()='OK']")
    Apply_btn_DOM = (By.XPATH , "//button[normalize-space()='Apply']")
    Select_btn = (By.XPATH , "//button[@id='fulfillmentLineView_showMultiSelect']")
    #time.sleep(5)
    container = (By.XPATH, "//div[@class='win-container']")
    checkbox = (By.XPATH ,"//div[@class='win-itembox']")
    #checkbox = (By.XPATH , '//*[@id="fulfillmentLineList"]/div[1]/div[2]/object')
    Line = (By.XPATH, '//*[@id="outerViewsHost"]/div[1]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div')
    checkbox2 = (By.XPATH , "//div[(@class= 'win-container') and contains(., 'Order Number')]")
    Pack_icon = (By.XPATH , "//button[@id='packAppBar']//span[@class='win-commandimage']")
    Ship_icon = (By.XPATH , "//button[@id='shipLines']//span[@class='win-commandimage']")
    Scanbarcodedetails = (By.XPATH, "//input[@id='barcodeId']")
    OK_btn3 = (By.ID , "Button1")
    Changestatus = (By.XPATH , "//button[@id='CartView_Change statusCommand']")
    Collected_by_customer = (By.CSS_SELECTOR , "div[aria-label='Collected by customer'] div[class='col grow pad12 padBottom0']")
    Partial_pickup = (By.CSS_SELECTOR , "div[aria-label='Yes - Partial pick'] div[class='col grow pad12 padBottom0']")
    Txnicon = (By.ID , 'CART_ITEM_ID')

    returntab = (By.XPATH, "//div[(@class= 'text semilight primaryFontColor') and contains(., 'RETURNS')]")
    returnproofofpurchase = (By.XPATH, "//button[@title ='Return - Proof of purchase']")
    ordernotext = (By.XPATH,
                   "//input[@class='numpad-control-input primaryFontColor numpad-control-input-placeholder numpad-control-input-readonly']")

    Username = (By.XPATH, "//div[(@class='h4 ellipsis textLeft')  and contains(., 'Payal Uttamani')]")

    def __init__(self, driver):
        super().__init__(driver)



    def domfilterorderid_packship(self):
        # detailpage = D365OrderDetailsPage()
        # d1 = detailpage.D365barcodedetails2()
        self.webelement_Click(self.DOM)
        time.sleep(5)
        self.webelement_Click(self.Filter_iconDOM)
        time.sleep(5)
        self.webelement_Click(self.Add_Filter_DOM)
        time.sleep(5)
        self.webelement_Click(self.Order_no_DOM)
        self.webelementEnter(self.Orderno_text, "M91003269")
        self.webelement_Click(self.OK_btn_dom)
        time.sleep(5)
        self.webelement_Click(self.Apply_btn_DOM)
        time.sleep(2)
        self.webelement_Click(self.Select_btn)
        # time.sleep(5)
        # self.webelement_Click(self.Line)
        time.sleep(2)
        self.is_click(self.checkbox2)
        # self.click_element_inside_container(self.container , self.checkbox)
        self.webelementPressUpperKey(self.Pack_icon)
        time.sleep(5)
        if self.is_element_present(self.Partial_pickup):
            self.webelement_Click(self.Partial_pickup)
        time.sleep(5)
        # self.webelementEnter(self.Scanbarcodedetails,d1)
        self.webelement_Click(self.OK_btn3)
        time.sleep(5)
        self.is_click(self.checkbox2)

        self.webelement_Click(self.Ship_icon)
        time.sleep(5)
        self.webelement_Click(self.Txnicon)