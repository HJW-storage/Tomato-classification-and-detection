# image Selector = #islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# serarch XPATH = /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import urllib.request

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)
keyElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
keyElement.send_keys('월드컵')
keyElement.send_keys(Keys.RETURN)

url = driver.find_element(By.CSS_SELECTOR, '#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img').get_attribute('src')
print(url)
urllib.request.urlretrieve(url, 'C:/Python_Lang/crawled_img/WorldCup.jpg')
