from sklearn.datasets import fetch_lfw_people
from  sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

faces = fetch_lfw_people(min_faces_per_person=60) #实例化
#跟数字数据区别，多一个键值对：image(除data, target, target_names)
print(faces.data.shape)
#行是样本
#列是样本相关的所有特征
print(faces.images.shape)
#三维数组，第一个数是第三维，1348是图像的个数，62是图像矩阵的行数，47是图像矩阵的列数

X = faces.data

fig, axes = plt.subplots(3,8                    #subplot的个数：3行8列
                        ,figsize =(8,4)        #画布的尺寸8*4
                        ,subplot_kw ={"xticks":[],"yticks":[]} #子图不显示坐标轴
                        )
#axes[0][0].imshow(faces.images[0,:,:])
for i, ax in enumerate(axes.flat):
    ax.imshow(faces.images[i,:,:], cmap='gray')
    #camp的取值
plt.show()

#降维
pca = PCA(150).fit(X)
#这里注意不能用faces.data来代替X。因为sklearn不接受高维数组
V = pca.components_

#将新特征向量空间可视化
fig, axes = plt.subplots(3,8                    #subplot的个数：3行8列
                        ,figsize =(8,4)        #画布的尺寸8*4
                        ,subplot_kw ={"xticks":[],"yticks":[]} #子图不显示坐标轴
                        )
for i, ax in enumerate(axes.flat):
    ax.imshow(V[i, :].reshape(62,47), cmap='gray')
plt.show()

#说明什么：新特征空间里的特征向量们。大部分是“五官”和“亮度”相关的向量