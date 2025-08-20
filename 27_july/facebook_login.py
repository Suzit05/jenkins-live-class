from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.facebook.com")
search_box1=driver.find_element("name", "email")
search_box1.send_keys("rajaji08")
search_box2=driver.find_element("name", "pass")
search_box2.send_keys("123456")
login=driver.find_element("name","login")
login.submit()

driver.implicitly_wait(1000)
print("page title:",driver.title )

driver.quit()