import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import numpy as np

iris = load_iris()
y = iris.target
x = iris.data

pca_f = PCA(n_components=0.97, svd_solver='full')
x_f = pca_f.fit_transform(x)
#print(x_f)
#print(pca_f.explained_variance_ratio_)

pca_2 = PCA(2).fit(x).components_
#components_反映的就是切片之后/降维之后，新的特征空间V(k,n)
print(pca_2.shape)