from playwright.sync_api import Page
from typing import Dict


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://effective-mobile.ru"
        self.navigation_locators = {
            "О нас": "a[href*='about']",
            "Вакансии": "a[href*='specializations']",
            "Отзывы": "a[href*='testimonials']",
            "Контакты": "a[href*='contact']",
            "Аутстафф": "a[href*='services']",
            "Трудоустройство": "a[href*='services']",
            "Консультации": "a[href*='contact']"
        }

    def navigate(self):
       self.page.goto(self.base_url)

    def click_navigation_item(self, item_name: str):
        locator = self.navigation_locators.get(item_name)
        if not locator:
            raise ValueError(f"Блок '{item_name}' не найден")

        self.page.click(locator)
        self.page.wait_for_load_state('networkidle')

    def get_current_url(self) -> str:
        return self.page.url

    def get_page_title(self) -> str:
        return self.page.title()

    def is_navigation_item_visible(self, item_name: str) -> bool:
        locator = self.navigation_locators.get(item_name)
        return self.page.is_visible(locator) if locator else False
