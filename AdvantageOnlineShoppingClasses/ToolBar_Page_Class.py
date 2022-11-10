from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class ToolBarClass:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    def Get_AdvLogo_Element(self):
        "returns the element of the SiteLogo in the toolbar"
        return self.driver.find_element(By.CSS_SELECTOR,"a[ng-click='go_up()']")

    def Get_MenuSearchIcon_Element(self):
        "returns the element of the SearchIcon in the toolbar"
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='search']>a>svg")

    def Get_Usericon_Element(self):
        "returns the element of the UserIcon in the toolbar"
        return self.driver.find_element(By.ID,"menuUserLink")

    def Get_Carticon_Element(self):
        "returns the element of the CartIcon in the toolbar"
        return self.driver.find_element(By.ID,"menuCart")

    def Click_CartIcon(self):
        "Clicks on the cart icon"
        self.Get_Carticon_Element().click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.uiview>section>article>h3")))

    def Wait_CartIconWindowClose(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "tool-tip-cart[id='toolTipCart']>div")))

    def Get_CloseSearch_Element(self):
        "returns the element of the X in the searchBar after it has been opened in the toolbar"
        if(self.driver.find_element(By.ID,"autoComplete").is_displayed()):
            return self.driver.find_element(By.CSS_SELECTOR,"div[data-ng-click='closeSearchForce()']")
        self.Get_MenuSearchIcon_Element().click()
        return self.driver.find_element(By.CSS_SELECTOR,"div[data-ng-click='closeSearchForce()']")

    def Get_SearchBar_Element(self):
        "returns the element of the Searchbar after it has been opened in the toolbar"
        if (self.driver.find_element(By.ID, "autoComplete").is_displayed()):
            return self.driver.find_element(By.ID,"autoComplete")
        self.Get_MenuSearchIcon_Element().click()
        return self.driver.find_element(By.ID,"autoComplete")

    def Click_SearchBar(self):
        "Presses Enter after the searchbar Has been Opened in the toolbar!"
        SearchIconElement = self.Get_SearchBar_Element()
        SearchIconElement.send_keys(Keys.ENTER)


    def Get_ItemsAmountInCart_Element(self):
        "returns the element of the Amount of items cartIcon in the toolbar"
        return self.driver.find_element(By.XPATH, "//tool-tip-cart[@id='toolTipCart']/div/table/tfoot/tr[1]/td[1]/span/label")

    def ItemsAmountInCartDigits(self):
        "returns Amount of items in cartIcon "
        return int(re.sub(r'[^0-9]','',self.Get_ItemsAmountInCart_Element().get_attribute("textContent")))

    def Get_ItemsTotalCostInCart_Element(self):
        "returns the element of the Cost of all items in cartIcon in the toolbar"
        return self.driver.find_element(By.XPATH, "//tool-tip-cart[@id='toolTipCart']/div/table/tfoot/tr[1]/td[2]/span")

    def ItemsTotalCostInCartDigits(self):
       "returns Total cost of items in cartIcon "
       return float(re.sub(r'[^0-9.]', '', self.Get_ItemsTotalCostInCart_Element().get_attribute("textContent")))

    def Get_CartIconCheckOut_Element(self):
        "returns the element of CheckOut button in the cartIcon in toolbar"
        return self.driver.find_element(By.ID,"checkOutPopUp")

    def Click_CartIconCheckOut(self):
        self.Get_CartIconCheckOut_Element().click()

    def Get_CartIconItemCost_Element(self,index:int):
        "returns the element of a spacifice item Cost from CartIcon in toolbar"
        return self.driver.find_element(By.XPATH,f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[3]/p")

    def CartIconItemCostDigits(self,index:int):
        "returns Cost of specifice item in cartIcon "
        return float(re.sub(r'[^0-9.]', '', self.Get_CartIconItemCost_Element(index).get_attribute("textContent")))

    def Get_CartIconItemName_Element(self,index:int):
        "returns the element of part of the name of a spacifice item from CartIcon in toolbar in format: xxxxxx..."
        return self.driver.find_element(By.XPATH,f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/h3")

    def CartIconItemNameSTR(self,index:int):
        "returns part of the name of a spacifice item from CartIcon in toolbar"
        return self.Get_CartIconItemName_Element(index).text.replace(".",'')

    def Get_CartIconQuntity_Element(self,index:int):
        "returns the element of the item Quantity of spacifice item in CartIcon in toolbar"
        return self.driver.find_element(By.XPATH, f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/label[1]")

    def CartIconQuntityDigits(self,index:int):
        "returns Quantity of specifice item in cartIcon "
        return int(re.sub(r'[^0-9]','',self.Get_CartIconQuntity_Element(index).text))

    def Get_CartIconColor_Element(self,index:int):
        "returns the element of the item color of spacifice item in CartIcon in toolbar in form: all upper case letters"
        return self.driver.find_element(By.XPATH,f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a/label[2]/span")
    def Get_CartIconItemPrice_Element(self,index:int):
        "returns the element of the price of a spacifice item in CartIcon in toolbar"
        return self.driver.find_element(By.XPATH,f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[3]/p")

    def CartIconItemPriceDigits(self,index:int):
        "returns the price of a spacifice item in CartIcon in toolbar"
        return float(re.sub(r'[^0-9.]', '', self.Get_CartIconItemPrice_Element(index).text))

    def Get_CartIconRemoveItem_Element(self,index:int):
        "returns Element of remove button for specifice items in CartIcon ToolBar"
        return self.driver.find_element(By.XPATH,f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[3]/div/div")

    def Click_CartIconRemoveItem(self,index:int):
        "Clicks on a spacifice item remove button from shopping cart"
        self.Get_CartIconRemoveItem_Element(index).click()

    def Get_UserIconUsername_Element(self):
        "returns the element of the username after the UserIcon popup is Displayed"
        if(self.driver.find_element(By.CLASS_NAME,"PopUp").is_displayed()):
            return self.driver.find_element(By.NAME, "username")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.NAME,"username")

    def Get_UserIconPassowrd_Element(self):
        "returns the element of the password after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.NAME, "password")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.NAME,"password")

    def Get_UserIconRemCheckBox_Element(self):
        "returns the element of the Remember me checkbox after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.NAME, "remember_me")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.NAME,"remember_me")

    def Get_UserIconSignIn_Element(self):
        "returns the element of the SignIn button after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.ID, "sign_in_btnundefined")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.ID,"sign_in_btnundefined")

    def Get_UserIconCreateAccount_Element(self):
        "returns the element of the Create New Account button after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT")

    def Get_UserIconSignOut_Element(self,username:str):
        "returns the element of the SignOut button after UserIcon was Pressed(User Must be Signed In for it to work)"
        self.wait.until(EC.invisibility_of_element((By.CLASS_NAME, "PopUp")))
        if(self.driver.find_element(By.CSS_SELECTOR,"label[translate='Sign_out'][role='link']").is_displayed()):
            return self.driver.find_element(By.CSS_SELECTOR,"label[translate='Sign_out'][role='link']")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][role='link']")

    def Wait_UserSignIn(self,username:str):
        "Waits for the user to be signed in"
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#menuUserLink>span"),username))

    def Wait_UserSignOut(self):
        "Waits for the user to be signed in"
        self.wait.until(EC.text((By.CSS_SELECTOR, "#menuUserLink>span"), ""))

    def Get_UserIconName_Element(self):
       return self.driver.find_element(By.CSS_SELECTOR,"#menuUserLink>span")
    def IsUserSignedIn(self,username:str):
        return self.Get_UserIconName_Element().text == username

    def Get_UserIconOrders_Element(self):
        "returns the element of the Orders button after UserIcon was Pressed(User Must be Signed In for it to work)"
        self.wait.until(EC.invisibility_of_element((By.CLASS_NAME,"PopUp")))
        if (self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']").is_displayed()):
            return self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']")

    def Get_UserIconMyAccount_Element(self):
        "returns the element of the Orders button after UserIcon was Pressed(User Must be Signed In for it to work)"
        self.wait.until(EC.invisibility_of_element((By.CLASS_NAME, "PopUp")))
        if (self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_account'][role='link']").is_displayed()):
            return self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_account'][role='link']")

    def Get_Location_Element(self):
        "returns the element of The current location of the user)"
        return self.driver.find_elements(By.CSS_SELECTOR, ".pages>a")[-1]

    def LocationName(self):
        "returns the name of the current location of the user(at homepage returns 'HOME'))"
        try:
            return self.Get_Location_Element().text
        except:
            return "HOME"




