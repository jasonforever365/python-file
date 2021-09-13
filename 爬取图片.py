# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 21:02:36 2021

@author: zhou jian
"""

import requests
if __name__ == "__main__":
    #如何爬取图片数据
    url = 'https://n.sinaimg.cn/fashion/crawl/141/w550h391/20201203/3884-ketnnaq5900509.png'
    #content返回的是二进制形式的图片数据
    #text(字符串) content(二进制) json(对象)
    img_data = requests.get(url=url).content
    with open('./fashionphoto.jpg','wb') as fp:
        fp.write(img_data)