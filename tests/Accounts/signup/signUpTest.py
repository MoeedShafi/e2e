"""
	signup for the app will be tested by this module
"""
import unittest,os
from selenium import webdriver
from pages.signUpPage import *
from common.providers.signUpProviders import *
from common.config import *
from selenium.webdriver.support.wait import WebDriverWait
from tests.base import BaseTest
from tests import base

uiData = signUpPageData()
data = signUpData()
driver= base.setdriver(browser)

class SignUpTests(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.driver = driver
        cls.driver.get(mainUrl)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.less_wait = WebDriverWait(cls.driver, 5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_001_verify_signup_screen(self):
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])

    def test_002_input_signup_empty_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys()
        email = self.find_element_by_name('email')
        email.send_keys()
        password = self.find_element_by_name('password')
        password.send_keys()
        try:
            signup=self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error==None:
            self.assertFalse(alist,'test failed test_input_signup_empty_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your full name.' not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))


    def test_003_input_empty_username_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys()
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        try:
            signup = self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_signup_without_username_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your full name.' not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))

    def test_004_input_spaced_username_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys('')
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        try:
            signup = self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_signup_spaced_username_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your full name.' not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))

    def test_005_input_empty_email_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys()
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        try:
            signup = self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_empty_email_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your email.' not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))

    def test_006_input_spaced_email_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys('')
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        try:
            signup = self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_spaced_email_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your email.' not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))

    def test_007_input_invalid_email_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys(data['invalidEmail'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        signup=self.find_element_by_css_selector(uiData['signUpButton2'])
        signup.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_invalid_email_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter a valid email address.' not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))



    def test_008_input_empty_password_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys()
        try:
            signup = self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_empty_password_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if 'Please enter your password.' not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))



    def test_009_input_spaced_password_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys('')
        try:
            signup = self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_spaced_password_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if "Please enter a valid password. Use at least 6 characters and don't use spaces." not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))



    def test_010_input_short_password_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['shortPassword'])
        signup=self.find_element_by_css_selector(uiData['signUpButton2'])
        signup.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_short_password_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if "Please enter a valid password. Use at least 6 characters and don't use spaces." not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))

    def test_011_input_long_password_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['longPassword'])
        signup=self.find_element_by_css_selector(uiData['signUpButton2'])
        signup.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertFalse(alist, 'test_input_long_password_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if "Please enter a valid password. Use at least 6 characters and don't use spaces." not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))

    def test_012_input_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        signup = self.find_element_by_css_selector(uiData['signUpButton2'])
        signup.click()
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error = None
        if error:
            self.assertFalse(self.find_elements_by_class_name(uiData['errors']), 'test_input_signup_data %s'%(error))

    def test_013_input_same_email_signup_data(self):
        alist = []
        self.beforeEachTestSignUp()
        self.assertEqual(self.driver.current_url, uiData['signUpUrl'])
        username = self.find_element_by_name('fullname')
        username.send_keys(data['username'])
        email = self.find_element_by_name('email')
        email.send_keys(data['email'])
        password = self.find_element_by_name('password')
        password.send_keys(data['password'])
        try:
            signup = self.find_element_by_css_selector(uiData['signUpButton2'])
            signup.click()
        except:
            pass
        try:
            error = self.find_elements_by_class_name(uiData['errors'])
        except:
            error=None
        if error == None:
            self.assertEqual(self.driver.current_url, uiData['signUpUrl'], 'test_input_same_email_signup_data')
        elif error:
            for i in error:
                alist.append(i.text)
            if "Email address already in use." not in alist:
                self.assertFalse(alist, 'test failed %s'%(alist))


if __name__ == '__main__':

    unittest.main()