from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from features.lib.pages.base_page_object import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback

class TodoListPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://todo-list-login.firebaseapp.com/')

    locator_dictionary = {
        "add_lists":(By.XPATH, "//button[@ng-click='home.list && home.add()']"),
        "home_lists":(By.XPATH, "//input[@ng-model='home.list']"),
        "del_lists":(By.XPATH, '//button[@ng-click="home.delete($index)"]'),
        "titlepage":(By.XPATH, "//div[@class='brownhill '][contains(.,'Todo Lists')]"),
        "sign_out": (By.XPATH, "//button[@ng-click='home.signOut()']"),
        "group_lists":(By.XPATH, "(//a[@class='ng-binding'])[1]"),
        "glists":(By.XPATH, "//a[contains(.,'file Iras submission List')]"),
        "grouplists":(By.XPATH, "//ul[@class='list-group']/li//div/a"),
        "delbuttons": (By.XPATH, "//ul[@class='list-group']/li//div/button")
    }

    def getlist_todo(self, what, datx, intx=None):

        if what in self.locator_dictionary.keys():
            try:
                element = WebDriverWait(self.browser, 30).until(
                    EC.visibility_of_element_located(self.locator_dictionary[what])
                )
                print(element)
            except(TimeoutException, StaleElementReferenceException):
                traceback.print_exc()

        if intx == 'NA': return self.find_element(By.XPATH, "//a[contains(.,'" + datx + "')]")
        else:
            return self.find_element(By.XPATH, "//a[contains(.,'" + datx + "')]//following::button[1]")
