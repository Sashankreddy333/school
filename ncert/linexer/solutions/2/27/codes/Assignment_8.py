#!/usr/bin/env python
# coding: utf-8

# In[1]:


#! /usr/bin/python3
import numpy as np
A=np.array([[4,3],
            [7,5]], dtype=float)

print("Given matrix A is, \n",A)

Q,R=np.linalg.qr(A)

print("Orthogonal Matrix Q :\n",Q)

print("\nQ^TQ:\n",Q.T@Q)

print("\nUpper Triangular Matrix R : \n",R)

print("\nA=QR=\n",Q@R)

