from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

# Browser data and browser automate open
driver = webdriver.Chrome()
driver.get("https://github.com/")

signin_link = driver.find_element(by=By.LINK_TEXT, value="Sign up")
signin_link.click()

signin_link = driver.find_element(by=By.LINK_TEXT, value="Sign in")
signin_link.click()

username = driver.find_element(by=id("login_field"))
username.send_keys("fideru")
password = driver.find_element(by=id("password"))
password.send_keys("z3r0xExE")

driver.quit()