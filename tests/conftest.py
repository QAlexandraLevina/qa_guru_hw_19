import os
import allure
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from selenium import webdriver
from config import settings
from utils.attachments import add_screenshot, add_xml, add_video


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23 Ultra",

    "app": "bs://sample.app",

    'bstack:options': {
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",

        "userName": settings.bs_userName,
        "accessKey": settings.bs_accessKey
    }
    })

    browser.config.driver = webdriver.Remote(settings.bs_url, options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    session_id = browser.driver.session_id

    yield

    add_screenshot(browser)
    add_xml(browser)

    with allure.step("Закрытие браузера"):
        browser.quit()

    add_video(session_id, settings.bs_userName, settings.bs_accessKey)