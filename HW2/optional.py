#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import*

g=9.8
size=0.25
C_drag=0.9
check=vec(10,10,10)
t=0
tolerance=vec(0,0.0001,0)

scene = canvas(center=vec(0,5,0), width=600, background=vec(255, 252, 208)/255.0)
ball = sphere(radius=size, color=color.red, make_trail=True, trail_radius=size/3)

ball.pos=vec(0,size,0)
ball.v=vec(0,0,0)
dt=0.001
        
oscillation = graph(width=450, align='left')
funct1 = gcurve(graph=oscillation, color=color.blue, width=4)


while mag(ball.v)>mag(check)+mag(tolerance) or mag(ball.v)<mag(check)-mag(tolerance):
    rate(1000)
    check=ball.v
    ball.v += vec(0,-g,0)*dt-C_drag*ball.v*dt
    ball.pos += ball.v*dt
    funct1.plot(pos=(t,mag(ball.v)))
    t+=0.001
    
print("the terminal speed = ",str(mag(check)))


# In[ ]:




