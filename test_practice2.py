import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_CredKart_02:

    def test_Credkart_login(self):
        d = webdriver.Chrome()
        d.maximize_window()
        d.implicitly_wait(20)
        # Open the site and click on login
        d.get("https://automation.credence.in/shop")
        # time.sleep(1)
        d.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        # Enter login details and submit
        d.find_element(By.XPATH, "//input[@id='email']").send_keys("Cred12@abc.com")
        d.find_element(By.XPATH, "//input[@id='password']").send_keys("Cred12@abc")
        # time.sleep(1)
        d.find_element(By.XPATH, "//button[@type='submit']").click()
        # After login, find 'CredKart' in page, if found >ok, if not >fail
        try:
            d.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login passed.")
            d.close()
            assert True
        except NoSuchElementException:
            print("Login failed.")
            d.close()
            assert False


    def test_Crekart_checkout(self):
        d = webdriver.Chrome()
        d.maximize_window()
        d.implicitly_wait(20)
        # Open the site
        d.get("https://automation.credence.in/")
        # time.sleep(1)
        # Login the site
        d.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        d.find_element(By.XPATH, "//input[@id='email']").send_keys("Cred12@abc.com")
        d.find_element(By.XPATH, "//input[@id='password']").send_keys("Cred12@abc")
        d.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(1)
        # Click on product1 - (playstation4) & add to cart
        d.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[2]/h3[1]").click()
        d.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        # time.sleep(1)
        # Click on proceed to checkout
        d.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[2]").click()
        # Enter Shipping address
        d.find_element(By.ID, "first_name").send_keys("kunal")
        d.find_element(By.ID, "last_name").send_keys("shukla")
        d.find_element(By.ID, "phone").send_keys("9876543210")
        d.find_element(By.ID, "address").send_keys("Abc, gef, Xyz-(mno)")
        d.find_element(By.ID, "zip").send_keys("100100")
        # time.sleep(1)
        s1 = Select(d.find_element(By.XPATH,
                                   "/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/select[1]"))
        s1.select_by_index(2)
        # Enter Payment details
        # Name
        d.find_element(By.ID, "owner").send_keys("kunal")
        # CVV
        d.find_element(By.ID, "cvv").send_keys("000")
        # Card number
        d.find_element(By.ID, "cardNumber").send_keys("6732")
        d.find_element(By.ID, "cardNumber").send_keys("1785")
        d.find_element(By.ID, "cardNumber").send_keys("6743")
        d.find_element(By.ID, "cardNumber").send_keys("2345")
        # time.sleep(1)
        # Expiry Year
        s2 = Select(
            d.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/select[2]"))
        s2.select_by_index(3)
        # Expiry month
        s3 = Select(
            d.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/select[1]"))
        s3.select_by_index(7)
        # time.sleep(2)
        # Checkout
        d.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/button[1]").click()
        # Find 'thank you' message & print order no.
        try:
            d.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/h1[1]")
            # d.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/h1[2]")
            print("Successfully placed your order.")
            print("Order no.:", d.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/p[2]/a[1]").text)
            d.close()
            assert True
        except:
            print("Order not placed.")
            d.close()
            assert False
