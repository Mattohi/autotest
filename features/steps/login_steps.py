from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


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

    text = context.driver.find_element(
        By.ID,
        "flash"
    ).text

    assert "You logged into a secure area!" in text

    context.driver.quit()


@then('User gagal login')
def step_impl(context):

    text = context.driver.find_element(
        By.ID,
        "flash"
    ).text

    assert "Your password is invalid!" in text

    context.driver.quit()