# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::- will store all the constraints deatls and locator
import os

app_url = "https://www.flipkart.com/"
browsers_name = ("chrome", "chromeheadless", "firefox")



def SOLUTION_DICTIONARY():
	print("SOLUTION_DICTIONARY is {}".format(os.getcwd()))
	return os.getcwd()

chrome_path=SOLUTION_DICTIONARY()+"//testdata//chromedriver.exe"
firefox_path=SOLUTION_DICTIONARY()+"//testdata//geckodriver.exe"

## flipkart locators
login_popup=".mCRfo9>div>div>button"
electronic_subcat="//span[text()='Electronics']"
OPPO="//a[@title='OPPO']"
oppo_page_label="//h1[text()='OPPO Mobile phones']"
oppo_view_all="(//span[text()='VIEW ALL'])[1]"
oppo_all_mobile="//a[@rel='noopener noreferrer']"
oppo_mobile_count="//h1[text()='Mobiles']/following-sibling::span"
oppo_phone_name_pdp="(//div[@class='bhgxx2 col-12-12'])[4]/div[1]/div/h1/span"
add_to_cart="//button[text()='ADD TO CART']"
home_logo="//img[@title='Flipkart']"
cart="//span[text()='Cart']"
cart_prodct="//div[@class='bhgxx2 col-12-12']/div/div/div/div/a"
place_order="//span[text()='Continue']|//span[text()='Place Order']"
delivery_address="//span[text()='Delivery Address']"
login_or_signup="//span[text()='Login or Signup']"
login_continure="//span[text()='CONTINUE']"
loging_password="//input[@type='password']"
login="//span[text()='Login']"
delivery_address_options=".A1v2GV"
deliver_button="//button[text()='Deliver Here']"
order_summary="//button[text()='CONTINUE']"
net_banking="//div[text()='Net Banking']"
bank_drop="//div[@class='TKBvsm qimlL8']/select"
payble_button="//button[contains(text(),'PAY ')]"