import urllib.request
import random
import time
from tqdm import tqdm
import urllib
from db_sqlit3 import Sqlit3

# 读取agent
with open('User_Agent', 'r') as f:
    user_agents = f.read().split('\n')

# 读取配置
db = Sqlit3()
last_date = db.select_one('select the_date from work order by id desc limit 1;')[0]
print(f'帖子版次是{last_date}')


def f(url):
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request, timeout=2)
    html = response.read()  # .decode('GBK') # GBK utf-8“
    response.close()
    time.sleep(random.uniform(1, 3))


sql = "select id, title, address, total, done from work where the_date=? ;"
data = db.select_all(sql, (last_date, ))

urls = []
url_id = {}
url_title = {}
flag = 0
for id, title, address, total, done in data:
    if total <= done:
        flag += 1
    print(title, total, done)

if flag == len(data):
    print('帖子刷完了')
else:
    for id, title, address, total, done in data:
        url_list = [address for i in range(total - done)]
        urls.extend(url_list)
        url_id[address] = id
        url_title[address] = title

    random.shuffle(urls)

    times = 7000
    quest = 0
    for url in tqdm(urls[:times]):
        try:
            f(url)
            id = url_id[url]
            sql = f'update work set done=done+1 where id = {id};'
            db.excute(sql)
        except:
            quest += 1
            print(f'出现问题{quest}次')
            print(f'{url_title[url]}')

print('运行结束')














