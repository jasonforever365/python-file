# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:41:14 2020

@author: zhou jian
"""

import random

def shengchengqi():
    list1 = []
    for i in range(10):
        list1.append(random.randint(1, 100))
        print ("new list", list1)
    for e in list1:
        yield e
    pass

myflag = True
for q in shengchengqi():
    if (myflag):
        myflag=False
        print("生成器输出值", end=" ")
    print(q, end=" ")