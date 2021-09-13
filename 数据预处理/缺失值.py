import pandas as pd
data = pd.read_csv(r"D:\python\datasets\Titanic.csv",index_col=0)
#index_col=0: 将原始表再单列出一列作为序列
#print(data.head())

Age = data.loc[:,'Age'].values.reshape(-1,1) #sklearn当中特征矩阵必须是二维

from sklearn.impute import SimpleImputer

imp_mean = SimpleImputer() #实例化，默认均值填补
imp_median = SimpleImputer(strategy='median') #用中位数填补
imp_0 = SimpleImputer(strategy='constant',fill_value=0) #用0填补

imp_mean = imp_mean.fit_transform(Age)
imp_median = imp_median.fit_transform(Age)
imp_0 = imp_0.fit_transform(Age)
#print(imp_mean)
#print(imp_median)
#print(imp_0)

#例如年龄，我们用中位数填补
data.loc[:,'Age'] = imp_median

#使用众数填补Embarked
Embarked = data.loc[:,'Embarked'].values.reshape(-1,1)
imp_mode = SimpleImputer(strategy='most_frequent')
data.loc[:,'Embarked'] = imp_mode.fit_transform(Embarked)
