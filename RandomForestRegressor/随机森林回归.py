import sklearn
from sklearn.datasets import load_boston
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

boston = load_boston()
#实例化
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
cross_val_score(regressor, boston.data, boston.target, cv=10,
                scoring="neg_mean_squared_error"
                )
#sklearn当中的模型评估指标（打分）列表
sorted(sklearn.metrics.SCORERS.keys())
