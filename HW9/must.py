#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import *

fd = 120                # 120 Hz
# ===== Add your parameters here =====
R = 30
L = 0.2
C = 0.00002
T = 1/fd
XL = 2*pi*fd*L
XC = -1/(2*pi*fd*C)

t = 0
dt = 1.0 / (fd*5000)    # 5000 simulation points per cycle

VR = VL = VC = 0
Q = 0

scene1 = graph(align='left', xtitle='t', ytitle='i(A) blue, v(100V) red', background=vector(0.6, 0.9, 0.6))
scene2 = graph(align='left', xtitle='t', ytitle='Energy(J)', background=vector(0.6, 0.9, 0.6))

i_t = gcurve(color=color.blue, graph=scene1)
v_t = gcurve(color=color.red, graph=scene1)
E_t = gcurve(color=color.red, graph=scene2)

# ===== Your codes here =====
I = 0
compare_i = 0
compare_v = 0
ti = tv = 0
phase = 0
E12 = 0
counter = 0
index = 0
ans_3 = 0

while t<=20*T:
    rate(5000)
    t+=dt
    
    if t<0:
        V = 0
    elif 0<=t<=12*T:
        V = 36*sin(2*pi*fd*t)
    elif t>12*T:
        V = 0
        
    di = (VL*dt)/L
    I+=di
    Q+=(I*dt)
    VR = I*R
    VC = Q/C
    VL = V-VR-VC
    E = 0.5*(C*VC*VC + L*I*I)
    
    i_t.plot(pos=(t/T, I))
    v_t.plot(pos=(t/T, (V/100)))
    E_t.plot(pos=(t/T, E))
    
    if 8.5*T<t<9.5*T:
        if compare_i<I:
            compare_i  = I
            ti = t
        if compare_v<V:
            compare_v = V
            tv = t
            
    if t>12*T:
        counter+=1
        if E12 == 0:
            E12 = E
        if E<0.1*E12 and index == 0:
            index = 1
            ans_3 = counter*dt
            
theo_i = 36/(complex(R, 0)+complex(0, XL)+complex(0, XC))
theo_phi = atan((XL+XC)/R)

print("- i relative to v -")
print("theoretical values :")
print(abs(theo_i))
print(-theo_phi)
print("simulated values :")
print(compare_i)
print(((tv-ti)/T)*2*pi)
print("the time that the energy decays to 10% of the energy at the time the voltage is just turned off :")
print(ans_3)


# In[ ]:




