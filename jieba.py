# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:01:00 2021

@author: zhou jian
"""

from sklearn.feature_extraction.text import CountVectorizer
import jieba

data = jieba.cut('网易是一家中国大陆互联网科技公司。目前提供网络游戏、门户网站、移动新闻客户端、移动财经客户端、电子邮件、电子商务、搜索引擎、博客、相册、社交平台、互联网教育等服务。截至2020年1月16日，网易公司的市值为442亿美元[1]，其收入中大约79%来自于在线游戏服务（2019年第三季度）')
#方法一
#for temp in data:
    #print(temp)
#方法二
data = ' '.join(data)
print(data)

vector = CountVectorizer()
res = vector.fit_transform([data])
print(vector.get_feature_names())
print(res.toarray())

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
#特征用One-hot编码表示
enc.fit([['男','中国','足球'], 
         ['女','美国','篮球'], 
         ['男','日本','羽毛球'], 
         ['女','中国','乒乓球']])

array = enc.transform([['男','美国','乒乓球']]).toarray()
print(array)
print(enc.inverse_transform(array))