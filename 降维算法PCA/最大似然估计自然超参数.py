import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import numpy as np

iris = load_iris()
y = iris.target
x = iris.data

pca_mle = PCA(n_components='mle')
x_mle = pca_mle.fit_transform(x)
#print(x_mle)
print(pca_mle.explained_variance_ratio_.sum())

#mle选择了最优的情况：n_components=3
