from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs

#make_blobs：自己创建数据集
X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)

#基于轮廓系数来选择最佳的n_clusters
#知道每个聚类的轮廓系数大小，和类之间的轮廓系数对比
#每个聚类完毕之后图像的分布情况

#先设定我们要分成的蔟族
n_clusters = 4

#创建一个画布，画布上共有一行两列两个图
fig, (ax1,ax2) = plt.subplots(1,2)

#画布尺寸
fig.set_size_inches(18,7)

#plt.figure(figsize=())

#首先我们设定横坐标
#轮廓系数的取值范围在[-1,1]之间，但至少大于0
#太长的横坐标不利于我们的可视化，所以X轴的取值在[-0.1,1]之间
ax1.set_xlim([-0.1,1])
ax1.set_ylim([0,X.shape[0]+(n_clusters+1)*10])

#开始建模，调用聚类好的标签
clusterer = KMeans(n_clusters=n_clusters,random_state=10).fit(X)
cluster_labels = clusterer.labels_

#调用轮廓系数分数，注意silhouette_score生产的是所有样本点的轮廓系数均值
#输入两个参数是，特征矩阵X和聚类完毕后的标签
silhouette_avg = silhouette_score(X, cluster_labels)
print("For n_clusters =", n_clusters,
      "The average silhouette_score is", silhouette_avg)

#调用silhouette_samples,返回每个样本点的轮廓系数，这就是我们的横坐标
sample_silhouette_values = silhouette_samples(X,cluster_labels)

#设定y轴取值
y_lower = 10

#接下来对每一个蔟进行循环
for i in range(n_clusters):
    #每个样本轮廓系数结果中抽出第i个蔟的轮廓系数，并对其排序
    ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
    #对其排序
    ith_cluster_silhouette_values.sort()
    #查看蔟里有多少样本
    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    #这个蔟的取值
    y_upper = y_lower + size_cluster_i
    #colormap库中，调用小数来调用颜色的函数
    color = cm.nipy_spectral(float(i)/n_clusters)


    #开始填充子图1中的内容
    #fill_between是一个范围中柱状图都统一颜色的函数
    #fill_betweenx的范围是在纵坐标上
    #fill_betweeny的范围是在横坐标上
    #fill_betweenx的参数应该输入（纵坐标的下限，纵坐标的上限，x轴上的取值，柱状图的颜色）
    ax1.fill_betweenx(np.arange(y_lower,y_upper)
                      ,ith_cluster_silhouette_values
                      ,facecolor=color
                      ,alpha=0.7)
    #为每个蔟的轮廓系数写上蔟的编号，并且让蔟的编号显示坐标轴上每个条形图的中间位置
    #text的参数为（要显示编号的位置的横坐标，要显示编号的位置的纵坐标，显示编号内容）
    ax1.text(-0.05
             ,y_lower + 0.5*size_cluster_i
             ,str(i))

    #为下一个蔟计算新的y轴上的初始值，是每一次迭代之后，y的上线再加上10
    #依次保证不同的蔟图像之间显示有空隙
    y_lower = y_upper +10

#给图1加上标题，横坐标轴和纵坐标轴的标签
ax1.set_title("The silhouette plot for the various clusters.")
ax1.set_xlabel("The silhouette coefficient values")
ax1.set_ylabel("Cluster label")
#把整个数据集上的轮廓系数均值以虚线的形式放入我们图中
ax1.axvline(x=silhouette_avg,color='red',linestyle='--')
#让y轴不显示刻度
ax1.set_yticks([])
#让y轴刻度显示为我们规定的列表
ax1.set_xticks([-0.1,0,0.2,0.4,0.6,0.8,1])

#对第二个图进行处理，首先重新颜色，由于没有循环，一次性生成多个颜色
colors = cm.nipy_spectral(cluster_labels.astype(float)/n_clusters)
#astype(float):生产1，2，3之类的浮点数
ax2.scatter(X[:,0],X[:,1]
            ,marker='o'#点形状
            ,s=8 #点大小
            ,c=colors
            )

#把生产的质心放进图像中
centers = clusterer.cluster_centers_
#draw white circles at cluster centers
ax2.scatter(centers[:,0], centers[:,1],marker='x',
            c='red',alpha=1,s=200)
#为图二设置标题，横坐标标题和纵坐标的标题
ax1.set_title("The visualization of the clustered data.")
ax1.set_xlabel("Feature space for the 1st feature")
ax1.set_ylabel("Feature space for the 2nd feature")
#为整个图设置标题
plt.suptitle(("silhouette analysis for KMeans clustering on sample data"
             "with n_clusters = %d" % n_clusters),
             fontsize=14, fontweight='bold')
plt.show()










