from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchLocators:
    createmessage_title = (By.CSS_SELECTOR, '#title')
    createmessage_body = (By.CSS_SELECTOR, '#message')
    createmessage_address = (By.CSS_SELECTOR, '#addressList')
    createmessage_button_create = (By.CSS_SELECTOR, '#btnSubmit')
    createmessage_schema = (By.CSS_SELECTOR, '#schema')


class ActionMessageCreate(BasePage):
    def enter_data_message_default(self, title, message, address):
        search_field = self.find_element(SearchLocators.createmessage_title)
        search_field.send_keys(title)
        search_field = self.find_element(SearchLocators.createmessage_body)
        search_field.send_keys(message)
        search_field = self.find_element(SearchLocators.createmessage_address)
        search_field.send_keys(address)
        search_field = self.find_element(SearchLocators.createmessage_button_create)
        search_field.click()

    def enter_data_message_schema(self, title, message, address, schema):
        search_field = self.find_element(SearchLocators.createmessage_title)
        search_field.send_keys(title)
        search_field = self.find_element(SearchLocators.createmessage_body)
        search_field.send_keys(message)
        search_field = self.find_element(SearchLocators.createmessage_address)
        search_field.send_keys(address)
        search_field = self.find_element(SearchLocators.createmessage_schema)
        search_field.clear()
        search_field.send_keys(schema)
        search_field.send_keys(Keys.ENTER)
