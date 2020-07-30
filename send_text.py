from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import sys

# pyinstaller --onefile --icon=icon.ico send_text.py

print("Để chạy được tool: Phải đảm bảo đã tắt hết trình duyệt Chrome và đã đăng nhập Tinder")
while True:
    a = input("Bạn đã chắc chắn (y/n):")
    if a.lower() == 'y':
        break
    exit()
    
message = input("Nhập lời nhắn:")

driver_path = f"{os.getcwd()}/chromedriver.exe"

user = os.getlogin()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

driver.get("https://tinder.com/")

time.sleep(6)

try:
    while True:
        time.sleep(2)
        match_button = driver.find_element_by_xpath("//button[@id='match-tab']")
        ActionChains(driver).move_to_element(match_button).click(match_button).perform()

        time.sleep(2)
        element = driver.find_element_by_xpath("//div[@class='D(f) Flw(w)']")
        result = element.find_elements_by_xpath("//div[@class='P(8px) Ta(c)']")[1]
        ActionChains(driver).move_to_element(result).click(result).perform()

        time.sleep(2)
        text_area = driver.find_element_by_xpath("//textarea[@id='chat-text-area']")
        text_area.send_keys(message)
        text_area.send_keys(Keys.ENTER)
except:
    sys.exit()
