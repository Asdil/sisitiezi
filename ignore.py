# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ignore
   Description :
   Author :       asdil
   date：          2022/10/11
-------------------------------------------------
   Change Activity:
                   2022/10/11:
-------------------------------------------------
"""
__author__ = 'Asdil'
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from tqdm import tqdm
import pandas as pd
#设置chromedriver

browser = webdriver.Chrome('/home/asdil/Documents/python/code/sisitiezi/chromedriver')

#设置超时时间

browser.set_page_load_timeout(30)
browser.get("https://www.mala.cn/member.php?mod=logging&action=login")
time.sleep(1)

browser.find_element(by=By.NAME, value="username").send_keys('值班编辑6')
time.sleep(1)
browser.find_element(by=By.NAME, value="password").send_keys('yy520025')
time.sleep(1)
browser.find_element(by=By.CLASS_NAME, value="postbtn").click() #登录
time.sleep(20)
#打开网页
data = pd.read_excel('/home/asdil/Documents/python/code/sisitiezi/result/你好您&你好谢谢你.xlsx')
urls = data['忽略链接'].tolist()


for url in tqdm(urls):
    url = url.replace('amp;', '')
    url = 'https://www.mala.cn' + url
    browser.get(url)
    time.sleep(1)
browser.close()
browser.quit()
