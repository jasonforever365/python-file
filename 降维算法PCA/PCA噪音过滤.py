from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()

def plot_digits(data):
    #data的结构必须是（m,n），并且n要能够被分成（8，8）的结构
    fig, axes = plt.subplots(4,10,figsize= (10,4)
                    ,subplot_kw={"xticks":[],"yticks":[]}
                )
    for i, ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(8,8),cmap='binary')
    plt.show()

#print(plot_digits(digits.data))

#人为加上噪音
rng = np.random.RandomState(42)
#在指定的数据集中，随机抽取服从正态分布的数据
#两个参数，分布是指定的数据集，和抽取出来的正态分布的方差
noisy = rng.normal(digits.data,2)
print(plot_digits(noisy))

#降维
pca = PCA(0.5, svd_solver ='full').fit(noisy)
x_dr = pca.transform(noisy)
x_dr.shape

#逆转降维结果，实现降噪
without_noise = pca.inverse_transform(x_dr)
plot_digits(without_noise)
