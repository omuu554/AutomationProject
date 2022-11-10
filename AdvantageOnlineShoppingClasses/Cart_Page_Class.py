from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    def product_name(self, product_location: int):
        """get name element of the product by the location of the product in the table"""
        return self.driver.find_element(By.XPATH, f"//div[@id='shoppingCart']/table/tbody/tr[{product_location}]/td[2]/label")

    def product_color(self, product_location: int):
        """get color element of the product by the location of the product in the table"""
        return self.driver.find_element(By.XPATH, f"//div[@id='shoppingCart']/table/tbody/tr[{product_location}]/td[4]/span")

    def product_quantity(self, product_location: int):
        """get quantity element of the product by the location of the product in the table"""
        return self.driver.find_element(By.XPATH, f"//div[@id='shoppingCart']/table/tbody/tr[{product_location}]/td[5]/label[2]")

    def units_price(self, product_location: int):
        """get product units price element of the product by the location of the product in the table"""
        return self.driver.find_element(By.XPATH, f"//div[@id='shoppingCart']/table/tbody/tr[{product_location}]/td[6]/p")

    def edit_product(self, product_location: int):
        """get edit element of the product by the location of the product in the table"""
        return self.driver.find_element(By.XPATH, f"//div[@id='shoppingCart']/table/tbody/tr[{product_location}]/td[6]/span/a[1]")

    def remove_product(self, product_location: int):
        """get remove element of the product by the location of the product in the table"""
        return self.driver.find_element(By.XPATH, f"//div[@id='shoppingCart']/table/tbody/tr[{product_location}]/td[6]/span/a[3]")

    def total_price(self):
        """get total price element of all the products in the cart"""
        return self.driver.find_element(By.XPATH, "//div[@id='shoppingCart']/table/tfoot/tr[1]/td[2]/span[2]")
    def check_out_button(self):
        """get check out button element"""
        return self.driver.find_element(By.ID, "checkOutButton")

    def continue_shopping(self):
        """get continue shopping button element"""
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='CONTINUE_SHOPPING']")

    def product_name_text(self, product_location: int):
        """return the name text of the product by product location in the table """
        return self.product_name(product_location).text

    def product_color_name(self, product_location: int):
        """return the color text of the product by location in the table """
        return self.product_color(product_location).text

    def product_quantity_text(self, product_location: int):
        """return the quantity text of the product by location in the table """
        return int(self.product_quantity(product_location).text)

    def units_price_text(self, product_location: int):
        """return the units price text in number of the product by product location in table """
        return float(re.sub(r'[^0-9.]', '', self.units_price(product_location).text))

    def edit_product_click(self, product_location: int):
        """click on edit of the product by location of the product in table"""
        self.edit_product(product_location).click()
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".max-width>h2")))

    def remove_product_click(self, product_location: int):
        """remove the product by the location of the product in table"""
        self.remove_product(product_location).click()

    def total_price_text(self):
        """return the total price in number"""
        return float(re.sub(r'[^0-9.]', '', self.total_price().text))

    def check_out_button_click(self):
        """click on check out button"""
        self.check_out_button().click()

    def continue_shopping_click(self):
        """click on continue shopping button"""
        self.continue_shopping().click()

    def Wait_UntilInCartPage(self):
        "Waits for the CartPagetoLoad"
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.uiview>section>article>h3")))
