#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import*

g=9.8
size=0.25
C_drag=0.9
count=0
count_a=0
displacement = vec(0, 0, 0)
t=0

scene = canvas(center=vec(0,5,0), width=600, background=vec(255, 252, 208)/255.0)
floor = box(length=30, height=0.01, width=4, color=color.blue)
ball = sphere(radius=size, color=color.red, make_trail=True, trail_radius=size/3)

ball.pos=vec(-15,size,0)
ball.v=vec(20*cos(pi/4), 20*sin(pi/4), 0)
dt=0.001
        
oscillation = graph(width=450, align='left')
funct1 = gcurve(graph=oscillation, color=color.blue, width=4)


while ball.pos.x < 0.5 and count<3:
    rate(1000)
    ball.v += vec(0,-g,0)*dt-C_drag*ball.v*dt
    ball.pos += ball.v*dt
    funct1.plot(pos=(t,mag(ball.v)))
    t+=0.001
    while count_a<1 and ball.v.y<=0.001:
        msg = text(text='the highest point ='+str(ball.pos.y), pos=vec(-10,-6,0))
        count_a+=1
    if ball.pos.y <= size and ball.v.y < 0:
        ball.v.y = -ball.v.y
        count+=1

displacement = vec(ball.pos)-vec(-15,5,0)
msg = text(text='the displacement ='+str(mag(displacement)), pos=vec(-10,-8,0))


# In[ ]:




