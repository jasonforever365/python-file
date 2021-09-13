# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:03:15 2021

@author: zhou jian
"""

variable =2 
_variable = 3
#变量只能以字母或_开头
#print('H' in 'Hello')
#print('xiaofeizaichengxuyuan'.find('xiaofei'))
#print('Hello word'.split(' '))
null_list = [1, 2.1, 3]
#print (null_list*3)
null_list = null_list *2
print (null_list)
null_list.insert(2, 5)
#在第三个位置加入5
print (null_list)
print (null_list.count(1))
null_list[0:2]
null_list.remove(1)
print (null_list)
null_list.sort(reverse=True)
#sort(reverse=True)是倒叙排列
print (null_list)

dict.keys()
dict.value()
dict.items()