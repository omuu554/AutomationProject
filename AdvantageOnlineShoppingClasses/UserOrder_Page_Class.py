from selenium import webdriver
from selenium.webdriver.common.by import By

class UserOrdersClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Get_OrderedItem_Element(self, index:int):
        return self.driver.find_element(By.XPATH, f"//div[@id='myAccountContainer']/div/table/tbody/tr[{index+1}]")

    def Get_OrderNumber_Element(self):
        pass
