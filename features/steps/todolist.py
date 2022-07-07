from behave import *
from features.lib.pages import *
import time
use_step_matcher("re")

appPage = 'https://todo-list-login.firebaseapp.com/'
add_todo_list = ['Read and write work emails', 'call Johnny karky', 'draft a new homepage', 'daily standup meet',
                     'attend bug triage', 'file Iras submission', 'draft new sales document', 'pay monthly bills',
                     'clear the bins', 'workout']


@when("I open todolist app")
def step_impl(context):
    page = LoginPage(context)
    page.visit(appPage)
    page.signgithub_button.click()
    page.switch_window()

@step('I login with username "([^"]*)" and password "([^"]*)"')
def step_impl(context,username,password):
    page = LoginPage(context)
    page.email.send_keys(username)
    page.password.send_keys(password)
    page.signin_button.click()
    page.switch_window()
    assert "Todo Lists" in TodoListPage(context).titlepage.text
    #page.login(username=username,passwd=password)

@step("I create 10 to do list with random strings")
def step_impl(context):
    page = TodoListPage(context)
    for xList in add_todo_list:
        page.home_lists.send_keys(xList)
        page.add_lists.click()

@step("I delete those 10 to-do list with random strings")
def step_impl(context):
    page = TodoListPage(context)
    for x in range(0, 9):
        page.del_lists.click()

@step("I verify that I successfully logged in by logging out")
def step_impl(context):
    TodoListPage(context).sign_out.click()

@step("I hover to sign in with github and click")
def step_impl(context):
    LoginPage(context).signgithub_button.click()

@step("I listed created to-do lists")
def step_impl(context):pass

@step("I try delete the list from 5 - 10")
def step_impl(context):
    page = TodoListPage(context)
    for listx in range(0, len(add_todo_list)):
        try:
           if listx > 3:
                getlistxx = page.getlist_todo(page.delbuttons, add_todo_list[listx])
                getlistxx.click()
                time.sleep(1)
        except Exception as e:
            print(str(e))
