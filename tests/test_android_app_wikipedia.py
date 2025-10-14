import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with allure.step("Клик по поисковой строке"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step("Ввод текста в поисковую строку"):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Java language')

    with allure.step("Проверка результатов поиска"):
        search_result = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))

    with allure.step("Клик по первому найденному элементу поиска"):
        first_search_result = search_result.first.should(have.text('Java (programming language)'))
        first_search_result.click()