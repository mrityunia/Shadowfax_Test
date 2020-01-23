# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::-
from pages.base_page_details import *
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
		"oppo_page_label": (By.XPATH, oppo_page_label)
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
				url=self.element_helper.we_find_element(*self.locator_dictionary["oppo_mobile"]).get_attribute("href")
				logging.info("Oppo URL is {} ".format(url))
				self.Browser.get(url)
				if self.element_helper.we_highlight_element(*self.locator_dictionary["oppo_page_label"]):
					logging.info("OPPO Mobile phones label is displaying")
					return True
		except:
			logging.error("Some error occurred it {} ".format(str(sys.exc_info())))
			return False
