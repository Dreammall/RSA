#!/usr/bin/env python
# coding: utf-8

# In[124]:


import random
from sympy import isprime

# ビット長 k
k = 1024

min = 2**(k-2)
max = 2**(k-1)
print(min)
print("   ")
print(max)
print("   ")
    
# 2^k-2 以上 2^k-1 未満の、kビットの乱数p,qを生成
p = random.randint(min,max)
q = random.randint(min,max)

def exEuclid(e, R):   
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    r0, r1 = e, R
    while r1 != 0:
        x0, x1 = x1, x0 - x1 * (r0 // r1)
        y0, y1 = y1, y0 - y1 * (r0 // r1)
        r0, r1 = r1, r0 % r1
    if x0 < 0:
        x0 += R
        y0 -= e
    return (x0, y0, r0)

# e = 65537を使用することで生成のための計算を省くことができる
e = 65537
R = (p-1)*(q-1)

#if isprime(p) == True and isprime(q) == True:
(x, y, c) = exEuclid(e, R)
print("x = ", x)


# In[ ]:




