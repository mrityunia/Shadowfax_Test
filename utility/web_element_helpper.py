# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::- This is for common web element methods will be used for

from pages.base_page_details import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class WebHelpper(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser
		)

	def we_find_element(self, *locator):
		try:
			elm = self.Browser.find_element(*locator)
			if elm is not None:
				return elm
			else:
				return None
		except Exception:
			logging.error("Some error Occurred during find an element" + str(sys.exc_info()))
			return None
		pass

	def we_find_elements(self, *locator):
		try:
			elms = self.Browser.find_elements(*locator)
			if elms is not None:
				return elms
			else:
				return None
		except:
			logging.error("Some error Occurred during find an element" + str(sys.exc_info()))
			return None

	def we_highlight_element(self, *locator):
		try:
			if self.we_display_element(*locator):
				self.Browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
				                            self.we_find_element(*locator), "border: 4px solid blue;")
				logging.info("Element is highlighted")
				return True
		except:
			logging.error("not able to highlight element {} ".format(str(sys.exc_info())))
			return False

	def we_display_element(self, *locator, timeout=60):
		try:
			wait = WebDriverWait(self.Browser, timeout=timeout)
			wait.until(EC.presence_of_element_located(locator))
			self.we_find_element(*locator).is_displayed()
			logging.info("Element is displaying now ----")
			return True
		except:
			logging.error("Element is not displaying within the time limit {} ".format(sys.exc_info()))
			return False
		pass

	def we_click(self, *locator):
		try:
			self.we_find_element(*locator).click()
			logging.info("Clicked on the element")
			return True
		except:
			logging.error("Element is not displaying within the time limit {} ".format(sys.exc_info()))
			return False
		pass

	def we_enabled(self, *locator):
		try:
			if self.we_display_element(*locator):
				if self.we_find_element(*locator).is_enabled():
					logging.info('element is enabled')
					return True
				else:
					return False
			else:
				return False
		except:
			logging.error("element enabled exception".format(sys.exc_info()))
			return False
	def we_send_keys(self,*locator,data):
		try:
			if self.we_enabled(*locator):
				self.we_find_element(*locator).send_keys(data)
				logging.info('{} data is entered into the field'.format(data))
			else:
				logging.error('Element is not enabled so not able to enter data into the field')
		except:
			logging.error("element entered  exception".format(sys.exc_info()))
	def we_select_by_value(self,*locator,data):
		try:
			sl=Select(self.we_find_element(*locator))
			sl.select_by_value(data)
			logging.info('{} data is selected '.format(data))
		except:
			logging.error('Some error occurred during select By Value')




