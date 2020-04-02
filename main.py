from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
import time
import os

print("Để chạy được tool: Phải đảm bảo đã tắt hết trình duyệt Chrome và đã đăng nhập Tinder")
while True:
    a = input("Bạn đã chắc chắn (y/n):")
    if a.lower() == 'y':
        break
    exit()
    

driver_path = f"{os.getcwd()}/chromedriver.exe"

user = os.getlogin()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

driver.get("https://tinder.com/")

body = driver.find_element_by_tag_name("body")

while True:
    body.send_keys(Keys.ARROW_RIGHT)
    driver.implicitly_wait(3)