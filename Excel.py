# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:39:44 2021

@author: zhou jian
"""
import pandas as pd
print('-'*10 + "begin Section 1 导入数据" + '-'*20)
#导入.xlsx文件
filePath = r'C:\Users\zhou jian\Desktop\python\lession4.xlsx'

df = pd.read_excel(filePath)
print('1.excel的数据','*'*15)
print(df, '\n')

#指定具体sheet
df = pd.read_excel(filePath,sheet_name= 'Sheet1')
print('2.excel的数据','*'*15)
print(df, '\n')

#指定sheet的顺序，从0开始
df = pd.read_excel(filePath, sheet_name=0)
print('3.excel的数据','*'*15)
print(df, '\n')

#指定某一列为行索引
df = pd.read_excel(filePath, index_col=0)
print('4.excel的数据','*'*15)
print(df, '\n')

#指定某一行为列索引
df = pd.read_excel(filePath, header=0)
print('5.excel的数据','*'*15)
print(df, '\n')

#指定导入列，传入需要保存的列数列表
df = pd.read_excel(filePath, usecols=[0,3])
print('6.excel的数据','*'*15)
print(df, '\n')

#导入.csv文件
df =pd.read_csv(r'C:\Users\zhou jian\Desktop\python\lession4.csv', sep=' ', 
                encoding='gbk')
print('1.csv的数据是','*'*15)
print(df, '\n')
























