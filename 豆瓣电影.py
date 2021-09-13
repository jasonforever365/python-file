# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:11:21 2020

@author: zhou jian
"""


import requests
import json
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0', #从豆瓣服务器的第几部电影取
        'limit': '1',  #一次取出的个数 
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url =url, params= param, headers = headers)
    list_data = response.json()
    fp = open('./douban.json', 'w', encoding = 'utf-8')
    json.dump(list_data, fp =fp, ensure_ascii =False)
    print('over!!!')