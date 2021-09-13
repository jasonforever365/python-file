import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import cross_val_score

dataset = load_boston()
#print(dataset.target)
#print(dataset.data.shape)

x_full, y_full = dataset.data, dataset.target
n_samples = x_full.shape[0]
n_features = x_full.shape[1]

#确认我们希望放入缺失数据的比例，在这里我们假设是50pct(missing_rate = 0.5),那总共要有3289个缺失值
rng = np.random.RandomState(0)
missing_rate=0.5
n_missing_samples = int(np.floor(n_samples * n_features * missing_rate))
#np.floor：向下取整，返回.0格式的浮点数

#所有数据要随机遍布在数据集的各行各列当中，而一个缺失的数据需要一个行索引和一个列索引
#如果能创造一个数组，包含3289个分布在0-506中间的行索引，和3289个分布在0-13之间的列索引
#然后我们用0,均值和随机森林来填写这些缺失值，然后查看回归的结果如何

missing_features = rng.randint(0, n_features, n_missing_samples)
#在randint(下限，上限，n)，请在下限和上限之间取出n个整数
missing_samples = rng.randint(0, n_samples, n_missing_samples)
#missing_samples = rng.choice(n_samples, n_missing_samples, replace=False)  #针对数据过大的解决办法

x_missing = x_full.copy()
y_missing = y_full.copy()

x_missing[missing_samples,missing_features] = np.nan
x_missing = pd.DataFrame(x_missing)
#y_missing不能空值。因为y是标签，无标签属于非监督学习

#使用均值进行填补
imp_mean = SimpleImputer(missing_values=np.nan,strategy='mean') #实例化
x_missing_mean = imp_mean.fit_transform(x_missing) #训练fit+导出predict >>> 特殊的接口fit/transform
#缺失是否仍有空值
pd.DataFrame(x_missing_mean).isnull().sum()

#使用0进行填补
imp_0 = SimpleImputer(missing_values=np.nan,strategy='constant',fill_value=0)
x_missing_0 = imp_0.fit_transform(x_missing)
pd.DataFrame(x_missing_0)

#使用随机森林填补缺失值
x_missing_reg = x_missing.copy()
#找出数据集中，缺失值从小到大排列的特征们的顺序
sortindex = np.argsort(x_missing_reg.isnull().sum(axis=0)).values
for i in sortindex:
    #构建我们的新特征矩阵(没有被选中去填充的特征+原始的标签)和新标签（被选中去填充的特征）
    df=x_missing_reg
    #构建新标签
    fillc =df.iloc[:,i]
    #新特征矩阵
    df =pd.concat([df.iloc[:,df.columns!=i],pd.DataFrame(y_full)],axis=1)
    #在新特征矩阵中，对含有缺失值的列，进行0的填补
    df_0 =SimpleImputer(missing_values=np.nan, strategy='constant',fill_value=0).fit_transform(df)

    #找出训练集和测试集
    #被选中要填充的特征中（标签），存在的那些值，非空值
    Ytrain = fillc[fillc.notnull()]
    #被选中要填充的特征中（标签），不存在的那些值，是空值
    #需要的不是Ytest的值，而是Ytest的索引
    Ytest = fillc[fillc.isnull()]
    #在新特征矩阵上， 被选出来的要填充的特征的非空值所对应的记录
    Xtrain = df_0[Ytrain.index,:]
    #在新特征矩阵上， 被选出来的要填充的特征的空值所对应的记录
    Xtest = df_0[Ytest.index,:]

    #用随机森林回归来填补缺失值
    rfc = RandomForestRegressor(n_estimators=100) #实例化
    rfc = rfc.fit(Xtrain,Ytrain)
    Ypredict = rfc.predict(Xtest)

    #讲补好的特征返回到原始的特征矩阵中
    x_missing_reg.loc[x_missing_reg.iloc[:,i].isnull(),i] = Ypredict

#对填充好的数据进行建模
#X包含4个特征
X=[x_full,x_missing_mean,x_missing_0,x_missing_reg]
mse= []
std= []
for x in X:
    estimator=RandomForestRegressor(random_state=0,n_estimators=100)
    scores = cross_val_score(estimator,x,y_full,scoring='neg_mean_squared_error',cv=5).mean()
    mse.append(scores * -1) #选择的负的均方误差

[*zip(["x_full","x_missing_mean","x_missing_0","x_missing_reg"],mse)]

x_labels = ["Full Data","Mean Imputation","Zero Imputation","Regressor Imputation"]
colors = ["r","g","b","orange"]

plt.figure(figsize=(12,6)) #画出画布
ax=plt.subplot(111) #添加子图
for i in np.arange(len(mse)): #相当于range(len(mse))
    ax.barh(i, mse[i],color=colors[i], alpha=0.6, align='center')
    #barh: bar horizon横向条形图
ax.set_title("imputation Techique with Boston Data")
ax.set_xlim(left=np.min(mse)*0.9,
            right=np.max(mse)*1.1)
ax.set_yticks(np.arange(len(mse)))
ax.set_xlabel("MSE")
ax.invert_yaxis() #命名y轴
ax.set_yticklabels(x_labels)
plt.show()
