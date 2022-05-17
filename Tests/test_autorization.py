from pages.LoginPage import Action_Login
from pages.LoginPage import Check_Login
from pages.MainPage import Check_Main
import pytest


@pytest.mark.skip(reason="Убрали сообщение: Неверная учетная запись или пароль")
def test_wrong_password(browser):
    main_page = Action_Login(browser)
    main_page.go_to_site()
    main_page.enter_login_and_password("admin", '0000')
    main_page = Check_Login(browser)
    message = main_page.check_wrong_login_message()
    assert 'Неверная учетная запись или пароль' in message, browser.get_screenshot_as_file(test_wrong_password.__name__ + ' ' + 'FAILED.png')


def test_wrong_login(browser):
    main_page = Action_Login(browser)
    main_page.go_to_site()
    main_page.enter_login_and_password("admin1", 'zj#KqU1')
    main_page = Check_Login(browser)
    message = main_page.check_wrong_login_message()
    assert 'Неверные учетные данные пользователя' in message, browser.get_screenshot_as_file(test_wrong_login.__name__ + ' ' + 'FAILED.png')

def test_success(browser):
    main_page = Action_Login(browser)
    main_page.go_to_site()
    main_page.enter_login_and_password("admin", 'zj#KqU1')
    main_page = Check_Main(browser)
    title = main_page.check_title()
    assert "Сервер сообщений" in title, browser.get_screenshot_as_file(test_success.__name__ + ' ' + 'FAILED.png')

