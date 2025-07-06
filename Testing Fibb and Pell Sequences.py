#!/usr/bin/env python
# coding: utf-8

# In[7]:


## Import Packages and define A and B (version as stated in Smilga)

import sympy
from sympy import sqrt
from sympy.solvers import solve
from sympy import Symbol
from sympy import *
q, s, r, y, x, t = symbols('q, s, r, y, x, t')

def A(x):
    return Matrix([[1, x], [0, 1]])

def B(q, x):
    return Matrix([[1, 0], [q*x, 1]])


# In[8]:


## Our first goal will be to Check the Fiboncci Sequence from Smilga:


# Checks Fibb.-type sequences (n odd)
def Fibb_seq_checker(q, n, x):
    '''
    q = tau (rational parameter)
    n = odd integer, length of half-relation (for Fibb. half-relation from Smilga, n=5)
    x = integer, parameter for final matrix (for Fibb. half-relation from Smilga, x = 2(-1)^k F_{k-1}F_k )
    '''
    M = eye(2)
    for i in range(0, n):
        if (i+1) % 2 == 0:
            M = M*B(q, -1)
        if (i+1) % 2 != 0 and (i + 1) != n:
            M = M*A(1)
        if (i + 1) == n:
            M = M*A(x)
    return q*M[0, 1] - M[1, 0]


# In[9]:


#Check Fibb_seq_checker function, we should be getting 0 for all:

print("q = 2", Fibb_seq_checker(2, 5, 0))
print("q = 3", Fibb_seq_checker(3, 5, 2))
print("q = 5/2", Fibb_seq_checker(5/2, 5, -4))
print("q = 8/3", Fibb_seq_checker(8/3, 5, 12))
print("q = 13/5", Fibb_seq_checker(13/5, 5, -30))


# In[10]:


def check_pell_seq(q, n, x):
    '''
    q = tau (rational parameter)
    n = even integer, length of half-relation (for pell. half-relation from Smilga, n=10)
    x = integer, parameter for first and final matrix (for pell. half-relation from Smilga, x = (-1)^k P_{k-1} P_k)
    '''
    M = A(x)
    for i in range(0, n):
        if (i+1) % 2 == 0:
            M = M*B(q, -1)
        if (i+1) % 2 != 0 and (i + 1) != 1 and (i + 1) != n - 1:
            M = M*A(1)
        if (i + 1) == n - 1:
            M = M * A(x)
    return M[0, 0] - M[1, 1]


# In[11]:


#Check check_pell_seq function, we should be getting 0 for all:

print("q = 3", check_pell_seq(3, 10, 0))
print("q = 7/2", check_pell_seq(7/2, 10, 2))
print("q = 17/5", check_pell_seq(17/5, 10, -10))
print("q = 41/12", check_pell_seq(41/12, 10, 60))


# In[ ]:




