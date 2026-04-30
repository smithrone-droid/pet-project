from pages.main_page import MainPage
from pages.login_page import LoginPage


# pytest -v --tb=line --language=en test_main_page.py
def test_guest_can_go_to_login_page(browser):
    # Определяем URL главной страницы магазина.
    link = "http://selenium1py.pythonanywhere.com/"
    # Создаём объект страницы MainPage, передавая браузер и ссылку.
    page = MainPage(browser, link)
    # Открываем главную страницу в браузере.
    page.open()
    # Переходим на страницу логина по ссылке с главной страницы.
    page.go_to_login_page()
    # Создаём объект LoginPage для текущего URL после перехода.
    login_page = LoginPage(browser, browser.current_url)
    # Проверяем, что текущая страница действительно является страницей логина.
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
