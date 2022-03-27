#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import *
from numpy import *

N = 100
R, lamda = 1.0, 500E-9
d = 100E-6

dx, dy = d/N, d/N
scene1 = canvas(align='left', height=600, width=600, center=vector(N*dx/2, N*dy/2, 0))
scene2 = canvas(align='right', x=600, height=600, width=600, center=vector(N*dx/2, N*dy/2, 0))
scene1.lights, scene2.lights = [], []
scene1.ambient, scene2.ambient = color.gray(0.99), color.gray(0.99)
side = linspace(-0.01*pi, 0.01*pi, N)
x,y = meshgrid(side,side)

E_field = zeros((N, N))
for i in range (N):
    for j in range (N):
        point = vec( (-d/2)+i*dx , (-d/2)+j*dy , 0 )
        if mag(point) <= d/2:
            E_field += cos( ((2*pi*x)/lamda)*point.x + ((2*pi*y)/lamda)*point.y ) * dx * dy

Inte = abs(E_field) ** 2
maxI = amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas=scene1, pos=vector(i*dx, j*dy, 0), length=dx, height=dy, width=dx,
            color=vector(Inte[i,j]/maxI, Inte[i,j]/maxI, Inte[i,j]/maxI))


Inte = abs(E_field)
maxI = amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas=scene2, pos=vector(i*dx, j*dy, 0), length=dx, height=dy, width = dx,
            color=vector(Inte[i,j]/maxI, Inte[i,j]/maxI, Inte[i,j]/maxI))
    
compare = 9999
for i in range (50):
    next = Inte[50+i, 50]
    if next > compare:
        count = i
        break
    compare = next
    
r = count*((2*0.01*pi)/N)
print("Radius = ", r)
print("theta_theo = ", ((1.22*lamda)/d))
print("theta_exp = ", atan(r/R))


# In[ ]:




