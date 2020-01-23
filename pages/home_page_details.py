# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::-
from pages.base_page_details import *
from utility.constraints_locator_details import *


class FlipkartHome(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser)

	def open_application(self):
		try:
			self.Browser.get(app_url)
			logging.info("{} application is opened ".format(str(app_url)))
			return True
		except:
			logging.error("Some error occurred at open application {} ".format(sys.exc_info()))
			return False
