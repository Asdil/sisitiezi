# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     step1
   Description :  爬取ip地址
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
import time
import random
import urllib.request
from tqdm import tqdm
from db_sqlit3 import Sqlit3
from collections import defaultdict

# 配置
times = 7000


# 读取agent
with open('User_Agent', 'r') as f:
    user_agents = f.read().split('\n')

# 读取代理服务器
with open('proxys.txt', 'r', encoding='utf-8') as f:
    proxys = f.read().split('\n')

# 读取配置
db = Sqlit3()
last_date = db.select_one('select the_date from work order by id desc limit 1;')[0]
print(f'帖子版次是{last_date}')


def get_data(url, proxy):
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}
    proxy_values = "%(ip)s" % {'ip': proxy}
    proxies = {"http": proxy_values, "https": proxy_values}
    handler = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(handler)

    request = urllib.request.Request(url, headers=headers)
    response = opener.open(request, timeout=2)
    html = response.read()  # .decode('GBK') # GBK utf-8“
    response.close()
    time.sleep(random.uniform(2, 3))


sql = "select id, title, address, total, done from work where the_date=? ;"
data = db.select_all(sql, (last_date, ))


# 输出待刷帖的标题，还有刷帖目标和已经刷帖数目
flag = 0
for id, title, address, total, done in data:
    if total <= done:
        flag += 1
    print(title, total, done)


# 开始刷帖
urls = []
url_id = {}
url_title = {}
if flag == len(data):
    print('帖子刷完了')
else:
    for id, title, address, total, done in data:
        url_list = [address for i in range(total - done)]
        urls.extend(url_list)
        url_id[address] = id
        url_title[address] = title
    random.shuffle(urls)
    quest = 0
    for url in tqdm(urls[:times]):
        proxy = random.choice(proxys)
        try:
            get_data(url, proxy)
            id = url_id[url]
            sql = f'update work set done=done+1 where id = {id};'
            db.excute(sql)
        except:
            quest += 1
            print(f'出现问题{quest}次')
            print(f'{url_title[url]} 代理地址:{proxy}')
print('运行结束')






