from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchLocators:
    username = (By.CSS_SELECTOR, "#username")
    password = (By.CSS_SELECTOR, "#password")
    wrong_login_message = (By.CLASS_NAME, 'mb-3Q')

class Action_Login(BasePage):
    def enter_login_and_password(self, login, password):
        search_field = self.find_element(SearchLocators.username)
        search_field.send_keys(login)
        search_field = self.find_element(SearchLocators.password)
        search_field.send_keys(password)
        search_field.send_keys(Keys.ENTER)
    def autorization(self):
        search_field = self.find_element(SearchLocators.username)
        search_field.send_keys('admin')
        search_field = self.find_element(SearchLocators.password)
        search_field.send_keys('zj#KqU1')
        search_field.send_keys(Keys.ENTER)

class Check_Login(BasePage):
    def check_wrong_login_message(self):
        wrong_login_message = self.find_element(SearchLocators.wrong_login_message)
        return wrong_login_message.text
