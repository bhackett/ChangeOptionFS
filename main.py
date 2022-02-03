# Change to Options Menu in FamilySearch Tree

from selenium import webdriver
from selenium.webdriver.common.by import By

BRIAN = 'https://www.familysearch.org/tree/pedigree/landscape/KW6J-MX4'
TRICIA = 'https://www.familysearch.org/tree/pedigree/landscape/KW6J-MXC'

driver = webdriver.Chrome()  # Retrieve chrome
driver.get(BRIAN)
driver.maximize_window()
username = driver.find_element(By.ID, 'userName')
username.click()  # Put cursor in userName element
username.send_keys("bhackett")  # Enter username
password = driver.find_element(By.ID, 'password')
password.click()  # Put cursor in password element
password.send_keys("bkh368385")  # Enter password
driver.find_element(By.ID, 'privateComputerLabel').click()
driver.find_element(By.ID, 'login').click()

input("Done")
