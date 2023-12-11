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
keyElement.send_keys('tomato green')
keyElement.send_keys(Keys.RETURN)

bodyElement = driver.find_element(By.TAG_NAME, 'body')
time.sleep(3)
for i in range(50):
    bodyElement.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

# //*[@id="islrg"]/div[1]/div[1]/a[1]
# //*[@id="islrg"]/div[1]/div[2]/a[1]
# //*[@id="islrg"]/div[1]/div[3]/a[1]

images = driver.find_elements(By.XPATH, '//*[@id="islrg"]/div[1]/div/a[1]')
# print(len(images))

imageSeq = 1
for image in images:
    image.click()
    time.sleep(0.5)

    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img
    # //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img

    highImages = driver.find_elements(By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img')
    # print(len(highImages))
    # print(highImages[0].get_attribute('src'))
    realImage = highImages[0].get_attribute('src')

    try:
        urllib.request.urlretrieve(realImage, 'C:/Python_Lang/gtoma/g' + str(imageSeq) + '.jpg')
        imageSeq += 1
    except:
        pass