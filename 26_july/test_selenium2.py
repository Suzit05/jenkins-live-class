from selenium import webdriver
#webdriver-- webtool ko automate krne k liye

driver=webdriver.Chrome()
#driver k through chrome ko control kr rhe


def test_fb():
    driver.get("https://www.facebook.com")
    title= driver.title
    title_expected= "Facebook – log in or sign up"
    print(title)

    try:
        assert title== title_expected
        print("titles matched")

    except AssertionError:
        print("titles do not match")

    finally:
        driver.quit()

if __name__ == "__main__":
        test_fb()
        #Is block ka matlab hai ki agar ye file directly run ki ja rahi hai 
        #(na ki kisi aur script se import ki ja rahi hai),
        # toh test_fb() function ko call karo.
