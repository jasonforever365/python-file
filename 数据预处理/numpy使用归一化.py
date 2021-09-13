import numpy as np
X = np.array([[-1,2],[-0.5,6],[-0.5,6],[0,10],[1,18]])
#归一化
#axis=0: 指的是找出每一列的最小值或最大值；axis=1: 指的是找出每一行的最小值或最大值
X_nor = (X - X.min(axis=0))/(X.max(axis=0) - X.min(axis=0))
print(X_nor)

#逆转归一化
X_returned = X_nor * (X.max(axis=0) - X.min(axis=0)) + X.min(axis=0)
print(X_returned)

