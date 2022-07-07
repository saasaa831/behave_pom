from selenium import webdriver
import os
import shutil
import time
import logging

def before_all(context):
     print("Executing before all")

def before_feature(context, feature):
     print("Before feature\n")
     # Create logger
     context.logger = logging.getLogger('tests')
     hdlr = logging.FileHandler('./tests.log')
     formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
     hdlr.setFormatter(formatter)
     context.logger.addHandler(hdlr)
     context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    print("User data:", context.config.userdata)
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.browser.maximize_window()
    print("Before scenario\n")

def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()

def after_feature(context, feature):
            print("\nAfter Feature")

def after_all(context):
    print("User data:", context.config.userdata)
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
    time.strftime("%d_%m_%Y"),
    'zip',
     "failed_scenarios_screenshots")
            print("Executing after all")


