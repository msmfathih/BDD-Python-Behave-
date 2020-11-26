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


# @then('Enter emailid "admin@gmail.com"')
@then('Enter emailid "{email}"')
def enterEmail(context, email):
    context.driver.find_element(By.ID, 'email').send_keys(email)


@then('Click on login button')
def clickLogin(context):
    context.driver.find_element(By.ID, 'enterimg').click()


@then('User must login to the home page')
def verifyPageTitle(context):
    status = context.driver.find_element(By.ID, "//h1[contains(text(),'Automation Demo Site')]").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()

