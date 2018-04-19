"""
	login for the app will be tested by this module
"""
import unittest,os
from selenium import webdriver
from pages.logInPage import *
from common.providers.logInProviders import *
from common.config import *
from selenium.webdriver.support.wait import WebDriverWait
from tests.base import BaseTest
from tests import base


uiData = logInPageData()
data = logInData()
driver= base.setdriver(browser)

class LoginTests(BaseTest):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        cls.driver.get(mainUrl)
        buttonpress=None
        try:
            cls.driver.get(uiData['logInUrl'])
        except Exception as e:
            print e
            pass
        cls.wait = WebDriverWait(cls.driver, 30)
        cls.less_wait = WebDriverWait(cls.driver, 5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def test_001_verify_login_screen(self):
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])


    def test_002_input_login_data(self):
        self.beforeEachTestLogIn()
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        login = self.find_element_by_class_name(uiData['logInButton'])
        login.click()
        self.timeToLoadUrl()
        if uiData['logInRedirectUrl'] not in str(self.driver.current_url):
            self.assertFalse(data, 'test failed %s not in %s'%(uiData['logInRedirectUrl'],str(self.driver.current_url)))

    def test_003_input_spaced_email_login_data(self):
        alist = []
        self.beforeEachTestLogIn()
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])
        email = self.find_element_by_name('email')
        email.send_keys('')
        password = self.find_element_by_name('password')
        password.send_keys('')
        try:
            login = self.find_element_by_class_name(uiData['logInButton'])
            login.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_spaced_email_login_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your email.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

    def test_004_input_invalid_email_login_data(self):
        alist = []
        self.beforeEachTestLogIn()
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['invalidEmail'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        try:
            login = self.find_element_by_class_name(uiData['logInButton'])
            login.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_invalid_email_login_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter a valid email address.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

    def test_005_input_invalid_password_login_data(self):
        alist = []
        self.beforeEachTestLogIn()
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['invalidPassword'])
        login = self.find_element_by_class_name(uiData['logInButton'])
        login.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_invalid_password_login_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Email / password combination is not valid.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

    def test_006_input_empty_login_data(self):
        alist = []
        self.beforeEachTestLogIn()
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])
        email = self.find_element_by_name('email')
        email.send_keys()
        password = self.find_element_by_name('password')
        password.send_keys()
        try:
            login = self.find_element_by_class_name(uiData['logInButton'])
            login.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_empty_login_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your email.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

    def test_007_input_sql_injection_login_data(self):
        alist = []
        self.beforeEachTestLogIn()
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['sqlInjectionEmail'])
        password = self.find_element_by_name('password')
        password.send_keys(data['sqlInjectionPassword'])
        try:
            login = self.find_element_by_class_name(uiData['logInButton'])
            login.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_empty_login_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter a valid email address.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))

    def test_008_input_too_long_email_login_data(self):
        alist = []
        self.beforeEachTestLogIn()
        self.assertEqual(self.driver.current_url, uiData['logInUrl'])
        email = self.find_element_by_name('email')
        email.send_keys(data['longEmail'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        try:
            login = self.find_element_by_class_name(uiData['logInButton'])
            login.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error == None:
            self.assertFalse(alist, 'test_input_empty_login_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Email / password combination is not valid.' not in alist:
                self.assertFalse(alist, 'test failed %s' % (alist))


if __name__ == '__main__':
    unittest.main()