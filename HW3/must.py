#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import *

g = 9.8
size, m = 0.05, 0.2
L, k = 0.5, [15, 12, 17]
v = [1, 2, 2.2]
d = [-0.06, 0, -0.1]
t = 0

scene = canvas(width=400, height=400, center=vec(0.4, 0.2, 0), align='left', background=vec(0.5, 0.5, 0))
floor = box(pos=vec(0.4, 0, 0), length=0.8, height=0.005, width=0.8, color=color.blue)
wall = box(pos=vec(0, 0.05, 0), length=0.01, height=0.1, width=0.8)

balls = []
for i in range(3):
    ball = sphere(pos=vec(L+d[i], size, (i-1)*3*size), radius=size, color=color.red) 
    ball.v = vec(v[i], 0, 0)
    balls.append(ball)
    
springs =[]
for i in range(3):
    spring = helix(pos=vec(0, size, (i-1)*3*size), radius=0.02, thickness=0.01) 
    spring.axis = balls[i].pos - spring.pos
    spring.k = k[i]
    springs.append(spring)
    
sf=[]
for i in range(3):
    spring_force = -k[i] * (mag(springs[i].axis) - L) * springs[i].axis.norm()
    sf.append(spring_force)

oscillation = graph(width=450, align='right')
oscillation2 = graph(width=450, align='right')
funct1 = gcurve(graph=oscillation, color=color.blue, width=2)
funct2 = gcurve(graph=oscillation, color=color.red, width=2)
funct3 = gcurve(graph=oscillation2, color=color.blue, width=2)
funct4 = gcurve(graph=oscillation2, color=color.red, width=2)
kiall = 0
peall = 0

dt = 0.001 
while True:
    rate(1000)
    springs[0].axis = balls[0].pos - springs[0].pos
    springs[1].axis = balls[1].pos - springs[1].pos
    springs[2].axis = balls[2].pos - springs[2].pos
    
    sf[0] = -k[0] * (mag(springs[0].axis) - L) * springs[0].axis.norm()
    sf[1] = -k[1] * (mag(springs[1].axis) - L) * springs[1].axis.norm()
    sf[2] = -k[2] * (mag(springs[2].axis) - L) * springs[2].axis.norm()
    balls[0].a = sf[0] / m
    balls[1].a = sf[1] / m
    balls[2].a = sf[2] / m
    
    balls[0].v += balls[0].a*dt
    balls[1].v += balls[1].a*dt
    balls[2].v += balls[2].a*dt
    balls[0].pos += balls[0].v*dt
    balls[1].pos += balls[1].v*dt
    balls[2].pos += balls[2].v*dt
    
    ki0=0.5*m*mag(balls[0].v)*mag(balls[0].v)
    ki1=0.5*m*mag(balls[1].v)*mag(balls[1].v)
    ki2=0.5*m*mag(balls[2].v)*mag(balls[2].v)
    
    pe0=k[0] * (mag(springs[0].axis) - L)*(mag(springs[0].axis) - L)*0.5
    pe1=k[1] * (mag(springs[1].axis) - L)*(mag(springs[1].axis) - L)*0.5
    pe2=k[2] * (mag(springs[2].axis) - L)*(mag(springs[2].axis) - L)*0.5
    
    kiall += (ki0+ki1+ki2)
    peall += (pe0+pe1+pe2)
    
    funct1.plot( pos=(t, ki0+ki1+ki2) )
    funct2.plot( pos=(t, pe0+pe1+pe2) )
    t+=0.001
    funct3.plot( pos=(t, kiall/t) )
    funct4.plot( pos=(t, peall/t) )


# In[ ]:




