from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

class ProductClass:

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def Get_ProductName_Element(self):
        "Returns the Element of the product name!"
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1")

    def Get_ProudctPrice_Element(self):
        "Returns the Element of the product price"
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h2")

    def ProductPriceDigits(self):
        "Returns the Element of the product name"
        return re.sub(r'[^0-9.]', '', self.Get_ProudctPrice_Element().text)

    def Get_ProudctDescription_Element(self):
        "Returns the Element of the product description"
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>p")

    def Get_ProductColorByName_Element(self,Color:str):
        "Returns the Element of a spcifice product Color in the page by name"
        return self.driver.find_element(By.CSS_SELECTOR, f"div[ng-show='firstImageToShow']>span.{Color.upper()}")

    def Get_ProductColorByIndex_Element(self,index:int):
        "Returns the Element of a spcifice product Color in the page By Index"
        return self.driver.find_element(By.CSS_SELECTOR, f"//div[@id='productProperties']/div[1]/div[1]/span[{index}]")

    def Get_SelectedColor_Element(self):
        "Returns the Element of Selected Color"
        return self.driver.find_element(By.CLASS_NAME, "colorSelected")

    def SelectedColorName(self):
        return self.Get_SelectedColor_Element().get_attribute("title")

    def Get_ProductQuantityMinus_Element(self):
        "Returns the Element Minus button to decrease quantity"
        return self.driver.find_element(By.CLASS_NAME, "minus")

    def Get_ProductQuantityPlus_Element(self):
        "Returns the Element Minus button to increase quantity"
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def Get_ProductQuantity_Element(self):
        "Returns the Element quantity bar"
        return self.driver.find_element(By.NAME, "quantity")

    def SendKeys_ProductQuantity(self, Quantity:int):
        "Change Item Quantity"
        self.ClearProductQuantity()
        self.Get_ProductQuantity_Element().send_keys(f"{Quantity}")

    def ClearProductQuantity(self):
        "Clears quantity of product"
        for i in range(10):
            self.Get_ProductQuantity_Element().send_keys(Keys.BACKSPACE)


    def Get_ADDTOCART_Element(self):
        "Returns the Element of the ADDTOCART button "
        return self.driver.find_element(By.NAME,"save_to_cart")

    def Click_ADDTOCART(self):
        "Clicks on ADDTOCARTBUTTON"
        self.Get_ADDTOCART_Element().click()


    def IsProductNotSoldOut(self):
        "Returns true if Product is not sold out "
        try:
            self.Get_ProductQuantity_Element().click()
            return True
        except:
            return False

