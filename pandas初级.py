# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:19:41 2021

@author: zhou jian
"""


import pandas as pd
food_info = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\SCF liandong 2018 till 2021017.xlsx')
#print(type(food_info))
#print(food_info.dtypes)
#print(help(pd.read_csv))
#pandas的核心是DataFrame

#print(food_info.loc[0])
#loc指的是行
#print(food_info.loc[3])    
ndb_col = food_info[['期限', '币种']] 
#print(ndb_col) 

col_names =food_info.columns.tolist()
#把当前列名做成list
#print(col_names)
#gram_columns = []
#for c in col_names:
    #if c.endswith('入'):
        #gram_columns.append(c)
#print(gram_columns)
#gram_df = food_info[gram_columns]
#print(gram_df)

max_categories = food_info['利息收入'].max()
#print(max_categories)

food_info.sort_values('利息收入',inplace=True)
#print(food_info['利息收入'])  
#sort_value: 从小到大, 默认ascending=True

food_info.sort_values('利息收入',inplace=True, ascending=False)
#print(food_info['利息收入']) 

committment = food_info['承诺']
#print(committment.loc[78:88])
committment_is_null = pd.isnull(committment)
#print(committment_is_null)
committment_null_true = committment[committment_is_null]
#print(committment_null_true)
committment_count = len(committment_null_true)
#print(committment_count)

fee_is_null = pd.isnull(food_info['费用'])
good_fee = food_info['费用'][fee_is_null == False]
mean_fee = sum(good_fee)/len(food_info['费用'])
print(mean_fee)

mean_fee = food_info['费用'].mean()
print(mean_fee)









     
                