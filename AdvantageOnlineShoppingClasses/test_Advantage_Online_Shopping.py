from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Home_Page_Class import Home_Page_Advantage
from Category_Page_Class import Category_Page_Advantage
from Cart_Page_Class import Cart_Page_Advantage
from CreateAccount_Page_Class import CreateAccountClass
from OrderPayment_Page_NotLog_Class import OrderPayment_page_NotLog_Advantage
from OrderPayment_Log_Page_Class import OrderPaymentLogClass
from Product_Page_Class import ProductClass
from ToolBar_Page_Class import ToolBarClass
from UserOrder_Page_Class import UserOrdersClass
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class TestAdvantageOnlineShopping(TestCase):
    def setUp(self):
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            service_chrome = Service(r"C:\selenium1\chromedriver.exe")

            # Open browser (create a driver object)
            self.driver = webdriver.Chrome(service=service_chrome, options=chrome_options)

            # Go to the required URL
            self.driver.get("https://advantageonlineshopping.com/#/")

            self.driver.maximize_window()
            self.driver.implicitly_wait(20)

            # Create an object for the toolbar
            self.Page_ToolBar = ToolBarClass(self.driver)
            # Create an object for the Home page
            self.Page_Home = Home_Page_Advantage(self.driver)
            # Create an object for the Category page
            self.Page_Category = Category_Page_Advantage(self.driver)
            # Create an object for the Cart page
            self.Page_Cart = Cart_Page_Advantage(self.driver)
            # Create an object for the Create Account page
            self.Page_CreateAccount = CreateAccountClass(self.driver)
            # Create an object for the Order Payment page when the user is not login
            self.Page_OrderPayment_NotLog = OrderPayment_page_NotLog_Advantage(self.driver)
            # Create an object for the Order Payment When is login
            self.Page_OrderPayment_Log = OrderPaymentLogClass(self.driver)
            # Create an object for the Product page
            self.Page_Product = ProductClass(self.driver)
            # Create an object for the User Order page
            self.Page_UserOrder = UserOrdersClass(self.driver)

    def test_1(self):
        self.Page_Home.click_category("speakers")
        self.Page_Category.click_product(20)
        self.Page_Product.SendKeys_ProductQuantity(3)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("tablets")
        self.Page_Category.click_product(17)
        self.Page_Product.SendKeys_ProductQuantity(4)
        self.Page_Product.Click_ADDTOCART()
        self.assertEqual(self.Page_ToolBar.ItemsAmountInCartDigits(), 7)
    def test_2(self):
        self.Page_Home.click_category("speakers")
        self.Page_Category.click_product(25)
        self.Page_Product.SendKeys_ProductQuantity(2)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("tablets")
        self.Page_Category.click_product(18)
        self.Page_Product.SendKeys_ProductQuantity(1)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("mice")
        self.Page_Category.click_product(32)
        self.Page_Product.SendKeys_ProductQuantity(5)
        self.Page_Product.Get_ProductColorByName_Element("BLUE").click()
        self.Page_Product.Click_ADDTOCART()
        self.assertEqual(self.Page_ToolBar.CartIconQuntityDigits(1), 5)
        self.assertEqual(self.Page_ToolBar.CartIconQuntityDigits(2), 1)
        self.assertEqual(self.Page_ToolBar.CartIconQuntityDigits(3), 2)
        self.assertIn(self.Page_ToolBar.CartIconItemNameSTR(1), "KENSINGTON ORBIT 72337 TRACKBALL WITH SCROLL RING")
        self.assertIn(self.Page_ToolBar.CartIconItemNameSTR(2), "HP Pro Tablet 608 G1".upper())
        self.assertIn(self.Page_ToolBar.CartIconItemNameSTR(3), "Bose SoundLink Wireless Speaker".upper())
        self.assertEqual(self.Page_ToolBar.Get_CartIconColor_Element(1).text, "BLUE")
        self.assertEqual(self.Page_ToolBar.Get_CartIconColor_Element(2).text, "BLACK")
        self.assertEqual(self.Page_ToolBar.Get_CartIconColor_Element(3).text, "TURQUOISE")
        self.assertEqual(self.Page_ToolBar.CartIconItemPriceDigits(1), 199.95)
        self.assertEqual(self.Page_ToolBar.CartIconItemPriceDigits(2), 479.00)
        self.assertEqual(self.Page_ToolBar.CartIconItemPriceDigits(3)/2, 129.00)

    def test_3(self):
        self.Page_Home.click_category("headphones")
        self.Page_Category.click_product(15)
        self.Page_Product.SendKeys_ProductQuantity(2)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("laptops")
        self.Page_Category.click_product(7)
        self.Page_Product.SendKeys_ProductQuantity(1)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Click_CartIconRemoveItem(2)
        with self.assertRaises(NoSuchElementException):
            self.Page_ToolBar.Get_CartIconItemName_Element(2)

    def test_4(self):
        self.Page_Home.click_category("speakers")
        self.Page_Category.click_product(20)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Click_CartIcon()
        self.assertEqual(self.Page_ToolBar.LocationName(), "SHOPPING CART")


        






