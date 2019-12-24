from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get('https://www.bilibili.com/')
input = browser.find_element_by_class_name('search-keyword')
submit = browser.find_element_by_class_name('search-button')

input.send_keys('蔡徐坤 篮球')
submit.click()