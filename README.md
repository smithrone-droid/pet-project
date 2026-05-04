# Pet Project: UI-тесты (Python + Pytest + Selenium)

Учебный проект с автотестами интернет-магазина на основе паттерна Page Object.

## Стек

- Python 3.12
- Pytest
- Selenium
- WebDriver Manager
- Black (форматирование)

## Структура проекта

```text
pet-project/
├── conftest.py            # фикстуры браузера + CLI-опции pytest
├── pages/
│   ├── base_page.py       # базовые методы страниц (open, проверки, promo-quiz)
│   ├── locators.py        # локаторы
│   ├── main_page.py       # PageObject главной страницы
│   ├── login_page.py      # PageObject страницы логина
│   └── product_page.py    # PageObject страницы товара
└── tests/
    ├── test_main_page.py
    └── test_product_page.py
```

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск тестов

Запуск всех тестов:

```bash
./.venv/bin/pytest -v --tb=line tests
```

Запуск тестов главной страницы:

```bash
./.venv/bin/pytest -v --tb=line --language=en tests/test_main_page.py
```

Запуск тестов продуктовой страницы:

```bash
./.venv/bin/pytest -v --tb=line --language=ru tests/test_product_page.py
```

Подробный запуск для разбора шагов:

```bash
./.venv/bin/pytest tests/test_product_page.py::test_guest_can_add_product_to_basket \
  -vv -s --setup-show --tb=long --durations=0 --maxfail=1 --browser=chrome --language=ru
```

## Параметры pytest

В `conftest.py` добавлены параметры:

- `--browser=chrome|firefox` (по умолчанию `chrome`)
- `--language=<lang>` (по умолчанию `en`)

Пример:

```bash
./.venv/bin/pytest -v tests/test_main_page.py --browser=firefox --language=ru
```

## Важно про promo-страницы

Для ссылок с `?promo=...` в тесте используется `solve_quiz_and_get_code()` из `BasePage`, чтобы пройти alert с формулой после добавления товара в корзину.

## Форматирование

```bash
./venv/bin/black pages tests conftest.py
```
