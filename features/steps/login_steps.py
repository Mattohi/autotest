from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('User membuka halaman login')
def step_impl(context):

    context.driver = webdriver.Safari()
    context.driver.maximize_window()
    context.driver.get(
        "https://the-internet.herokuapp.com/login"
    )


@when('User memasukkan username "{username}"')
def step_impl(context, username):

    context.driver.find_element(
        By.ID,
        "username"
    ).send_keys(username)


@when('User memasukkan password "{password}"')
def step_impl(context, password):

    context.driver.find_element(
        By.ID,
        "password"
    ).send_keys(password)


@when('User menekan tombol login')
def step_impl(context):

    context.driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()


@then('User berhasil login')
def step_impl(context):

    flash = WebDriverWait(
        context.driver,10
    ).until(
        EC.presence_of_element_located(
            (By.ID,"flash")
        )
    )

    assert "You logged into a secure area!" in flash.text
    context.driver.quit()


@then('User gagal login')
def step_impl(context):

    flash = WebDriverWait(
        context.driver,10
    ).until(
        EC.presence_of_element_located(
            (By.ID,"flash")
        )
    )

    assert "Your password is invalid!" in flash.text
    context.driver.quit()