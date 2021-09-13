#!/usr/bin/env python
# coding: utf-8

# In[3]:


coupon_rate = float(input("entering a coupon rate: "))
face = float(input("entering a face value: "))
Ir = [0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16]
m = int(input("entering remaining year: "))
coupon_discount_price = 0
Ip = []
for j in Ir:
    for i in range(m):
        coupon_discount_price += (coupon_rate*face)/((j+1)**(i+1))
    bond_price = coupon_discount_price + face/((1+j)**(1+1))
    Ip.append(bond_price)
print(Ip)




# In[4]:


import matplotlib用法.pyplot as plt
plt.scatter(Ir, Ip)
plt.xlabel("discount rate")
plt.ylabel("bond price")


# In[ ]:


coupon_rate = float(input("entering a coupon rate: "))
face = float(input("entering a face value: "))
bond_price = float(input("entering a bond value: "))
m = int(input("entering remaining year: "))
coupon_discount_price = 0
for i in range(m):
    coupon_discount_price += (coupon_rate*face)/((j+1)**(i+1))
bond_price = coupon_discount_price + face/((1+j)**(1+1))


