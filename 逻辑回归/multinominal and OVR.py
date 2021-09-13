from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()

for multi_class in ("multinomial","ovr"):
    lr = LogisticRegression(solver="sag", max_iter=100, random_state=42,
                             multi_class=multi_class).fit(iris.data, iris.target)

    print("training score: %.3f(%s)"% (lr.score(iris.data, iris.target), multi_class))
    # 用%来代替打印的字符串中，想由变量替换的部分，%.3f表示，保留三位小数的浮点数，%s表示，字符串