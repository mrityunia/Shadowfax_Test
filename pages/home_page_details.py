# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::-
from utility.constraints_locator_details import *
from selenium.webdriver.common.by import By
from utility.web_element_helpper import *


class FlipkartHome(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser)
		self.element_helper = WebHelpper(context=context)
		pass

	locator_dictionary = {
		"login_popup": (By.CSS_SELECTOR, login_popup),
		"electronic_subcat": (By.XPATH, electronic_subcat),
		"oppo_mobile": (By.XPATH, OPPO),
		"oppo_page_label": (By.XPATH, oppo_page_label),
		"cart":(By.XPATH,cart)
	}

	def open_application(self):
		try:
			self.Browser.get(app_url)
			logging.info("{} application is opened ".format(str(app_url)))
			self.Browser.maximize_window()
			return True
		except:
			logging.error("Some error occurred at open application {} ".format(sys.exc_info()))
			return False

	def close_home_popup(self):
		try:
			logging.info("Inserting into close_home_popup()--")
			self.element_helper.we_highlight_element(*self.locator_dictionary["login_popup"])
			self.element_helper.we_click(*self.locator_dictionary["login_popup"])
			return True
		except:
			logging.error('some error occurred during closng the popup {} '.format(sys.exc_info()))
			return False

	def get_electronic(self):
		try:
			logging.info("Inserting into get Electronics ")
			if self.element_helper.we_highlight_element(*self.locator_dictionary["electronic_subcat"]):
				self.element_helper.we_click(*self.locator_dictionary["electronic_subcat"])
				self.element_helper.we_display_element(*self.locator_dictionary["oppo_mobile"])
				return True
		except:
			logging.error("Some error occurred it {} ".format(str(sys.exc_info())))
			return False

	def click_oppo(self):
		try:
			logging.info("Inserting into OPPO click ")
			if self.element_helper.we_highlight_element(*self.locator_dictionary["oppo_mobile"]):
				url = self.element_helper.we_find_element(*self.locator_dictionary["oppo_mobile"]).get_attribute("href")
				logging.info("Oppo URL is {} ".format(url))
				self.Browser.get(url)
				if self.element_helper.we_highlight_element(*self.locator_dictionary["oppo_page_label"]):
					logging.info("OPPO Mobile phones label is displaying")
					return True
		except:
			logging.error("Some error occurred it {} ".format(str(sys.exc_info())))
			return False
	def go_to_cart_from_home(self):
		try:
			if self.element_helper.we_highlight_element(*self.locator_dictionary["cart"]):
				self.element_helper.we_click(*self.locator_dictionary["cart"])
				return True
			else:
				logging.error('Cart is not displaying')
				return False
		except:
			logging.error("Some error occurred it {} ".format(str(sys.exc_info())))
			return False

class OPPOMobilePhone(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser
		)
		self.element_helper = WebHelpper(context=context)

	locator_directory = {
		"oppo_view_all": (By.XPATH, oppo_view_all),
		"oppo_all_mobile": (By.XPATH, oppo_all_mobile),
		"oppo_mobile_count": (By.XPATH, oppo_mobile_count),
		"oppo_phone_pdp": (By.XPATH, oppo_phone_name_pdp),
		"add_to_cart": (By.XPATH, add_to_cart),
		"home_logo":(By.XPATH,home_logo)

	}

	def load_all_mobile(self):
		try:
			if self.element_helper.we_highlight_element(*self.locator_directory["oppo_view_all"]):
				self.element_helper.we_click(*self.locator_directory["oppo_view_all"])
				logging.info("Clicked on View all button")
				return True
		except:
			logging.error('Some error occured at load all mobile {} '.format(sys.exc_info()))
			return False

	def get_oppo_mobile_by_name(self, mobile_name):
		mobile_name_present = False
		try:
			dum_mobile = str(mobile_name).lower()
			dn = ""
			for ch in dum_mobile:
				if ch.isalpha() or ch.isnumeric():
					dn = dn + ch
				else:
					dn = dn + "-"
			dn = dn.replace('-', '')
			logging.info('dummy mobile name {} '.format(dn))
			if self.element_helper.we_highlight_element(*self.locator_directory["oppo_mobile_count"]):
				mobile_count_text = self.element_helper.we_find_element(
					*self.locator_directory["oppo_mobile_count"]).text[9:11]
				logging.info('Total mobile count is {} '.format(str(mobile_count_text)))
				if int(mobile_count_text) > 0:
					logging.info('Mobile count is more than 0')
					mobiles = self.element_helper.we_find_elements(*self.locator_directory["oppo_all_mobile"])
					for mob in mobiles:
						mobile_name_url = mob.get_attribute('href')
						web_mobile_name = str(mobile_name_url).split('/')[3].replace('-', '')
						if dn == web_mobile_name:
							logging.info(
								'{0} is found and the url is {1} '.format(str(mobile_name), str(mobile_name_url)))
							self.Browser.get(str(mobile_name_url))
							if self.element_helper.we_highlight_element(*self.locator_directory["oppo_phone_pdp"]):
								if self.element_helper.we_find_element(
										*self.locator_directory["oppo_phone_pdp"]).text == mobile_name:
									mobile_name_present = True
									logging.info("Navigated to {} product details page ".format(str(mobile_name)))
									break
				else:
					logging.error('Mobile count is 0 , No mobile is present ')
					return mobile_name_present
			else:
				logging.error('OPPO mobile is not loaded ')
		except:
			logging.error('Some error occurred at load all mobile {} '.format(sys.exc_info()))
			return mobile_name_present

	def add_to_cart(self):
		try:
			if self.element_helper.we_highlight_element(*self.locator_directory["add_to_cart"]):
				self.element_helper.we_click(*self.locator_directory["add_to_cart"])
				logging.info("Cliked on add to Cart ")
				return True
			else:
				logging.error('Add to cart button is not displaying')
				return False
		except:
			logging.error('Some error occurred at load all mobile {} '.format(sys.exc_info()))
			return False

	def navigate_to_home(self):
		try:
			if self.element_helper.we_highlight_element(*self.locator_directory["home_logo"]):
				self.element_helper.we_click(*self.locator_directory["home_logo"])
				return True
			else:
				logging.error('Flipkart Home is not displaying')
				return False
		except:
			logging.error('Some error occurred at navigate to Home {} '.format(sys.exc_info()))
			return False
