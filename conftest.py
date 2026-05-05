import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

load_dotenv()

PROMO_LINKS = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.skip(reason="Пропускаем offer7, есть дефект по несовпадению названий"),
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
]


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--language", action="store", default="en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    lang = request.config.getoption("language")

    # Откатили использование Selenium Remote URL
    # selenium_remote_url = os.getenv("SELENIUM_REMOTE_URL")

    print(f"\nЗапуск браузера: {browser_name}")
    print(f"\nЯзык браузера: {lang}")

    # Откатили вывод Selenium Remote URL
    # print(f"\nSelenium Remote URL: {selenium_remote_url}")

    if browser_name == "chrome":
        options = ChromeOptions()

        prefs = {"intl.accept_languages": lang}
        options.add_experimental_option("prefs", prefs)
        options.add_argument(f"--lang={lang}")

        # Откатили Docker/Grid-опции для локального запуска
        # options.add_argument("--headless=new")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--window-size=1920,1080")

        print("\nЗапускаем Chrome для теста")

        # Откатили запуск через Selenium Grid / Remote WebDriver
        # if selenium_remote_url:
        #     driver = webdriver.Remote(
        #         command_executor=selenium_remote_url,
        #         options=options,
        #     )
        # else:
        #     driver = webdriver.Chrome(
        #         service=ChromeService(ChromeDriverManager().install()),
        #         options=options,
        #     )

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    elif browser_name == "firefox":
        options = FirefoxOptions()

        # Откатили Docker/Grid-опции для локального запуска
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")

        options.set_preference("intl.accept_languages", lang)

        print("\nЗапускаем Firefox для теста")

        # Откатили запуск через Selenium Grid / Remote WebDriver
        # if selenium_remote_url:
        #     driver = webdriver.Remote(
        #         command_executor=selenium_remote_url,
        #         options=options,
        #     )
        # else:
        #     driver = webdriver.Firefox(
        #         service=FirefoxService(GeckoDriverManager().install()),
        #         options=options,
        #     )

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )

    else:
        raise pytest.UsageError("Параметр --browser должен быть chrome или firefox")

    yield driver

    print("\nЗакрытие браузера")
    driver.quit()


@pytest.fixture
def credentials():
    login = os.getenv("STEPIK_LOGIN")
    password = os.getenv("STEPIK_PASSWORD")

    if not login or not password:
        pytest.fail("Креды не заданы")

    return login, password


@pytest.fixture(params=PROMO_LINKS)
def link(request):
    return request.param
