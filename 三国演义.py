# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:14:47 2021

@author: zhou jian
"""
import requests
from bs4 import BeautifulSoup
#爬取三国演义所有的章节和标签
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    #需要在首页中解析章节的标题和详情页的URL
    #实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        #解析到章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！！！')
        
            
    
        
