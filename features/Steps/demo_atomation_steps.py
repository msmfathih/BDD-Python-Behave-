from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('start chrome browser')
def startBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open demo automation login page')
def navigateLoginPage(context):
    context.driver.get("http://demo.automationtesting.in/")


@then('verify the logo present on the page')
def verifyLogo(context):
    status = context.driver.find_element(By.ID, 'logo').is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()

