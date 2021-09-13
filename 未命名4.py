# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 05:33:20 2021

@author: zhou jian
"""


import pandas as pd
books = pd.read_excel(r'C:\Users\zhou jian\Desktop\python\book.xlsx', skiprows=3,usecols='C:F', 
                      index_col=None)
print(books)