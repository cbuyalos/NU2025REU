#!/usr/bin/env python
# coding: utf-8

# In[150]:


#create a list of coprime numbers from 1 to s
import math

def coprime_list(s : int):
    output = []
    for i in range(2, s):
        gcd = math.gcd(i, s)
        if gcd == 1:
            output.append(i)
    return output

#find w that divide s \pm 1
def divides_spm1(s: int):
    output = []
    for i in range(2, s + 2):
        if (s+1) % i == 0 and i not in output:
            output.append(i)
        if (s-1) % i == 0 and i not in output:
            output.append(i)
    return output

#create a list capturing small values in \bigcap (w: s)
def create_residue_class_union(s : int):
    output = []
    for i in divides_spm1(s):
        output.extend([i - 2*s, i - s, i, i + s, i + 2*s])
        output.extend([-i - s, -i, -i + s, -i + 2*s, -i + 3*s])
    return output
        
#check if all the coprime integers (w st gcd(w, s) = 1) is contained in our large list of residue classes
def check_coprime_subset_residues(s : int):
    cp_list = coprime_list(s)
    residue_list = create_residue_class_union(s)
    for i in cp_list:
        if i not in residue_list:
            return False
    return True

#check if all members of the residue class are coprime to s.
def check_residue_subset_coprime(s : int):
    residue_list = create_residue_class_union(s)
    for i in residue_list:
        if math.gcd(i, s) != 1:
            return False
    return True

        


# In[151]:


for i in range(2, 100):
    print(i, check_coprime_subset_residues(i), check_residue_subset_coprime(i))


# In[ ]:




