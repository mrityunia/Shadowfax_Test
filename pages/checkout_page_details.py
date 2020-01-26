# Created by ********  chomri01 at 1/26/2020

# Feature Name :: --

# To Do ::-

from utility.constraints_locator_details import *
from selenium.webdriver.common.by import By
from utility.web_element_helpper import *


class CartDetails(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser
		)
		self.element_helper = WebHelpper(context=context)
		pass

	location_directory = {
		"place_order": (By.XPATH, place_order),
		"cart_products": (By.XPATH, cart_prodct),
		"delivery_address": (By.XPATH, delivery_address),
		"login_or_signup": (By.XPATH, login_or_signup),
		"loigin_id": (By.TAG_NAME, 'Input'),
		"login_continue": (By.XPATH, login_continure),
		"login_passoword": (By.XPATH, loging_password),
		"login": (By.XPATH, login),
		"delevery_address_options": (By.CSS_SELECTOR, delivery_address_options),
		"delevery_button": (By.XPATH, deliver_button),
		"order_summary": (By.XPATH, order_summary),
		"product_not_availble": (By.PARTIAL_LINK_TEXT, "The following item is Not"),
		"net_anking": (By.XPATH, net_banking),
		"bank_drop": (By.XPATH, bank_drop),
		"payble": (By.XPATH, payble_button)
	}

	def items_is_present(self, item_name):
		is_present = False
		try:
			logging.info('Searching product in cart is {} '.format(item_name))
			products = self.element_helper.we_find_element(*self.location_directory["cart_products"])
			logging.info('web Product Name is {} '.format(products.text))
			if products.text == item_name:
				is_present = True
				logging.info('{} items is present in cart details page '.format(item_name))
			else:
				logging.info('{} items is not present in cart details page '.format(item_name))

		except:
			logging.error('Some error occurred in items found {} ' + str(sys.exc_info()))
		return is_present

	def place_order_from_cart(self):
		try:
			logging.info("Inserting into place order page")
			if self.element_helper.we_display_element(*self.location_directory["place_order"]):
				self.element_helper.we_click(*self.location_directory["place_order"])
				logging.info('Clicked on place order button')
				self.element_helper.we_highlight_element(*self.location_directory["delivery_address"])
				logging.info("Delivery address is showing")
				return True
			else:
				return False
		except:
			logging.error('Some error occured in place order {} ' + str(sys.exc_info()))
			return False

	def enter_id_password(self, user_id, password):
		try:
			logging.info(' user id {0} and password {1} '.format(user_id, password))
			if self.element_helper.we_display_element(*self.location_directory["login_or_signup"]):
				if self.element_helper.we_enabled(*self.location_directory["loigin_id"]):
					self.element_helper.we_send_keys(*self.location_directory["loigin_id"], data=user_id)
					if self.element_helper.we_highlight_element(*self.location_directory["login_continue"]):
						self.element_helper.we_click(*self.location_directory["login_continue"])
						if self.element_helper.we_enabled(*self.location_directory["login_passoword"]):
							self.element_helper.we_send_keys(*self.location_directory["login_passoword"], data=password)
							if self.element_helper.we_highlight_element(*self.location_directory["login"]):
								self.element_helper.we_click(*self.location_directory["login"])
								logging.info('Able to login to Flipkart ')
								return True
							else:
								logging.error("Login button is not present")
								return False
						else:
							logging.error('password enter box is not enabled ')
							return False
					else:
						logging.error('Login Continue button is not present')
						return False
				else:
					logging.error("User id Enter text box is not enabled ")
					return False
			else:
				logging.error('Sign in option is not present')
				return False
		except:
			logging.error('Some error occurred at login {} '.format(sys.exc_info()))
			return False

	def select_deleviry_address(self):
		is_selected_delevery = False
		try:

			if self.element_helper.we_highlight_element(*self.location_directory["delevery_button"]):
				logging.info("Delevery Here buttons is displaying")
				address = self.element_helper.we_find_elements(*self.location_directory["delevery_address_options"])
				logging.info('total availbel delivery options are {} '.format(str(len(address))))
				if len(address) > 1:
					self.element_helper.we_click(*self.location_directory["delevery_button"])
					logging.info("click on selected delvery adderess ")

					if self.element_helper.we_display_element(*self.location_directory["order_summary"]):
						logging.info("Order summary page is displaying")
						is_selected_delevery = True
				else:
					logging.info('Delivery address need to add')
			else:
				logging.error("Delivery Button is not displaying")
		except:
			logging.error('Some error occurred at Delevery address {} '.format(sys.exc_info()))
		return is_selected_delevery

	def conf_order_summary(self):
		try:
			if self.element_helper.we_highlight_element(*self.location_directory["order_summary"]):
				self.element_helper.we_click(*self.location_directory["order_summary"])
				logging.info(" payment page is opening")
				if self.element_helper.we_display_element(*self.location_directory["net_anking"]):
					logging.info("Net banking is showing")
					return True
			else:
				logging.error("Order summary page is not opened")
				return False
		except:
			logging.error('Some error occurred at conf order summary {} '.format(sys.exc_info()))
			return False

	def dumy(self):
		return True

	def select_netbanking(self):
		try:
			if self.element_helper.we_highlight_element(*self.location_directory["net_anking"]):
				self.element_helper.we_click(*self.location_directory["net_anking"])
				logging.info('net banking option is showing')
				if self.element_helper.we_display_element(*self.location_directory["bank_drop"], timeout=70):
					logging.info("Net bank dropdown is displaying")
					return True
			else:
				logging.error('Net banking is not showing')
		except:
			logging.error('Some error occurred at select net banking {} '.format(sys.exc_info()))
			return False

	def select_bank(self, bank_name):
		try:
			logging.info(' TO Be select {} '.format(bank_name))
			if self.element_helper.we_highlight_element(*self.location_directory["bank_drop"]):
				bank_options = Select(self.element_helper.we_find_element(*self.location_directory["bank_drop"]))
				for sl in bank_options.options:
					if bank_name in sl.text:
						bank_options.select_by_visible_text(bank_name)
						logging.info('{} bank  is selcted from web banks')
						if self.element_helper.we_display_element(*self.location_directory["payble"]):
							return True
			else:
				logging.error('bank ioptions is not present')
				return False
		except:
			logging.error('Some error occurred at select banking {} '.format(sys.exc_info()))
			return False

	def payment_by_bank(self):
		try:
			if self.element_helper.we_highlight_element(*self.location_directory["payble"]):
				if self.element_helper.we_enabled(*self.location_directory["payble"]):
					import time
					time.sleep(3)
					self.element_helper.we_click(*self.location_directory["payble"])
					logging.info("navigating to payment page")
					time.sleep(2)
					bank_current_url=self.Browser.current_url
					logging.info("current url is {} ".format(str(bank_current_url)))
					if bank_current_url.find('corpnetbanking.com'):
						logging.info("orpnetbanking is opened ")
						import datetime
						sc_name=SOLUTION_DICTIONARY()+"\\testdata\\orpnetbanking" +".png"
						logging.info("Screen shot name us {} ".format(sc_name))
						self.Browser.save_screenshot(sc_name)
						logging.info("Screen shot is saved ")
						return True
				else:
					logging.error("Payable button is not displaying")
			else:
				return False
		except:
			logging.error('Some error occurred at payment_by_bankg {} '.format(sys.exc_info()))
			return False
