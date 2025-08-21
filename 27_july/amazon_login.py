from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.amazon.in")



signIn = driver.find_element(By.CSS_SELECTOR, ".nav-line-1-container ")
signIn.click()

email=driver.find_element("name","email")
email.send_keys("your number")
email.submit()

password=driver.find_element("name","password")
password.send_keys("yourpassword")
password.submit()

time.sleep(10)
driver.quit()