# Created by ********  chomri01 at 1/23/2020

# Feature Name :: --Steps of Flipkart test

# To Do ::- this module for all the steps for Flipkart_tes feature


from behave import given,when,then
from pages.home_page_details import *
from pages.checkout_page_details import *
@given(u'the user opens Flipkart')
def step_impl(context):
	global home_page
	home_page=FlipkartHome(context)
	assert True is home_page.open_application()
	assert True is home_page.close_home_popup()
	pass


@when(u'the user navigates to "{sub_category}" options')
def step_impl(context,sub_category):
	logging.info("User selects {} as sub category ".format(str(sub_category)))
	assert True is home_page.get_electronic()
	pass


@when(u'selects "{product_category}"')
def step_impl(context,product_category):
	logging.info("User selects product is {} ".format(str(product_category)))
	assert True is home_page.click_oppo()
	pass


@then(u'product list page is opened')
def step_impl(context):
	global oppo_mobile
	oppo_mobile=OPPOMobilePhone(context=context)
	assert True is oppo_mobile.load_all_mobile()



@when(u'the user selects "{product}"')
def step_impl(context,product):
	logging.info("User selects {} as a product ".format(str(product)))
	assert  True is oppo_mobile.get_oppo_mobile_by_name(product)
	context.mobile_name = product



@when(u'clicks on add to cart')
def step_impl(context):
	assert True is oppo_mobile.add_to_cart()

@when(u'the user navigates to Flipkart main page by clicking Home icon')
def step_impl(context):
	assert True is oppo_mobile.navigate_to_home()

@when(u'the user navigates to cart page')
def step_impl(context):
	assert True is home_page.go_to_cart_from_home()

@then(u'the item is present in cart')
def step_impl(context):
	global cart_details
	cart_details = CartDetails(context=context)
	assert True is cart_details.items_is_present(str(context.mobile_name))

@when(u'the user clicks on place the order')
def step_impl(context):

	assert True is cart_details.place_order_from_cart()
	pass


@when(u'the user enters "{user_id}" and "{password}"')
def step_impl(context,user_id,password):
	assert True is cart_details.enter_id_password(user_id=user_id,password=password)
	assert True is cart_details.select_deleviry_address()
	pass
@when(u'clicks on Submit')
def step_impl(context):
	assert True is cart_details.conf_order_summary()
	pass

@then(u'user navigates to payment options page')
def step_impl(context):
	cart_details.dumy()
	pass


@when(u'the user clicks on net banking')
def step_impl(context):
	assert True is cart_details.select_netbanking()
	pass


@when(u'selects bank as "{bank_name}"')
def step_impl(context,bank_name):
	logging.info("Select bank Name is {} ".format(str(bank_name)))
	assert True is cart_details.select_bank(bank_name)
	pass


@then(u'user takes a screen shot of the page')
def step_impl(context):
	assert True is cart_details.payment_by_bank()
	pass
