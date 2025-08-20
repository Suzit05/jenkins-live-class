from selenium import webdriver

#launch chrome
driver=webdriver.Chrome()

#open web page
driver.get("https:///www.google.com")

#find an elemnet by id
#by inspecting

search_box=driver.find_element("name", "q")
search_box.send_keys("Open ai Chatgpt")

search_box.submit()
driver.implicitly_wait(60)
print("Page title:", driver.title)

driver.quit()

