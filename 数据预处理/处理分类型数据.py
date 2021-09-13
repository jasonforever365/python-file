from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = pd.read_csv(r"D:\python\datasets\Titanic.csv",index_col=0).dropna()
data.iloc[:,-1] = LabelEncoder().fit_transform(data.iloc[:,-1])
#print(data.head()) #把最后一列变成了（0，1, 2）

from sklearn.preprocessing import OrdinalEncoder
#接口OrdinalEncoder的categories_对应LabelEncoder的classes_功能
data_ = data.copy()
OrdinalEncoder().fit(data_.iloc[:,1:-1]).categories_
data_.iloc[:,1:-1] = OrdinalEncoder().fit_transform(data_.iloc[:,1:-1])
#print(data_.iloc[:,1:-1])

from sklearn.preprocessing import OneHotEncoder
X = data.iloc[:,1:-1]
enc = OneHotEncoder(categories='auto').fit(X)
result = enc.transform(X).toarray()
#toarray: 转化为一个数组
#print(result)

newdata = pd.concat([data, pd.DataFrame(result)],axis=1)
#print(newdata.head())\
newdata.drop(['Sex','Embarked'],axis=1, inplace = True)