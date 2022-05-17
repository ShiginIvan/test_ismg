from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    message_status = (By.XPATH, '/ html / body / div / div[2]')
    messages_menu = (By.CSS_SELECTOR, '#messagesMenuLink')
    messages_menu_messages = (By.CSS_SELECTOR, '#navbarNavDropdown > ul.navbar-nav.me-auto > li:nth-child(1) > ul > li:nth-child(1) > a')


class CheckMessageCreateStatus(BasePage):
    def check_message_status(self):
        search_message_status = self.find_element(SearchLocators.message_status)
        return search_message_status.text


class ActionMessageCreateStatus(BasePage):
    def open_data_messages(self):
        search_field = self.find_element(SearchLocators.messages_menu)
        search_field.click()
        search_field = self.find_element(SearchLocators.messages_menu_messages)
        search_field.click()



