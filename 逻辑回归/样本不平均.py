import imblearn
#imblearn是专门处理不平衡数据集的库，在处理样本不均衡问题中性能高过sklearn很多
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state=42) #实例化
X, y = sm.fit_sample(X,y) #返回已经上采样完成的
n_sample_ = X.shape[0]

n_1_sample = y.value_counts()[1]
n_0_sample = y.value_counts()[0]

print('样本个数：{}; 1占{:.2%}; 0占{:.2%}'.format(n_sample_,n_1_sample/n_sample_,n_0_sample/n_sample_)