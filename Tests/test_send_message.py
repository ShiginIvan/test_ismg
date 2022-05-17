from pages.LoginPage import ActionLogin
from pages.MainPage import ActionMain
from pages.MessageCreatePage import ActionMessageCreate
from pages.MessageCreateStatusPage import CheckMessageCreateStatus
from pages.MessageCreateStatusPage import ActionMessageCreateStatus
from pages.DataMessagesPage import CheckDataMessages
import pytest


@pytest.mark.parametrize('title, message, address',
                         [
                             ('заголовок', 'сообщение', '79101234567'),
                             ('check', 'mess', '79101234569'),
                             ('!', '@', '79101234560')
                         ])
def test_send_default_page_create_status(browser, title, message, address):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_default(title, message, address)
    message_create_status_page = CheckMessageCreateStatus(browser)
    check = message_create_status_page.check_message_status()
    assert 'Создание сообщений успешно: Отправлено сообщений: 1' in check, browser.get_screenshot_as_file(test_send_default_page_create_status.__name__ + ' ' + 'FAILED.png')


def test_send_default_page_data_messages(browser):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_default('заголовок', 'сообщение', '79101234567')
    message_create_page = ActionMessageCreateStatus(browser)
    message_create_page.open_data_messages()
    data_messages_page = CheckDataMessages(browser)
    check = data_messages_page.check_message_status()
    assert 'Прочитано' in check, browser.get_screenshot_as_file(test_send_default_page_data_messages.__name__ + ' ' + 'FAILED.png')


def test_send_push_page_create_status(browser):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_schema('заголовок', 'сообщение', '79101234567', 'push')
    message_create_status_page = CheckMessageCreateStatus(browser)
    check = message_create_status_page.check_message_status()
    assert 'Создание сообщений успешно: Отправлено сообщений: 1' in check, browser.get_screenshot_as_file(test_send_push_page_create_status.__name__ + ' ' + 'FAILED.png')


def test_send_push_page_data_messages(browser):
    login_page = ActionLogin(browser)
    login_page.go_to_site()
    login_page.authorization()
    main_page = ActionMain(browser)
    main_page.open_create_message()
    message_create_page = ActionMessageCreate(browser)
    message_create_page.enter_data_message_schema('заголовок', 'сообщение', '79101234567', 'push')
    message_create_page = ActionMessageCreateStatus(browser)
    message_create_page.open_data_messages()
    data_messages_page = CheckDataMessages(browser)
    check = data_messages_page.check_message_status()
    assert 'Доставлено' in check, browser.get_screenshot_as_file(test_send_push_page_data_messages.__name__ + ' ' + 'FAILED.png')
