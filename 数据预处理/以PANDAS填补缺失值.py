import pandas as pd

data = pd.read_csv(r"D:\python\datasets\Titanic.csv",index_col=0)
data.loc[:,'Age'] = data.loc[:,'Age'].fillna(data.loc[:,'Age'].median())
#fillna可以直接填充
print(data.loc[:,'Age'].head())

data.drop(axis=0,inplace=True)
#axis=0:删除所有有缺失值的行；axis=1:删除所有有缺失值的列
#参数inplace, 为True表示在原数据集上进行修改，为False表示生成一个复制对象，不修改原数据，默认为False
