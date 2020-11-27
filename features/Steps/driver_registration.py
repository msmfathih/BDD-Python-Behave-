# import time
# from behave import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
#
# @given('start chrome browser')
# def startBrowser(context):
#     context.driver = webdriver.Chrome(ChromeDriverManager().install())
#
#
# @when('open RentVehicle login page')
# def movetoLoginPage(context):
#     context.driver.get("http://rentvehicles.multicompetition.com/login")
#
#
# @then('verify the logo present on the page')
# def verifyLogo(context):
#     status = context.driver.find_element(By.XPATH, "//a[contains(text(),'Rent Vehicles')]").is_displayed()
#     assert status is True
#
#
# @then('Enter emailid "{email}" and password "{pwd}"')
# def enterEmailAddress(context, email, pwd):
#     context.driver.find_element(By.ID, "email").send_keys(email)
#     context.driver.find_element(By.ID, "password").send_keys(pwd)
#
#
# @then('Click on login button')
# def clickLoginButton(context):
#     context.driver.find_element(By.ID, "btnLogin").click()
#
#
# @then('User must login to the home page')
# def verifyHomePage(context):
#     status = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").is_displayed()
#     assert status is True
#
#
# @when('Click om Drive dropdown')
# def click_Driver_DropDown(context):
#     context.driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
#     time.sleep(2)
#
#
# @then('Click on Driver Registration Page')
# def click_Driver_Page(context):
#     context.driver.find_element(By.XPATH, "//p[contains(text(),'Register Drivers')]").click()
#     time.sleep(2)
#
#
# @then('Enter Drivername "{drivername}"')
# def enter_Driver_Name(context, drivername):
#     context.driver.find_element_by_xpath("//input[@name='name']").send_keys(drivername)
#     time.sleep(2)
#
#
# @then('Enter PhoneNumber "{p_number}"')
# def enter_mobile_number(context, p_number):
#     context.driver.find_element(By.NAME, 'mobile_number').send_keys(p_number)
#     time.sleep(2)
#
#
# @then('Enter Emailid "{email_address}"')
# def enter_emailid(context, email_address):
#     context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email_address)
#     time.sleep(2)
#
#
# @then('Upload Licence copy file')
# def upload_licence_copy(context):
#     context.driver.find_element_by_id("name").send_keys(
#             "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
#     time.sleep(2)
#
#
# @then('Click Owner of this vehicle')
# def vehicle_owner_radio_button(context):
#     element = context.driver.find_element_by_css_selector("input.is_vehicle_owner:nth-child(4)")
#     context.driver.execute_script("arguments[0].click();", element)
#     time.sleep(2)
#
#
# @then('Select Dropdown Vehicle')
# def select_vehicle_type(context):
#     element = context.driver.find_element_by_xpath("//select[@name='vehicle_type_id']")
#     sel2 = Select(element)
#     sel2.select_by_index(2)
#     time.sleep(2)
#
#
# @then('Click submit button')
# def submit_details(context):
#     element = context.driver.find_element_by_id("submitBtn")
#     context.driver.execute_script("arguments[0].click();", element)
#     time.sleep(2)
#
#
# @then('close browser')
# def close_browser(context):
#     context.driver.close()
#     time.sleep(2)
#
#
