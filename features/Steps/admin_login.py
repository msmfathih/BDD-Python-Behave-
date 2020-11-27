import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given('start chrome browser')
def startBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open RentVehicle login page')
def navigateLoginPage(context):
    context.driver.get("http://rentvehicles.multicompetition.com/login")


@then('verify the logo present on the page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH, "//a[contains(text(),'Rent Vehicles')]").is_displayed()
    assert status is True

@then('Enter emailid "{email}" and password "{pwd}"')
def enterCredentials(context,email, pwd):
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then('Click on login button')
def clickLLogin(context):
    context.driver.find_element(By.ID, "btnLogin").click()


@then('User must login to the home page')
def verifyDashboard(context):
    status = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").is_displayed()
    assert status is True


@then('close browser')
def closeApp(context):
    # context.driver.find_element(By.XPATH, "/html/body/div[2]/aside[1]/div/div[4]/div/div/nav/ul/li[4]/a/p").click(),time.sleep(3)
    # context.driver.find_element(By.XPATH, "//p[contains(text(),'Logout')]").click()
    context.driver.close()
