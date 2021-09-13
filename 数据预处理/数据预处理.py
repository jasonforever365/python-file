from sklearn.preprocessing import MinMaxScaler
data = [[-1,2],[-0.5,6],[-0.5,6],[0,10],[1,18]]

#不太熟悉numpy的小伙伴，能够判断data的结构么
#如果换成表是什么样子
import pandas as pd
pd.DataFrame(data)

#实现归一化
#scaler = MinMaxScaler() #实例化
#scaler = scaler.fit(data) #通过fit训练出min(x)和max(x)
#result = scaler.transform(data) #通过接口导出结果
#或者fit_transform
#result = scaler.fit_transform(data)
#print(result)
#归一化后的结果逆转
#print(scaler.inverse_transform(result))

#使用MinMaxScaler的参数feature_range实现将数据归一化到[0,1]以外的范围中
data=[[-1,2],[-0.5,6],[-0.5,6],[0,10],[1,18]]
scaler = MinMaxScaler(feature_range=[5,10]) #依然实例化
result = scaler.fit_transform(data)
print(result)

#当x中的特征数量非常多的时候，fit会报错并表示，数据量太大了，计算不了
#此时使用partial_fit作为训练接口
#scaler = scaler.partial_fit(data)

