import time
from behave import *
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('start chrome browser')
def startBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open RentVehicle login page')
def movetoLoginPage(context):
    context.driver.get("http://rentvehicles.multicompetition.com/login")


@then('verify the logo present on the page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH, "//a[contains(text(),'Rent Vehicles')]").is_displayed()
    assert status is True


@then('Enter emailid "{email}" and password "{pwd}"')
def enterEmailAddress(context, email, pwd):
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then('Click on login button')
def clickLoginButton(context):
    context.driver.find_element(By.ID, "btnLogin").click()


@then('User must login to the home page')
def verifyHomePage(context):
    status = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").is_displayed()
    assert status is True



@when('Click on driver dropdown')
def click_driver_dropdown(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
    time.sleep(2)


@then('Select Drivers list')
def click_driver_list(context):
    context.driver.find_element(By.XPATH, "//p[contains(text(),'Drivers List')]").click()
    time.sleep(2)


@then('Click on Action view')
def click_action_view(context):
    click_action_view = context.driver.find_element_by_xpath("//tr[4]//td[6]//a[1]")
    click_action_view.click()


@then('Verify driver details pagge title')
def verify_page_title(context):
    verify_driverpage_title = context.driver.find_element(By.XPATH, "//h3[contains(text(),'Driver Details')]")
    assert verify_driverpage_title.text == "Driver Details", time.sleep(2)


@then('Verify driver name')
def verify_driver_name(context):
    status = context.driver.find_element(By.XPATH, "//label[contains(text(),'Driver Name : ashika')]").is_displayed()
    assert status is True


@then('Verify driver email')
def verify_emailid(context):
    link = None
    while not link:
        try:
            link = context.driver.find_element(By.XPATH, "//label[contains(text(),'Email : ashika@gmail1.com')]")
            print("verified email id")
        except NoSuchElementException:
            time.sleep(2)


@then('Verify NIC number')
def verify_nic(context):
    verify_driver_nic = context.driver.find_element(By.XPATH, "//label[contains(text(),'NIC Number: 9200122134V')]")
    if verify_driver_nic is not None:
        print("Driver nic number verified")
    else:
        print("Driver nic number is not verified")


@then('Click on Go back button')
def click_back_button(context):
    context.driver.find_element(By.ID, "cancelButton").click()


@then('close browser')
def closeApp(context):
    context.driver.close()
