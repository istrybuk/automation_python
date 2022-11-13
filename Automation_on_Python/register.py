import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://34.141.58.52:8080/#/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "login")
    input1.send_keys("zavan@mail.ru")
    time.sleep(5)
    input2 = browser.find_element(By.CSS_SELECTOR, "#password > input")
    input2.send_keys("1234")
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, "p-button-label")
    button.submit()
    time.sleep(10)

    response = requests.get('http://34.141.58.52:8080/#/profile')

    r = response.status_code
    assert response.status_code == 200

    browser.save_screenshot('result.png')

finally:

    browser.quit()
