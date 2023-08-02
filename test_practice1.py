# config interpreter
# pip install selenium
# pip install pytest - for test run
# pip install pytest-html - to generate report
# pip install pytest-xdist - to run parallel
# pip install allure-pytest - to generate allure report
# Select pytest as default runner in python (Go to setting --> Tools-->integrated Tools
# # -----------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test_Practice_01:

    # @pytest.mark.xfail
    def test_summation(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a and b is :" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False


    def test_Login_phptravels(self):
        d = webdriver.Chrome()
        d.maximize_window()
        d.implicitly_wait(20)
        # Open site
        d.get("https://phptravels.net/admin")
        # time.sleep(2)
        # Enter credentials and log in
        d.find_element(By.XPATH, "//input[@id='email']").send_keys("admin@phptravels.com")
        d.find_element(By.XPATH, "//input[@id='password']").send_keys("demoadmin")
        d.find_element(By.XPATH, "//button[@id='submit']").click()
        # time.sleep(2)
        # From Dashboard - go to settings -> payment gateway
        d.find_element(By.XPATH, "//button[normalize-space()='Settings']").click()
        # time.sleep(2)
        d.find_element(By.XPATH, "/html[1]/body[1]/main[1]/header[1]/ul[1]/li[2]/div[1]/ul[1]/li[3]/a[1]").click()
        # time.sleep(2)
        # Go back to main page (both options are correct - use any 1)
        # d.find_element(By.XPATH, "//a[@title='Previous Page']").click()
        d.back()
        # time.sleep(2)
        # Go to last option 'Super Admin' and click on logout
        d.find_element(By.XPATH, "//a[@id='dropdownUser1']").click()
        # time.sleep(2)
        d.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        # time.sleep(2)
        # If successfully logout, check for any text which is on login page to confirm we are back
        try:
            d.find_element(By.XPATH, "//strong[normalize-space()='Administrators Login']")
            print("\nSuccessfully logged out.")
            d.close()
            assert True
        except NoSuchElementException:
            print("\nLogout failed.")
            d.close()
            assert False
