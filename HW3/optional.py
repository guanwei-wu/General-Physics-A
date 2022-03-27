#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import*

sizes = [0.04, 0.06]
ms = [0.12, 0.2]
L, k = 0.5, 15
t = 0
period = 0
tolerence=-0.0000001

scene = canvas(width=800, height=800, center=vec(0,-0.2,0), align="left", background=vec(0.5,0.5,0))
b1 = sphere(pos=vec(-1.1*L, 0, 0), radius=sizes[0], color=color.red, v=vec(0, 0, 0))
b2 = sphere(pos=vec(0, 0, 0), radius=sizes[1], color=color.red, v=vec(0, 0, 0))
spring = helix(pos=vec(b1.pos.x, 0, 0), radius=0.02, thickness=0.01)
spring.axis = b2.pos - b1.pos

dt = 0.001 
while True:
    rate(1000)
    spring.pos = b1.pos
    spring.axis = b2.pos - b1.pos

    spring_force = -k*(mag(spring.axis) - L) * spring.axis.norm()
    b1.a = -spring_force/ms[0]     
    b2.a = spring_force/ms[1]
    b1.v += b1.a * dt
    b2.v += b2.a * dt
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt
    period+=0.001
    if b2.pos.x >= tolerence and b2.v.x>0:
        print("the period of the SHM =",period)
        period=0
    t+=0.001


# In[ ]:




