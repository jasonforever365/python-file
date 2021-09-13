import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
#对两个序列中的点进行距离匹配的函数
from sklearn.datasets import load_sample_image
#导入图片数据所用的类
from sklearn.utils import shuffle
#洗牌

#实例化，导入颐和园图片
china = load_sample_image("china.jpg")
#图片的数据类型为uint8,三维数据，长度*宽度*像素 > 三个数绝对的颜色
#包含多少种不同的颜色
newimage = china.reshape((427*640,3))

import pandas as pd
pd.DataFrame(newimage).drop_duplicates().shape
#我们有9W种颜色

#图像可视化
plt.figure(figsize=(15,15))
plt.imshow(china)
#plt.show()

#查看模块中的另一张图片
flower = load_sample_image('flower.jpg')
plt.figure(figsize=(15,15))
plt.imshow(flower)
#plt.show()

#决定超参数，数据预处理
n_clusters = 64

#plt.imshow在浮点数上表现优异，在这里我们把china中的数据，转换为浮点数，压缩到[0,1]之间
china = np.array(china, dtype=np.float64)/china.max()
#把china从图像格式，转换成矩阵格式
w,h,d = original_shape = tuple(china.shape)

assert d==3
#assert相当于raise error if not,表示为，“不为True就报错”
#要求d必须等于3，如果不等于，就报错

image_array = np.reshape(china, (w*h, d))
#reshape是改变结构

#由于数据量太大，首先选择1000个数据来找出质心
image_array_sample = shuffle(image_array,random_state=0)[:1000]
kmeans = KMeans(n_clusters=n_clusters,random_state=0).fit(image_array_sample)
kmeans.cluster_centers_
#找出质心之后，将已存在的质心对所有数据进行聚类
labels = kmeans.predict(image_array)
#使用质心来替换所有的样本
image_kmeans = image_array.copy()

for i in range(w*h):
    image_kmeans[i] = kmeans.cluster_centers_[labels[i]]

pd.DataFrame(image_kmeans).drop_duplicates().shape

#恢复图片内容
image_kmeans = image_kmeans.reshape(w,h,d)

#随机矢量量化
centroid_random = shuffle(image_array,random_state=0)[:n_clusters]
labels_random = pairwise_distances_argmin(centroid_random, image_array,axis=0)

#函数pairwise_distances_argmi(x1,x2,axis) #x1,x2分布是序列
#用来计算x2中每个样本到x1的距离，并返回和x2相同形状的，x1中对应最近的样本点的索引

#使用随机质心来替换所有的样本
image_random = image_array.copy()
for i in range(w*h):
    image_kmeans[i] = centroid_random[labels_random[i]]
image_random = image_random.reshape(w,h,d)

plt.figure(figsize=(10,10))
plt.axis('off')
plt.title('Original image (96,615 colors)')
plt.imshow(china)
plt.figure(figsize=(10,10))
plt.axis('off')
plt.title('Quantized image (64 colors, K-Means)')
plt.imshow(image_kmeans)
plt.figure(figsize=(10,10))
plt.axis('off')
plt.title('Quantized image (64 colors, Random)')
plt.imshow(image_random)
plt.show()


