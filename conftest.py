import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--language", action="store", default="en")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    lang = request.config.getoption("--language")
    print(f"\nЗапуск браузера {browser_name}")
    print(f"\nЯзык браузера {lang}")

    if browser_name == "chrome":
        options = ChromeOptions()

        prefs = {"intl.accept_languages": lang}
        options.add_experimental_option("prefs", prefs)
        options.add_argument(f"--lang={lang}")

        print("\nЗапускаем браузер для теста")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )


    elif browser_name == "firefox":
        options = Options()
        options.add_argument("--no-sandbox")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise pytest.UsageError("параметр --browser должен быть chrome или firefox")


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