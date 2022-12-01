# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     deal_later
   Description :
   Author :       asdil
   date：          2022/10/9
-------------------------------------------------
   Change Activity:
                   2022/10/9:
-------------------------------------------------
"""
__author__ = 'Asdil'
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from tqdm import tqdm
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

for i in tqdm(range(1, 21343)):
    try:
        herf = f'https://www.mala.cn/plugin.php?id=threadcheck:shaixuan&type=%B9%E3%B8%E6-%C9%CC%D2%B5%CD%C6%B9%E3&page={i}'  # 21343
        # herf = f'https://www.mala.cn/plugin.php?id=threadcheck:shaixuan&type=%B9%E3%B8%E6-%B9%E3%B8%E6%C6%E4%CB%FB&page={i}' # 1399
        # herf = f'https://www.mala.cn/plugin.php?id=threadcheck:shaixuan&type=%B9%E3%B8%E6-%B7%BF%B2%FA%B9%E3%B8%E6&page={i}' # 158
        browser.get(herf)
        data = browser.page_source
        with open(f'/home/asdil/Documents/python/code/sisitiezi/pages11/{i}.html', 'w', encoding='utf-8') as f:
            f.write(data)
    except:
        print(f'{i}')
    time.sleep(1)
browser.close()
browser.quit()
