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
from Account_Page_Class import AccountPageClass
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
            # Create an object for the User Account page
            self.Page_UserAccount = AccountPageClass(self.driver)

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

    def test_5(self):
        self.Page_Home.click_category("speakers")
        product_price_1 = self.Page_Category.product_price_text(25)
        self.Page_Category.click_product(25)
        self.Page_Product.SendKeys_ProductQuantity(2)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("tablets")
        product_price_2 = self.Page_Category.product_price_text(18)
        self.Page_Category.click_product(18)
        self.Page_Product.SendKeys_ProductQuantity(1)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("mice")
        product_price_3 = self.Page_Category.product_price_text(32)
        self.Page_Category.click_product(32)
        self.Page_Product.SendKeys_ProductQuantity(5)
        self.Page_Product.Get_ProductColorByName_Element("BLUE").click()
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Click_CartIcon()
        sumprices = self.Page_Cart.units_price_text(3)+self.Page_Cart.units_price_text(2)+self.Page_Cart.units_price_text(1)
        self.assertEqual(round(product_price_1*2,2), self.Page_Cart.units_price_text(3))
        self.assertEqual(round(product_price_2*1,2), self.Page_Cart.units_price_text(2))
        self.assertEqual(round(product_price_3*5,2), self.Page_Cart.units_price_text(1))
        self.assertEqual(sumprices, self.Page_Cart.total_price_text())

    def test6(self):
        self.Page_Home.click_category("headphones")
        self.Page_Category.click_product(15)
        self.Page_Product.SendKeys_ProductQuantity(2)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("laptops")
        self.Page_Category.click_product(7)
        self.Page_Product.SendKeys_ProductQuantity(1)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Click_CartIcon()
        self.Page_ToolBar.Wait_CartIconWindowClose()
        self.Page_Cart.edit_product_click(2)
        self.Page_Product.SendKeys_ProductQuantity(4)
        self.Page_Product.Click_ADDTOCART()
        self.Page_Cart.Wait_UntilInCartPage()
        self.Page_ToolBar.Wait_CartIconWindowClose()
        self.Page_Cart.edit_product_click(1)
        self.Page_Product.SendKeys_ProductQuantity(10)
        self.Page_Product.Click_ADDTOCART()
        self.Page_Cart.Wait_UntilInCartPage()
        self.assertEqual(self.Page_Cart.product_quantity_text(2), 4)
        self.assertEqual(self.Page_Cart.product_quantity_text(1), 10)

    def test_7(self):
        self.Page_Home.click_category("tablets")
        self.Page_Category.click_product(18)
        self.driver.back()
        self.assertEqual(self.Page_ToolBar.LocationName(), "TABLETS")
        self.driver.back()
        self.assertEqual(self.Page_ToolBar.LocationName(), "HOME")

    def test_8(self):
        self.Page_Home.click_category("headphones")
        self.Page_Category.click_product(15)
        self.Page_Product.SendKeys_ProductQuantity(2)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Get_AdvLogo_Element().click()
        self.Page_Home.click_category("laptops")
        self.Page_Category.click_product(7)
        self.Page_Product.SendKeys_ProductQuantity(1)
        self.Page_Product.Click_ADDTOCART()
        self.Page_ToolBar.Click_CartIconCheckOut()
        self.Page_OrderPayment_NotLog.click_registration()
        self.Page_CreateAccount.Get_Email_Element().send_keys("dodo423@gmail.com")
        self.Page_CreateAccount.Get_Password_Element().send_keys("B21c34!v")
        self.Page_CreateAccount.Get_ConfirmPassword_Element().send_keys("B21c34!v")
        self.Page_CreateAccount.Get_UserName_Element().send_keys("BOBB6")
        self.Page_CreateAccount.Get_IAgree_Element().click()
        self.Page_CreateAccount.Click_RegisterButton()
        self.Page_OrderPayment_Log.Click_NextButton()
        self.Page_OrderPayment_Log.Get_Username_Element().send_keys("pptr23")
        self.Page_OrderPayment_Log.Get_Password_Element().send_keys("Ww234567890q")
        self.Page_OrderPayment_Log.Get_PayNowSafePay__Element().click()
        self.Page_OrderPayment_Log.Wait_ThankyouPageLoad()
        self.assertIn("THANK YOU", self.Page_OrderPayment_Log.Get_ThankYou_Element().text.upper())
        OrderID = self.Page_OrderPayment_Log.Get_OrderNumber_Element().text
        self.Page_ToolBar.Click_CartIcon()
        self.assertTrue(self.Page_Cart.empty_cart_taitel().is_displayed())
        self.Page_Cart.continue_shopping_click()
        self.Page_ToolBar.Wait_CartIconWindowClose()
        self.Page_ToolBar.Get_UserIconOrders_Element().click()
        self.assertEqual(OrderID,self.Page_UserOrder.Get_FOrderNumber_Element(1).text)
        self.Page_ToolBar.Get_UserIconMyAccount_Element().click()
        self.Page_UserAccount.Click_DeleteAccount()
        self.Page_UserAccount.Click_DeleteButton()





















