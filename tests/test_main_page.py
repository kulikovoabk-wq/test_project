import pytest
import allure
from playwright.sync_api import expect
from page.main_page import MainPage


@allure.feature("Главная страница Effective Mobile")
@allure.story("Навигация по сайту")
class TestMainPageNavigation:

    @allure.title("Переход по всем элементам навигации")
    @pytest.mark.parametrize("nav_item,expected_url_pattern", [
        ("О нас", "about"),
        ("Вакансии", "specializations"),
        ("Отзывы", "testimonials"),
        ("Контакты", "contact"),
        ("Аутстафф", "services"),
        ("Трудоустройство", "services"),
        ("Консультации", "contact")
    ])
    def test_navigation_items(self, page, nav_item, expected_url_pattern):
        main_page = MainPage(page)

        with allure.step("Открыть главную страницу"):
            main_page.navigate()

        with allure.step(f"Проверить видимость элемента '{nav_item}'"):
            assert main_page.is_navigation_item_visible(nav_item), \
                f"Элемент навигации '{nav_item}' не виден на странице"

        with allure.step(f"Кликнуть на элемент '{nav_item}'"):
            main_page.click_navigation_item(nav_item)

        with allure.step("Проверить изменение URL"):
            current_url = main_page.get_current_url()
            assert expected_url_pattern in current_url.lower(), \
                f"Ожидаемый паттерн '{expected_url_pattern}' не найден в URL: {current_url}"

        with allure.step("Проверить загрузку страницы"):
            expect(page).to_have_url(f"**/{expected_url_pattern}**")

    @allure.title("Проверка доступности всех элементов навигации")
    def test_all_navigation_items_visible(self, page):
        main_page = MainPage(page)
        main_page.navigate()
        for nav_item in main_page.navigation_locators.keys():
            with allure.step(f"Проверить видимость '{nav_item}'"):
                assert main_page.is_navigation_item_visible(nav_item), \
                    f"Элемент навигации '{nav_item}' не виден"
