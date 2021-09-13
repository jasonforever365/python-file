# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:49:16 2020

@author: zhou jian
"""

import requests
if __name__ == "__main__":
    #制定URL
    url = "https://www.sogou.com/"
    #发起请求
    response = requests.get(url=url)
    #获取响应数据,返回字符串的响应数据
    page_text = response.text
    print(page_text)
    #持久化存储
    with open("./sougou.text", "w", encoding="utf-8") as fp:
        fp.write(page_text)
    print("读取数据结束")



