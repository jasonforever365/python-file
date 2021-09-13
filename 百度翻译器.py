# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 08:20:31 2020

@author: zhou jian
"""

import requests
import json
if __name__ == "__main__":
    #指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    #post请求参数处理(同get请求一致)
    word = input('enter a word')
    data = {
        'kw': word
    }
    #进行请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    #获取相应数据:json()方法返回的是一个obj （如果确认响应服务器是json类型的，才能使用json）
    dic_obj = response.json()
    print (dic_obj)
    #进行持久化存储
    filename = word +'.json'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    
    print('over!!!')
    
    
