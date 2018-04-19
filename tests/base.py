"""
	signup for the app will be tested by this module
"""
import unittest,os
from selenium import webdriver
from pages.signUpPage import *
from pages.logInPage import *
from pages.forgotPasswordPage import *
from common.providers.signUpProviders import *
from common.config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

uiDataSignUp = signUpPageData()
uiDataLogIn = logInPageData()
uiDataForgotPassword = forgotPasswordPageData()


def setdriver(browser):
    if browser == 'chrome':
        os.environ["webdriver.chrome.driver"] = chromeDriverPath
        driver = webdriver.Chrome(chromeDriverPath)
        return driver
    elif browser == 'firefox':
        os.environ["webdriver.firefox.driver"] = firefoxDriverPath
        driver = webdriver.Firefox(executable_path=firefoxDriverPath)
        return driver

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.environ["webdriver.chrome.driver"] = chromeDriverPath
        cls.driver = webdriver.Chrome(chromeDriverPath)
        cls.driver.get(mainUrl)
        cls.wait = WebDriverWait(cls.driver, 30)
        cls.less_wait = WebDriverWait(cls.driver, 5)

    def find_element_by_css_selector(self, button):
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, button)))
        return self.driver.find_element_by_css_selector(button)

    def find_element_by_class_name(self, classname):
        return self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, classname)))

    def find_elements_by_class_name(self, classname):
        self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, classname)))
        return self.driver.find_elements_by_class_name(classname)

    def find_element_by_name(self, name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.NAME, name)))
        return self.driver.find_element_by_name(name)

    def beforeEachTestSignUp(self):
        self.driver.get(uiDataSignUp['logOutUrl'])
        self.driver.get(uiDataSignUp['signUpUrl'])

    def beforeEachTestLogIn(self):
        self.driver.get(uiDataLogIn['logOutUrl'])
        self.driver.get(uiDataLogIn['logInUrl'])

    def beforeEachTestForgotPassword(self):
        self.driver.get(uiDataLogIn['logOutUrl'])
        self.driver.get(uiDataForgotPassword['forgotPasswordUrl'])

    def timeToLoadUrl(self):
        sleep(30)




