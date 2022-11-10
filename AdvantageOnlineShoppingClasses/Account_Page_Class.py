from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPageClass:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Get_DeleteAccount_Element(self):
        "returns the Element of the Delete Account button"
        return self.driver.find_element(By.CLASS_NAME, "deleteMainBtnContainer")

    def Click_DeleteAccount(self):
        "Clicks on the Delete Account button"
        self.Get_DeleteAccount_Element().click()

    def Get_GetDeleteButton_Element(self):
        "returns the Element of the Delete button"
        return self.driver.find_element(By.CLASS_NAME,"deleteRed")

    def Click_DeleteButton(self):
        "Clicks on the Delete button"
        self.Get_GetDeleteButton_Element().click()

    def Get_GetCloseButton_Element(self):
        "returns the Element of the Close Delete Window button"
        return self.driver.find_element(By.CLASS_NAME, "deleteRed")

    def Click_CloseButton(self):
        "Clicks on the Close Delete Window button"
        self.Get_GetDeleteButton_Element().click()

    def Get_EditPaymentMethod_Element(self):
        "returns the Element of the edit button for the payment methods"
        return self.driver.find_element(By.XPATH, "//div[@id='myAccountContainer']/div[4]/h3/a")

    def Click_EditPaymentMethod(self):
        "Clicks on edit button for the payment methods"
        self.Get_EditPaymentMethod_Element().click()

    def Get_PaymentMethodSelected_Element(self):
        "returns the Element of the currently selected payment method"
        return self.driver.find_element(By.CLASS_NAME,"selected")

    def Get_PaymentMethod_Element(self,index:int):
        "returns the Element of a payment method by index"
        return self.driver.find_element(By.XPATH, f"//div[@class='paymentMethods']/div[{index}]")

    def Wait_UserAccountPageLoaded(self):
        "Waits until user is at the MyAccount Page"
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[translate='MY_ACCOUNT']")))

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
        "returns the Element of the Save Button MasterCard"
        return self.driver.find_element(By.CSS_SELECTOR, "sec-sender[sec-send='_saveMasterCredit()']>button")

    def Click_SaveMasterCard(self):
        "Click Save Button MasterCard"
        self.Get_SaveMasterCard_Element().click()


