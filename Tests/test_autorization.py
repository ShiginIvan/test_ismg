from pages.LoginPage import ActionLogin
from pages.LoginPage import CheckLogin
from pages.MainPage import CheckMain
import pytest


@pytest.mark.skip(reason="Убрали сообщение: Неверная учетная запись или пароль")
def test_wrong_password(browser):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.enter_login_and_password("admin", '0000')
    login_page = CheckLogin(browser)
    message = login_page.check_wrong_login_message()
    assert 'Неверная учетная запись или пароль' in message, browser.get_screenshot_as_file(test_wrong_password.__name__ + ' ' + 'FAILED.png')


def test_wrong_login(browser):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.enter_login_and_password("admin1", 'zj#KqU1')
    login_page = CheckLogin(browser)
    message = login_page.check_wrong_login_message()
    assert 'Неверные учетные данные пользователя' in message, browser.get_screenshot_as_file(test_wrong_login.__name__ + ' ' + 'FAILED.png')


def test_success(browser):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.enter_login_and_password("admin", 'zj#KqU1')
    main_page = CheckMain(browser)
    title = main_page.check_title()
    assert "Сервер сообщений" in title, browser.get_screenshot_as_file(test_success.__name__ + ' ' + 'FAILED.png')

