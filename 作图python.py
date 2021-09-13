#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\zhou jian\Desktop\datasets\Titanic.csv", )
df.head()


# In[4]:


df.boxplot("Fare", by = "Pclass")


# In[12]:


import seaborn as sns
sns.catplot(data = df, x = "Survived", y = "Age", kind = "violin")


# In[ ]:




