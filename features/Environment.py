# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --

# To Do ::-
from utility.logger_report_details import *
def before_feature(context, scenario):
	start_logger()
	logging.info("Starting Feature name is {}".format(str(scenario.name)))
	pass
def before_scenario(context, scenario):
	logging.info("Starting scenario ---------")
	pass
def after_feature(context,scenario):
	logging.info("End of Feature ----------")
	pass
def after_scenario(context,scenario):
	logging.info("End of Scenario ------")
	pass
def before_step(context , step):
	logging.info("Starting steps is {} ".format(str(step.name)))
