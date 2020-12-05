#!/usr/bin/env python
# coding: utf-8

# In[89]:


from sympy import isprime
import math
import numpy

# コード化した平文を入力
m = 4
print("コード化した平文：m =",m)
# 素数 p, q
p = 13
q = 2
if isprime(p) == True and isprime(q) == True:
    print("pとqは素数です")
# 公開鍵１
n = p * q
print("[公開鍵１] 法：n =",n)
# 公開鍵２
e = 5
print("[公開鍵２] e =",e)
# 非公開鍵の法 n
R = (p-1)*(q-1)
print("λ：",R)
# 秘密鍵 d
for d in range(10):
    if(pow(d*e,1,R)==1 ):
        print("[秘密鍵] d =",d)
        break

# RSA 暗号化関数
def RSAenc(t,k,l):
    cc = pow(t,k,l)
    return cc

# RSA 復号化関数
def RSAdec(x,y,z):
    mm = pow(x,y,z)
    return mm

c = RSAenc(m,e,n)
dec = RSAdec(c,d,n)
print("   ")
print("[暗号文] c1 =",c)
print("[復号文] m =",dec)


# In[ ]:




