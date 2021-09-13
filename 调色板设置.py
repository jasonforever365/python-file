# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:19:38 2021

@author: zhou jian
"""


import numpy as np
import matplotlib用法.pyplot as plt
import seaborn as sns

#plt.plot([0,1],[0,1],sns.xkcd_rgb['pale red'],lw=3)
#plt.plot([0,1],[0,2],sns.xkcd_rgb['medium green'],lw=3)
#plt.plot([0,1],[0,3],sns.xkcd_rgb['denim blue'],lw=3)
#xkcd_rgb修改颜色

#sns.palplot(sns.color_palette('Blues'))
#sns.palplot(sns.color_palette('Blues_r'))
#颜色渐变图(由浅变深)，加上_r表示由深变浅

#sns.palplot(sns.color_palette('cubehelix',8))
#色调线性的变换
#sns.palplot(sns.cubehelix_palette(8, start=.5, rot=-.75))

sns.palplot(sns.light_palette('green'))
sns.palplot(sns.dark_palette('purple'))
sns.palplot(sns.light_palette('navy',reverse='True'))

