from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = pd.read_csv(r"D:\python\datasets\Titanic.csv",index_col=0).dropna()
data.iloc[:,-1] = LabelEncoder().fit_transform(data.iloc[:,-1])
print(data.head())