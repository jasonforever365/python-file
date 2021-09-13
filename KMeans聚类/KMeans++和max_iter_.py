from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#make_blobs：自己创建数据集
X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)

plus = KMeans(n_clusters=10).fit(X)
print(plus.n_iter_)
#默认init = 'KMeans++'

random = KMeans(n_clusters=10,init='random',random_state=420).fit(X)
print(random.n_iter_)

random = KMeans(n_clusters=10,init='random', max_iter=10
                ,random_state=420).fit(X)
y_pred_max10 = random.labels_
print(silhouette_score(X,y_pred_max10))

random = KMeans(n_clusters=10,init='random', max_iter=20
                ,random_state=420).fit(X)
y_pred_max20 = random.labels_
print(silhouette_score(X,y_pred_max20))