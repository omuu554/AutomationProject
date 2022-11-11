from selenium import webdriver
from selenium.webdriver.common.by import By
import re

class UserOrdersClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Get_FOrderedItem_Element(self, index:int):
        "returns a list of elements for item index which are the first item of everyOrder(must only give index of first item of an order)"
        return self.driver.find_elements(By.XPATH, f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index+1}]/td")

    def Get_FOrderNumber_Element(self, index:int):
        "returns a Element of OrderNumber(must only give index of first item of an order)"
        return self.Get_FOrderedItem_Element(index)[1].find_element(By.XPATH,"//td/label")

    def Get_FOrderTotalCost_Element(self, index:int):
        "returns the Element of the Total cost of Order(must only give index of first item of an order)"
        return self.Get_FOrderedItem_Element(index)[-1].find_element(By.CSS_SELECTOR, "td>label")

    def FTotalPriceDigits(self, index:int):
        "Returns Total price of items without shipping in Digits"
        return float(re.sub(r'[^0-9.]', '', self.Get_FOrderTotalCost_Element(index).text))

    def Get_FOrderItemName_Element(self, index:int):
        "returns the Element Item Name(must only give index of first item of an order)"
        return self.driver.find_element(By.XPATH,  f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index + 1}]/td[4]/span")

    def Get_FOrderItemColor_Element(self, index:int):
        "returns the Element Item Color(must only give index of first item of an order)"
        return self.driver.find_element(By.XPATH,  f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index + 1}]/td[5]/div")

    def FOrderItemColorName(self, index:int):
        "returns the Item Color in all upper cases (must only give index of first item of an order)"
        return self.Get_FOrderItemColor_Element(index).get_attribute('title').upper()

    def Get_FOrderItemQuantity_Element(self, index: int):
        "returns the Element Item quantity(must only give index of first item of an order)"
        return self.driver.find_element(By.XPATH,  f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index + 1}]/td[6]/label")

    def Get_FOrderRemove_Element(self, index:int):
        "returns the Element for remove order button(must only give index of first item of an order)"
        return self.Get_FOrderedItem_Element(index)[-1].find_element(By.CSS_SELECTOR, "td>span>a")

    def Get_OrderItemName_Element(self, index: int):
        "returns the Element Item name(must only give index of item that is not the first in the order)"
        return self.driver.find_element(By.XPATH, f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index + 1}]/td[1]/span")

    def Get_OrderItemQuantity_Element(self, index: int):
        "returns the Element Item quantity(must only give index of item that is not the first in the order)"
        return self.driver.find_element(By.XPATH,  f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index + 1}]/td[3]/label")

    def Get_OrderItemColor_Element(self, index: int):
        "returns the Element Item color(must only give index of item that is not the first in the order)"
        return self.driver.find_element(By.XPATH, f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index + 1}]/td[2]/div")

    def OrderItemColorName(self, index: int):
        "returns the Item color in all upper cases(must only give index of item that is not the first in the order)"
        return self.Get_OrderItemColor_Element(index).get_attribute('title').upper()




