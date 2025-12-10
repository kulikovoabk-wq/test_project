# Автоматизированные тесты для главной страницы сайта effective-mobile.ru

## Требования

- Python 3.10+
- Docker (для запуска в контейнере)
- Playwright
- Allure

## Структура проекта

test_project/
├── docker/
│   └── Dockerfile
├── page/
│   └── main_page.py
├── tests/
│   └── test_main_page.py
├── requirements.txt
├── conftest.py
├── pytest.ini
└── README.md

## Локальный запуск

```bash
git clone https://github.com/kulikovoabk-wq/test_project.git
cd test_project
pip install -r requirements.txt
playwright install
pip install allure-pytest
# Все тесты
pytest -v
# С генерацией Allure отчетов
pytest --alluredir=./allure-results

## Запуск в Docker:
```bash
git clone https://github.com/kulikovoabk-wq/test_project.git
cd test_project
# Сборка образа
docker build -t test_project -f docker/Dockerfile .
# Запуск тестов в контейнере
docker run --rm test_project
# Запуск с монтированием volume для результатов
docker run --rm -v $(pwd)/allure-results:/app/allure-results test_project
