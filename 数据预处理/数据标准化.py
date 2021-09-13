from sklearn.preprocessing import StandardScaler

data=[[-1,2],[-0.5,6],[-0.5,6],[0,10],[1,18]]
scaler = StandardScaler() #实例化
scaler = scaler.fit(data) #本质是生成均值和方差

StandardScaler(copy=True, with_mean=True, with_std=True)
print(scaler.mean_) #查看均值的属性mean_
print(scaler.var_) #查看方差的属性var_

x_std = scaler.transform(data) #通过接口导出结果






