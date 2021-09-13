# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:36:45 2021

@author: zhou jian
"""


import numpy as np
import seaborn as sns
import matplotlib用法.pyplot as plt

sns.set(rc={"figure.figsize":(6,6)})
#分类色板
current_palette=sns.color_palette()
#sns.palplot(current_palette)

#sns.palplot(sns.color_palette('hls',8))

data=np.random.normal(size=(20,8)) + np.arange(8)/2
#sns.boxplot(data=data, palette=sns.color_palette('hls',8))
#不同的数据传进来8中不同的颜色
sns.palplot(sns.hls_palette(8, l=7, s=9))
#l:调节亮度；s：调节饱和度
sns.palplot(sns.color_palette('Paired',8))
#调出的调色板是4对