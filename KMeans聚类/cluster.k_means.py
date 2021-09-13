from sklearn.cluster import k_means
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)

k_means(X, 4, return_n_iter=True)
#参数return_n_iter默认为False,调整为True后就可以看到返回的最佳迭代次数

