# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 21:04:05 2020

@author: zhou jian
"""


import requests
if __name__ == "__main__":
    #UA伪装：将对应的USER-AGENT封窗到字典里
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = "https://www.sogou.com/web"
    #处理url处理的参数：封装到字典中
    kw = input("enter a word:")
    param = {
        "query":kw
    }
    #对指定的URL发起的请求是携带参数的，并且在请求过程中处理了参数
    response = requests.get(url = url, params=param, headers = headers)
    page_text = response.text
    file_name = kw+'.html'
    with open(file_name, 'w', encoding ='utf-8') as fp:
        fp.write(page_text)
    print(file_name, '保存成功')
    
    