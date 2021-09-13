# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:00:35 2021

@author: zhou jian
"""


import seaborn as sns
import numpy as np
import matplotlib用法 as mpl
import matplotlib用法.pyplot as plt
#%matplotlib inline

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*5)*(7-i)*flip)
  
#sns.set()  #该语言表示设置为seaborn默认的风格或者理解为恢复设置 
#sns.set_style('white') 
#sns.despine(offset=30) #offset表示x轴，y轴偏移30
#print(sinplot())
        
#sns.set_style('whitegrid')

#data = np.random.normal(size=(20,6)) + np.arange(6)/2
#sns.boxplot(data=data,palette='deep')
#sns.despine(left=True) #删除左边的边框

#with sns.axes_style("darkgrid"):
    #plt.subplot(211)
    #sinplot()
#plt.subplot(212)
#sinplot(-1)

sns.set()    
sns.set_context('poster', font_scale =1, rc={"lines.linewidth":2.5}) 
#设置整体的风格
#paper, notebook, talk, poster
plt.figure(figsize=(8,6))  
sinplot()    
    
    
    
    
    