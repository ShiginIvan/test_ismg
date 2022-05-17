from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost:8990/"

    def find_element(self, locator, time=1):
        try:
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),f"Can't find element by locator {locator}")
        except TimeoutException:
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),f"Can't find element by locator {locator}" and self.driver.get_screenshot_as_file(str(locator) + ' ' + 'NOT FOUND.png'))

    def go_to_site(self):
        return self.driver.get(self.base_url)
