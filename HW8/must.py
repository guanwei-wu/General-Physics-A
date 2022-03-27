#!/usr/bin/env python
# coding: utf-8

# In[21]:


from vpython import*
import numpy as np
import math
R = 0.12
r = 0.06
h = 0.1
m = 1000
n = 500
k = 10**(-7)
N = 1
j = 1

def ring(radius):
    sum = vec(0, 0, 0) 
    pos = (radius, 0, h)
    meg = 0
    for i in range(m):
        ds = vec(R*cos(2*math.pi*(i+1)/m) - R*cos(2*math.pi*i/m), R*sin(2*math.pi*(i+1)/m) - R*sin(2*math.pi*i/m), 0)
        dr = vec(radius - R*cos(2*math.pi*i/m), -R*sin(2*math.pi*i/m), h)
        sum += (cross(ds, dr)*k / mag(dr)**3)
    meg = sum.z*math.pi*(radius**2 - (radius - r/n)**2)
    return meg

total = 0
for i in range(n):
    total += ring(r*i/n)
    
total = (total*N)/j
print(total)

def ring_a(radius):
    sum_a = vec(0, 0, 0) 
    pos_a = (radius, 0, 0)
    meg_a = 0
    for i in range(m):
        ds_a = vec(r*cos(2*math.pi*(i+1)/m) - r*cos(2*math.pi*i/m), r*sin(2*math.pi*(i+1)/m) - r*sin(2*math.pi*i/m), h)
        dr_a = vec(radius - r*cos(2*math.pi*i/m), -r*sin(2*math.pi*i/m), h)
        sum_a += (cross(ds_a, dr_a)*k / mag(dr_a)**3)
    meg_a = sum_a.z*math.pi*(radius**2 - (radius - R/n)**2)
    return meg_a

total_a = 0
for i in range(n):
    total_a += ring_a(R*i/n)
    
total_a = (total_a*N)/j
print(total_a)


# In[ ]:




