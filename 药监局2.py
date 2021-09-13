# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:26:54 2021

@author: zhou jian
"""


import requests
import json
if __name__ == "__main__":
    #批量获取不同企业的ID
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'      
    }
    id_list = [] #存储企业的id
    all_data_list = [] #存储所有企业的资料
    
    for page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,    
            'pageSize': '15',
            'productName':'', 
            'conditionType': '1',
            'applyname':'', 
            'applysn': '',
        }
        json_ids = requests.post(url=url, headers=headers,data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        #print(id_list)
        #获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
                'id': id
            }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        #print(detail_json,'------end')
        all_data_list.append(detail_json)
    #持久化存储
    fp = open('./alldata.json','w',encoding='utf-8')
    json.dump(all_data_list, fp=fp,ensure_ascii=False)
    print("over")
    