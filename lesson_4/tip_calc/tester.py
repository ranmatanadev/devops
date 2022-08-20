from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# For not close
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

my_driver = webdriver.Chrome(
    options=options, service=Service('/Applications/chromedriver'))
# My index.html
my_driver.get(
    "file:/Users/ranmatana/repositories/devops/lesson_4/tip_calc/index.html")
# get elements
# my_driver.find_element(By.ID, "billamt").send_keys("100")
