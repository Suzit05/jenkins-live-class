#1.open amazon
#2. search for a product
#3. scroll the page slowly to load dynamic  content
#4.extract product names and prices(if available)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



#setup chrome driver
options=webdriver.ChromeOptions()
options.add_argument('--start-maximized') #maximized screen
driver=webdriver.Chrome(options=options)

driver.get("https://www.amazon.in")

search_box=driver.find_element("name", "field-keywords")
search_box.send_keys("Laptops")
search_box.send_keys(Keys.ENTER)


time.sleep(5)

#scroll
scroll_pause_time=2
last_height=driver.execute_script("return document.body.scrollHeight")

for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height=driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#extract product title and prices

products=driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']") 
#find_elements -> You need to use find_elements (note the plural) to get a list of all matching elements:

for product in products:
    try:
        title=product.find_element(By.TAG_NAME, "h2").text
        print("product title:", title)

        price=product.find_element(By.TAG_NAME, "span").text
        print("product price:", price) #price nikal lo--yha error h

    except Exception as e:
        print("Error extracting product info:", e)


driver.quit()

