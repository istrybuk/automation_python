from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://automationpractice.com/index.php"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # button = browser.find_element(By.XPATH, "//*[@id='header']/div[2]/div/div/nav/div[1]/a")
    # button.click()
    # input1 = browser.find_element(By.XPATH, "//*[@id='email_create']")
    # input1.send_keys("zavan@mail.ru")
    # button = browser.find_element(By.XPATH, "// *[ @ id ='SubmitCreate']")
    # button.submit()
    # button = browser.find_element(By.XPATH, "//input[@id='id_gender2']")
    # button.click()

    time.sleep(12)

    browser.save_screenshot('result1.png')  # Сохраняем скриншот нашего результата
finally:
    browser.quit()
