# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 07:23:43 2021

@author: zhou jian
"""


import requests

if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    kw = input('输入需要查询的城市')
    param = {
        'cname':'', 
        'pid':'', 
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
    }
    reponse = requests.post(url =url, params =param, headers=headers)
    page_text = reponse.text
    filename = kw +'.text'
    with open(filename, 'w', encoding ='utf-8') as fp:
        fp.write(page_text)
    print(filename, "搜索成功")