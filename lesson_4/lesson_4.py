from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# For not close
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')

driver = webdriver.Chrome(
    options=options, service=Service('/Applications/chromedriver'))


# get elements
# driver.find_element(By.ID, "billamt").send_keys("100")

# 1.
# driver.get("http://www.walla.co.il")
# driver.get("http://www.ynet.co.il")

# 2.
# try:
#     title = driver.title
#     driver.refresh()
#     name = driver.current_url
#     if title == name:
#         print("compare")
#     else:
#         print("not compare")
# except:
#     print("cannot get some properties")

# 3. NO
# for page in ('https://www.bing.com','https://www.facebook.com'):
#     driver.execute_script(f"window.open ('{page}')")
# driver.switch_to.window(driver.window_handles[1])

# 4.
# driver.get("https://translate.google.com/?sl=iw&tl=en&op=translate")
# driver.find_element(
#     By.CSS_SELECTOR, "textarea.er8xn").send_keys("רן מתנה")

# 5.
# driver.get("https://www.youtube.com/")
# selector = driver.find_element(By.CSS_SELECTOR, "input#search")
# selector.send_keys("Song")
# selector.send_keys(Keys.ENTER)

# 6.
# driver.get("https://translate.google.com/")
# header = driver.find_element(By.CLASS_NAME, "QFw9Te")
# # start from your target element, here for example, "header"
# all_children_by_css = header.find_elements(By.CSS_SELECTOR, "*")
# print(str(all_children_by_css))

# 7.
# driver.get("https://www.facebook.com/")
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("RAN")
# driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("123")
# driver.find_element(By.CSS_SELECTOR, "form").submit()

# 8.
# driver.get("https://www.google.com/")
# cookies = driver.get_cookies()
# print("cookies", cookies)
# driver.delete_all_cookies()

# 9.
# driver.get("https://github.com/")
# driver.find_element(
#     By.CSS_SELECTOR, "input.form-control.input-sm.header-search-input.jump-to-field.js-jump-to-field.js-site-search-focus").send_keys("Selenium")
# driver.find_element(By.CSS_SELECTOR, "form").submit()

# 10.
# chrome_options.add_argument("--disable-extensions")

