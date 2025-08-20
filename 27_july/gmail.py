from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://mail.google.com")


email_box=driver.find_element("name","identifier")
email_box.send_keys("ravi@gmail.com")
wait = WebDriverWait(driver, 10)
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Next']]")))
next_button.click()



print("page title:",driver.title)


driver.quit()