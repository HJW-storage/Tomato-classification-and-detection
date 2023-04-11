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
keyElement.send_keys('green tomato')
keyElement.send_keys(Keys.RETURN)

# url = driver.find_element(By.CSS_SELECTOR, '#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img').get_attribute('src')
# print(url)
# urllib.request.urlretrieve(url, 'C:/Python_Lang/crawled_img/WorldCup.jpg')

bodyElement = driver.find_element(By.TAG_NAME, 'body')
time.sleep(3)
for i in range(50):
    bodyElement.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
#islrg > div.islrc > div:nth-child(3) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
#islrg > div.islrc > div:nth-child(4) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img

#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
#islrg > div.islrc > div:nth-child(3) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
#islrg > div.islrc > div:nth-child(4) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
images = driver.find_elements(By.CSS_SELECTOR, '#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')
print(len(images))

imageURL = []
for image in images:
    if image.get_attribute('src') is not None:
        imageURL.append(image.get_attribute('src'))

# print(imageURL)
for seq, urlImg in enumerate(imageURL):
    urllib.request.urlretrieve(urlImg, 'C:/Python_Lang/gcolor_tomato/' + "gtomato" + str(seq) + '.jpg')
