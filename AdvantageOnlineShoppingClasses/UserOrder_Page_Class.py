from selenium import webdriver
from selenium.webdriver.common.by import By

class UserOrdersClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Get_OrderedItem_Element(self, index:int):
        return self.driver.find_elements(By.XPATH, f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index+1}]/td")

    def Get_FOrderNumber_Element(self, index:int):
        return self.Get_OrderedItem_Element(index)[1].find_element(By.XPATH,"//td/label")

    def Get_FOrderTotalCost_Element(self, index:int):
        return self.Get_OrderedItem_Element(index)[-1].find_element(By.XPATH, "//td/label")


