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

# 读取agent
with open('User_Agent', 'r') as f:
    user_agents = f.read().split('\n')


ip_port = []
for i in tqdm(range(30)):
    url = f'https://free.kuaidaili.com/free/inha/{i}/'  # 高匿名ip地址
    # url = f'https://free.kuaidaili.com/free/intr/{i}/'  # 透明ip
    try:
        user_agent = random.choice(user_agents)
        headers = {'User-Agent': user_agent}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request, timeout=2)
        html = response.read().decode('utf-8')
    except:
        print('失败')
        continue
    ips = []
    ports = []
    for line in html.split('\n'):
        if 'td data-title="IP"' in line:
            line = line.strip().split(r'<')[-2].split(r'>')[-1]
            ips.append(line)
        elif 'data-title="PORT"' in line:
            line = line.strip().split(r'<')[-2].split(r'>')[-1]
            ports.append(line)
    for i in range(len(ips)):
        ip_port.append(f'{ips[i]}:{ports[i]}')
    time.sleep(random.uniform(2, 4))
ip_port = list(set(ip_port))
with open('raw_proxys.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(ip_port))




