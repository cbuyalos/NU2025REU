#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Import Packages and define A and B (version as stated in Smilga)

import sympy
from sympy import sqrt
from sympy.solvers import solve
from sympy import Symbol
from sympy import *
m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9, m_10 = symbols('m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9, m_10')
q, s, r, y, x, t = symbols('q, s, r, y, x, t')

def A(x):
    return Matrix([[1, x], [0, 1]])

def B(q, x):
    return Matrix([[1, 0], [q*x, 1]])


# In[3]:


def sylvester_matrix(f, g, x):
    m = sympy.degree(f, x)
    n = sympy.degree(g, x)
    
    f_coeffs = sympy.Poly(f, x).all_coeffs()
    g_coeffs = sympy.Poly(g, x).all_coeffs()
    
    f_coeffs = f_coeffs + [0]*(n-1)
    g_coeffs = g_coeffs + [0]*(m-1)
    
    rows = []
    rows.append(f_coeffs)
    for i in range(n - 1):
        f_coeffs = f_coeffs[0:-1]
        f_coeffs.insert(0, 0)
        rows.append(f_coeffs)
    rows.append(g_coeffs)
    for i in range(m - 1):
        g_coeffs = g_coeffs[0:-1]
        g_coeffs.insert(0, 0)
        rows.append(g_coeffs)
        
    return sympy.Matrix(rows)

def resultant_poly(f, g, x):
    return sylvester_matrix(f, g, x).det()


# In[6]:


a_1, a_2, a_3, a_4, a_5 = symbols('a_1, a_2, a_3, a_4, a_5')
b_1, b_2, b_3, b_4, b_5 = symbols('b_1, b_2, b_3, b_4, b_5')

#resultant of P^3 and P^3
resultant_poly(a_1*a_2*a_3*t + a_1 - a_2 + a_3, b_1*b_2*b_3*(x-t) + b_1 - b_2 + b_3, t)

#resultant of P^4 and P^4
resultant_poly(a_1*a_2*a_3*a_4*t + a_1*a_2 - a_2*a_3 + a_3*a_4 + a_1*a_4, b_1*b_2*b_3*b_4*(x-t) + b_1*b_2 - b_2*b_3 + b_3*b_4 + b_1*b_4, t)

#resultant of P^3 and P^3 -- ISSUE is that the degree of this polynomial is 4
resultant_poly(a_1*a_2*a_3*a_4*a_5*t**2 + (a_1*a_2*a_3 - a_2*a_3*a_4 + a_1*a_2*a_5 + a_1*a_4*a_5 + a_3*a_4*a_5)*t + a_1 - a_2 + a_3 - a_4 + a_5, b_1*b_2*b_3*b_4*b_5*(x-t)**2 + (b_1*b_2*b_3 - b_2*b_3*b_4 + b_1*b_2*b_5 + b_1*b_4*b_5 + b_3*b_4*b_5)*(x-t) + b_1 - b_2 + b_3 - b_4 + b_5, t)


# In[12]:


#We can use this to test specific values 

def deg_three_test(a_1, a_2, a_3, b_1, b_2, b_3):
    return resultant_poly(a_1*a_2*a_3*t + a_1 - a_2 + a_3, b_1*b_2*b_3*(x-t) + b_1 - b_2 + b_3, t)
def deg_four_test(a_1, a_2, a_3, a_4, b_1, b_2, b_3, b_4):
    return resultant_poly(a_1*a_2*a_3*a_4*t + a_1*a_2 - a_2*a_3 + a_3*a_4 + a_1*a_4, b_1*b_2*b_3*b_4*(x-t) + b_1*b_2 - b_2*b_3 + b_3*b_4 + b_1*b_4, t)

def deg_five_test(a_1, a_2, a_3, a_4, a_5, b_1, b_2, b_3, b_4, b_5):
    return resultant_poly(a_1*a_2*a_3*a_4*a_5*t**2 + (a_1*a_2*a_3 - a_2*a_3*a_4 + a_1*a_2*a_5 + a_1*a_4*a_5 + a_3*a_4*a_5)*t + a_1 - a_2 + a_3 - a_4 + a_5, b_1*b_2*b_3*b_4*b_5*(x-t)**2 + (b_1*b_2*b_3 - b_2*b_3*b_4 + b_1*b_2*b_5 + b_1*b_4*b_5 + b_3*b_4*b_5)*(x-t) + b_1 - b_2 + b_3 - b_4 + b_5, t)

# this is k=1,k=2 of (i)
solve(deg_four_test(1, -1, -1, 8, 1, -1, -2, 24))
# this is(k=2,k=3) of fibb. sequence
solve(deg_five_test(1, -1, 1, -1, 2, 1, -1, 1, -1, -4))


# In[59]:


## We want to turning this polynomial into the form of a P^3 polynomial:
deg_three_test(a_1, a_2, a_3, b_1, b_2, b_3)

#in order to do this, the following condition_polynomial must vanish:
def condition_polynomial(a_1, a_2, a_3, b_1, b_2, b_3):
    return (a_1*a_2*a_3*b_1 + b_1*b_2*b_3*a_1)*(a_1*a_2*a_3*b_2 + b_1*b_2*b_3*a_2)*(a_1*a_2*a_3*b_3+ b_1*b_2*b_3*a_3) - (a_1*a_2*a_3*b_1*b_2*b_3)

#I cannot find a value where this happens. We can test example values, ex
solve(condition_polynomial(1, 1, 1, -1, -1, x))


# In[ ]:




