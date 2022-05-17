from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    messages_message_status = (By.CSS_SELECTOR, '#messages > tbody > tr:nth-child(1) > td:nth-child(6) > a')


class CheckDataMessages(BasePage):
    def check_message_status(self):
        search_message_status = self.find_element(SearchLocators.messages_message_status)
        return search_message_status.text
