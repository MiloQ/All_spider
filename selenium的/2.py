from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
browser.get('https://www.taobao.com')#打开淘宝
input = browser.find_element_by_id('q') #选择搜索输入框
input.send_keys('iPhone')#在搜索框内输入文字
time.sleep(1)
input.clear()#清空搜索框
button = browser.find_element_by_class_name('btn-search')
button.click()
browser.close()


