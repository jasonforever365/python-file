import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression as LR

data = pd.read_csv(r"D:\python\sklearnjqxx_jb51\【机器学习】菜菜的sklearn课堂(1-12全课)\05逻辑回归与评分卡\rankingcard.csv",index_col=0)
#print(data.head())

#去掉重复值
data.drop_duplicates(inplace =True)
#删除后不要忘记恢复索引
data.index = range(data.shape[0])

data["NumberOfDependents"].fillna(data['NumberOfDependents'].mean(), inplace=True)

#填补缺失值
data.isnull().mean()

#参数：X：要填补的特征矩阵；y:完整的，没有缺失值的标签; to_fill:字符串，要填补的那一列的名称

def fill_missing_rf(X, y, to_fill):
    df = X.copy()
    fill = df.loc[:,to_fill]
    df = pd.concat([df.loc[:,df.columns!=to_fill],pd.DataFrame(y)],axis=1)

    #找出我们的训练集和测试集
    Ytrain = fill[fill.notnull()]
    Ytest = fill[fill.isnull()]
    Xtrain = df.iloc[Ytrain.index,:]
    Xtest = df.iloc[Ytest.index, :]

    #用随机森林回归填补缺失值
    from sklearn.ensemble import RandomForestRegressor as rfr
    rfr = rfr(n_estimators=100)
    rfr = rfr.fit(Xtrain,Ytrain)
    Ypredict = rfr.predict(Xtest)

    return Ypredict

X = data.iloc[:,1:]
y= data.iloc[:,0]
y_pred = fill_missing_rf(X, y, "MonthlyIncome")
print(y_pred)

data.loc[data.loc[:,"MonthlyIncome"].isnull(),"MonthlyIncome"]

