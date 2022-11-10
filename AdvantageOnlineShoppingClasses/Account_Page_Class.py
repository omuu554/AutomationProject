from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AccountPageClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def Get_DeleteAccount_Element(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteMainBtnContainer")

    def Click_DeleteAccount(self):
        self.Get_DeleteAccount_Element().click()

    def Get_GetDeleteButton_Element(self):
        return self.driver.find_element(By.CLASS_NAME,"deleteRed")

    def Click_DeleteButton(self):
        self.Get_GetDeleteButton_Element().click()

    def Get_GetCloseButton_Element(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteRed")

    def Click_CloseButton(self):
        self.Get_GetDeleteButton_Element().click()




    def Get_EditPaymentMethod_Element(self):
        return self.driver.find_element(By.XPATH, "//div[@id='myAccountContainer']/div[4]/h3/a")

    def Click_EditPaymentMethod(self):
        self.Get_EditPaymentMethod_Element().click()

    def Get_PaymentMethodSelected_Element(self):
        self.driver.find_element(By.CLASS_NAME,"selected")

    def Get_PaymentMethod_Element(self,index:int):
        return self.driver.find_element(By.XPATH, f"//div[@class='paymentMethods']/div[{index}]")

    def Get_CardNumber_Element(self):
        "Returns the Element of Card Number of MasterCard"
        return self.driver.find_element(By.ID,"creditCard")

    def Get_CVVNumber_Element(self):
        "Returns the Element of CVV Number of MasterCard"
        return self.driver.find_element(By.NAME,"cvv_number")

    def Get_ExpirationDateMonth_Element(self):
        "Returns the Element of the Month Expiration Date of MasterCard"
        return self.driver.find_element(By.NAME,"mmListbox")

    def Select_ExpirationDateMonth(self,MonthNumber:int):
        "Chooses Month Number from Month Expiration Date dropdown list"
        MonthSelector = Select(self.Get_ExpirationDateMonth_Element())
        if(MonthNumber<10):
            MonthSelector.select_by_visible_text(f"0{MonthNumber}")
        else:
            MonthSelector.select_by_visible_text(f"{MonthNumber}")

    def Get_ExpirationDateYear_Element(self):
        "Returns the Element of the Year Expiration Date of MasterCard"
        return self.driver.find_element(By.NAME, "yyyyListbox")

    def Select_ExpirationDateYear(self, YearNumber: int):
        "Chooses Year Number from Year Expiration Date dropdown list"
        YearSelector = Select(self.Get_ExpirationDateYear_Element())
        YearSelector.select_by_visible_text(f"{YearNumber}")

    def Get_CardHolder_Element(self):
        "Returns the Element of The Card Holder of MasterCard"
        return self.driver.find_element(By.NAME, "cardholder_name")

    def Get_SaveMasterCard_Element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "sec-sender[sec-send='_saveMasterCredit()']>button")

    def Click_SaveMasterCard(self):
        self.Get_SaveMasterCard_Element().click()


