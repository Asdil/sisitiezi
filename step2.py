# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     step1
   Description :  测试代理ip
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

# 读取配置
db = Sqlit3()
last_date = db.select_one('select the_date from work order by id desc limit 1;')[0]
sql = "select id, title, address, total, done from work where the_date=? ;"
data = db.select_all(sql, (last_date, ))

# 读取agent
with open('User_Agent', 'r') as f:
    user_agents = f.read().split('\n')

# 读取代理服务器
# 测试网站
with open('raw_proxys.txt', 'r', encoding='utf-8') as f:
    proxys = f.read().split('\n')


def test_proxys(url, proxy):
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}
    proxy_values = "%(ip)s" % {'ip': proxy}
    proxies = {"http": proxy_values, "https": proxy_values}
    handler = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request(url, headers=headers)
    response = opener.open(request, timeout=4)
    html = response.read()
    response.close()


avaliable_proxys = []
for proxy in tqdm(proxys):
    print(proxy)
    try:
        _, _, url, _, _ = random.choice(data)
        test_proxys(url, proxy)
        avaliable_proxys.append(proxy)
    except:
        pass
    time.sleep(random.uniform(0.5, 1))

with open('proxys.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(avaliable_proxys))