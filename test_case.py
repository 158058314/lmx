from time import sleep

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
sleep(10)
browser.quit()
