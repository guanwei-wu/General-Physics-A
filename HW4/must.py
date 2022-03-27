#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import *
size, m = 0.02, 0.2
L, k = 0.2, 20
amplitude = 0.03

'''
scene = canvas(width=600, height=400, fov=0.03, align='left', center=vec(0.3, 0, 0), background=vec(0.5, 0.5, 0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue) # left wall
ball = sphere(radius=size, color=color.red)                            # ball
spring = helix(radius=0.015, thickness=0.01)

oscillation = graph(width=400, align='left', xtitle='t', ytitle='x', background=vec(0.5, 0.5, 0))
x = gcurve(color=color.red, graph=oscillation)

oscillation2 = graph(width=400, align='left', xtitle='t', ytitle='ave_power', background=vec(0.5, 0.5, 0))
p = gdots(color=color.cyan, graph=oscillation2)
'''

oscillation3 = graph(width=400, align='left', xtitle='omega', ytitle='ave_power', background=vec(0.5, 0.5, 0))
ans = gcurve(color=color.blue, graph=oscillation3)


omega = [0.1*i + 0.7*sqrt(k/m) for i in range(1, int(0.5*sqrt(k/m)/0.1))]
for omega_d in omega:
    b = 0.05 * m * omega_d
    T = 2*pi / omega_d

    class obj:pass
    wall_left, ball, spring = obj(), obj(), obj()

    ball.pos = vector(L, 0 , 0)
    ball.v = vector(0, 0, 0)
    ball.m = m
    spring.pos = vector(0, 0, 0)
    t, dt, n= 0, 0.001,1
    work = 0
    check = 0

    while True:
        #rate(1000)
        spring.axis = ball.pos - spring.pos
        spring_force = vec(0.1 * sin(omega_d*t), 0, 0) - k * (mag(spring.axis) - L) * norm(spring.axis) -b * ball.v
        ball.a = spring_force / ball.m
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
        #x.plot(pos=(t,ball.pos.x - L))
        work+=dot(vec(0.1 * sin(omega_d*t), 0, 0),ball.v)*dt
        
        if t / T >n:
            #p.plot(pos=(t,work/T))
            if (int)(100000*work/T - 100000*check)==0:
                ans.plot(pos=(omega_d,work/T))
                break
            if (int)(100000*work/T - 100000*check)!=0:
                check = work/T
            n+=1
            work=0


# In[ ]:




