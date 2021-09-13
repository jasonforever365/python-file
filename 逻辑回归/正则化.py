from sklearn.linear_model import LogisticRegression as LR
from sklearn.datasets import load_breast_cancer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X = data.data
y = data.target
#print(X.shape)

#lrl1 = LR(penalty="l1",solver='liblinear',C=0.5, max_iter=1000)
#lrl2 = LR(penalty="l2",solver='liblinear',C=0.5, max_iter=1000)

#逻辑回归的重要属性coef_，查看每个特征所对应的参数
#lrl1 = lrl1.fit(X,y)
#lrl1.coef_
#lrl1.coef_有好多为0
#(lrl1.coef_ !=0).sum(axis=1)
#有10个特征不为0

#lrl2= lrl2.fit(X,y)
#lrl2.coef_
#lrl2.coef_有好多为0
#(lrl2.coef_ !=0).sum(axis=1)
#所有特征均不为0

l1 = []
l2 = []
l1test = []
l2test = []

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y ,test_size=0.3, random_state=420)

for i in np.linspace(0.05, 1, 19):
    lrl1 = LR(penalty="l1", solver='liblinear', C=i, max_iter=1000)
    lrl2 = LR(penalty="l2", solver='liblinear', C=i, max_iter=1000)

    #accuracy_score用于衡量预测和现实的差距
    lrl1 = lrl1.fit(Xtrain,Ytrain)
    l1.append(accuracy_score(lrl1.predict(Xtrain),Ytrain))
    l1test.append(accuracy_score(lrl1.predict(Xtest),Ytest))

    lrl2 = lrl2.fit(Xtrain,Ytrain)
    l2.append(accuracy_score(lrl2.predict(Xtrain), Ytrain))
    l2test.append(accuracy_score(lrl2.predict(Xtest), Ytest))

graph = [l1,l2,l1test, l2test]
color = ["green", "black", "lightgreen","gray"]
label = ["L1", "L2", "L1test", "L2test"]

plt.figure(figsize=(6,6))
for i in range(len(graph)):
    plt.plot(np.linspace(0.05, 2, 19), graph[i], color[i], label=label[i])

plt.legend(loc=4) #图例的位置再哪里？4表示右下角
plt.show()