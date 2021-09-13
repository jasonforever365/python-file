from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = pd.read_csv(r"D:\python\datasets\Titanic.csv",index_col=0)
data_2 = data.copy()

from sklearn.preprocessing import Binarizer
X = data_2.iloc[:,5].values.reshape(-1,1) #类为特征，需升维度
transformer = Binarizer(threshold=30).fit_transform(X)
print(transformer)
