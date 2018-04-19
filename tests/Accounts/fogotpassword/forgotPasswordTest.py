"""
	forget password for the app will be tested by this module
"""
import unittest,os
from selenium import webdriver
from pages.forgotPasswordPage import *
from common.providers.forgotPasswordProviders import *
from common.config import *
from selenium.webdriver.support.wait import WebDriverWait
from tests.base import BaseTest
from tests import base

uiData = forgotPasswordPageData()
data = forgotPasswordData()
driver= base.setdriver(browser)

class ForgotPasswordTests(BaseTest):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        cls.driver.get(mainUrl)
        buttonpress=None
        try:
            cls.driver.get(uiData['forgotPasswordUrl'])
        except Exception as e:
            print e
            pass
        cls.wait = WebDriverWait(cls.driver, 30)
        cls.less_wait = WebDriverWait(cls.driver, 5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def test_001_verify_forgot_pasword_screen(self):
        self.assertEqual(self.driver.current_url, uiData['forgotPasswordUrl'])


    def test_002_input_forgot_pasword_data(self):
        self.beforeEachTestForgotPassword()
        self.assertEqual(self.driver.current_url, uiData['forgotPasswordUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        button = self.find_element_by_class_name(uiData['forgotPasswordButton'])
        button.click()
        self.timeToLoadUrl()
        if uiData['forgotPasswordRedirectUrl'] != str(self.driver.current_url):
            self.assertFalse(data, 'test failed %s not in %s'%(uiData['forgotPasswordRedirectUrl'],str(self.driver.current_url)))


    def test_003_forgot_password_link(self):
        self.beforeEachTestLogIn()
        link = self.find_element_by_class_name(uiData['forgotPasswordLink'])
        link.click()
        self.timeToLoadUrl()
        if uiData['forgotPasswordUrl'] != str(self.driver.current_url):
            self.assertFalse(data, 'test failed %s not in %s'%(uiData['forgotPasswordRedirectUrl'],str(self.driver.current_url)))



    def test_004_input_forgot_pasword_empty_data(self):
        alist=[]
        self.beforeEachTestForgotPassword()
        self.assertEqual(self.driver.current_url, uiData['forgotPasswordUrl'])
        email = self.find_element_by_name('email')
        email.send_keys()
        button = self.find_element_by_class_name(uiData['forgotPasswordButton'])
        button.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_forgot_pasword_empty_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your email.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

    def test_005_input_forgot_pasword_invalid_data(self):
        alist=[]
        self.beforeEachTestForgotPassword()
        self.assertEqual(self.driver.current_url, uiData['forgotPasswordUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['invalidEmail'])
        button = self.find_element_by_class_name(uiData['forgotPasswordButton'])
        button.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_forgot_pasword_empty_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter a valid email address.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

    def test_006_input_forgot_pasword_invalid_data(self):
        alist=[]
        self.beforeEachTestForgotPassword()
        self.assertEqual(self.driver.current_url, uiData['forgotPasswordUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['unRegisteredEmail'])
        button = self.find_element_by_class_name(uiData['forgotPasswordButton'])
        button.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_forgot_pasword_unregistered_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'User with this email address not found.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

if __name__ == '__main__':
    unittest.main()