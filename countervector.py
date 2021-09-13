# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:47:23 2021

@author: zhou jian
"""


from sklearn.feature_extraction.text import CountVectorizer

vector = CountVectorizer()
res = vector.fit_transform(['life is short, i like python', 'life is too long, i dislike python'])
print(vector.get_feature_names())
print(res.toarray())

