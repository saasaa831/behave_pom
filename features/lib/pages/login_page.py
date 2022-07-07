from selenium.webdriver.common.by import By
from features.lib.pages.base_page_object import BasePage

class LoginPage(BasePage):
    locator_dictionary = {
        "email": (By.ID, 'login_field'),
        "password": (By.ID, 'password'),
        "signin_button": (By.NAME, 'commit'),
        "signgithub_button":(By.LINK_TEXT, 'Sign in with github'),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://todo-list-login.firebaseapp.com/')

    def login(self,username="abc@xyz.com",passwd="Test@123"):
        self.find_element(*self.locator_dictionary['email']).send_keys(username)
        self.find_element(*self.locator_dictionary['password']).send_keys(passwd)
        self.find_element(*self.locator_dictionary['signin_button']).click()

    def signingit(self):
        self.find_element(*self.locator_dictionary['signgithub_button']).click()
