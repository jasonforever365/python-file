# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:08:59 2021

@author: zhou jian
"""


import pandas as pd
import numpy as np
financement_trade = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\SCF liandong 2018 till 2021017.xlsx')
currency_classes = ['USD', 'CNY','EUR']
margin_by_currency = {}
for this_currency in currency_classes:
    TF_rows = financement_trade[financement_trade['币种'] == this_currency]
    TF_margins = TF_rows['资金部平均成本']
    margin_in_currency = TF_margins.mean()
    margin_by_currency[this_currency] = margin_in_currency
#print(margin_by_currency)


margin_by_currency = financement_trade.pivot_table(index='币种', values='资金部平均成本',aggfunc=np.mean)
#print(margin_by_currency)

margin_by_currency = financement_trade.pivot_table(index='币种', values=['资金部平均成本','TAUX AP'],aggfunc=np.mean)
#print(margin_by_currency)

drop_na_columns = financement_trade.dropna(axis=1)
#specify axis=1 or axis='columns' will drop any columns that have null values
new_financement_trade = financement_trade.dropna(axis=0,subset=['承诺','费用'])
#print(new_financement_trade.head())

new_financement_trade = financement_trade.sort_values('本息费',ascending=False)
#print(new_financement_trade[:10])
financement_trade_reindexed = new_financement_trade.reset_index(drop=True)
#print(financement_trade_reindexed.loc[0:10])

def hundredth_row(columns):
    hundredth_item = columns.loc[99]
    return hundredth_item

hundredth_row = financement_trade.apply(hundredth_row)
print(hundredth_row)
#returen 第一百行 from each columns
#apply指的传进来一个function, 按照function的定义去操作


