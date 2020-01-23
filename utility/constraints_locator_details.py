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