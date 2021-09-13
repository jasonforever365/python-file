import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

x =np.linspace(0,1,20)
y = []

for epsilon in np.linspace(0,1,20):
    E = np.array([comb(25,i)*(epsilon**i)*((1-epsilon)**(25-i)) for i in range(13,26)]).sum()
    y.append(E)

plt.plot(x,y,"o-", label='when estimators are different')
plt.plot(x,y,"--",color='red',label='if all estimators are same')
plt.xlabel("individual estimator's error")
plt.ylabel("RandomForest's error")
plt.legend()
plt.show()
