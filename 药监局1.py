# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:26:36 2021

@author: zhou jian
"""


import requests
if __name__ == "__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'      
    }
    page_text = requests.get(url=url, headers=headers).text
    with open('./cosmotic.html','w', encoding='utf-8') as fp:
        fp.write(page_text)
        
    