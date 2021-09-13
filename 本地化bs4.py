# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:28:54 2021

@author: zhou jian
"""


from bs4 import BeautifulSoup
if __name__ == "__main__":
    #将本地的html文档中的数据加载到该对象中
    fp = open('./test.html','r', encoding = 'utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    print(soup)
    #print(soup.a) #soup.tagName返回的是html中第一次出现的标签
    #print(soup.div)
    #print(soup.find('div')) #跟print(soup.div)相同
    #print(soup.find('div',class_='logo')) #class要带下划线
    #print(soup.find_all('a')) #查找所有的a标签（返回是列表）
    #print(soup.select('.logo'))
    #print(soup.select('.logo > ul > li > a')[0]) # > 表示一个层级
    #print(soup.select('.logo > ul a')[0].text) #空格表示多个层级
    
    