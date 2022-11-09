from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
class Category_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def product(self, product_id: int):
        """get product element by the id of the product """
        return self.driver.find_element(By.ID, f"{product_id}")
    def product_name(self, product_id: int):
        """get product name element by the id of the product """
        return self.driver.find_element(By.XPATH, f"//img[@id='{product_id}']/../p[1]/a")

    def product_price(self, product_id: int):
        """get product price element by the id of the product """
        return self.driver.find_element(By.XPATH, f"//img[@id='{product_id}']/../p[2]/a")

    def click_product(self, product_id: int):
        """go to product page by the id of the product"""
        self.product(product_id).click()
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".max-width>h2")))

    def product_name_text(self, product_id: int):
        """return the name text of the product by product id """
        return self.product_name(product_id).text

    def product_price_text(self, product_id: int):
        """return the price text of the product by product id """
        return re.sub(r'[^0-9.]', '', self.product_price(product_id).text)