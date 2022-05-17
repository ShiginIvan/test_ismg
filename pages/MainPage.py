from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By

class SearchLocators:
    title_main_page = (By.CSS_SELECTOR, 'body > div > h2')
    messages_menu = (By.CSS_SELECTOR, '#messagesMenuLink')
    messages_menu_create_message = (By.CSS_SELECTOR,'#navbarNavDropdown > ul.navbar-nav.me-auto > li:nth-child(1) > ul > li:nth-child(7) > a')


class Check_Main(BasePage):
    def check_title(self):
        search_title = self.find_element(SearchLocators.title_main_page)
        return search_title.text

class Action_Main(BasePage):
    def open_create_message(self):
        search_field = self.find_element(SearchLocators.messages_menu)
        search_field.click()
        search_field = self.find_element(SearchLocators.messages_menu_create_message)
        search_field.click()

