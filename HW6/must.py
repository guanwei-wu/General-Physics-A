#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vpython import *
import numpy as np
from histogram import *

# parameters
N = 200
m, size = 4e-3/6e+23, 31e-12*10
L = ((24.4e-3/(6e+23))*N)**(1/3) / 2 + size
k, T = 1.38e-23, 298.0    # Boltzmann constant and initial temperature
t, dt = 0, 3e-13
vrms = (2*k*1.5*T/m)**0.5 # initial root mean square velocity
gamma = 5/3
atoms = []                # list to store atoms

# histogram setting
deltav = 50.0
vdist = graph(x=800, y=0, ymax=N*deltav/1000, width=500, height=300, xtitle='v', ytitle='dN', align='left')
theory_low_T = gcurve(color=color.cyan)
theory_high_T = gcurve(color=color.green)
dv = 10
for v in arange(0., 4201.+dv, dv): # Maxwell-Boltzmann distribution
    theory_low_T.plot(pos=(v, deltav/dv*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*(v**2)*dv))

obs_1 = ghistogram(graph=vdist, bins=arange(0.,4200,deltav), color=color.red)
obs_2 = ghistogram(graph=vdist, bins=arange(0.,4200,deltav), color=color.blue)

# initialization
scene = canvas(width=500, height=500, background=vector(0.2,0.2,0), align='left')
container = box(length=2*L, height=2*L, width=2*L, opacity=0.2, color=color.yellow)
container.v = 0
p_a, v_a = np.zeros((N,3)), np.zeros((N,3))

for i in range(N):
    p_a[i] = [2 * L*random() - L, 2 * L*random() - L, 2 * L*random() - L]
    if i== N-1:
        atom = sphere(pos=vector(p_a[i, 0], p_a[i, 1], p_a[i, 2]), radius=size, color=color.yellow, make_trail=True, retain=50)
    else:
        atom = sphere(pos=vector(p_a[i, 0], p_a[i, 1], p_a[i, 2]), radius=size, color=vector(random(), random(), random()))
    
    ra = pi*random()
    rb = 2*pi*random()
    v_a[i] = [vrms*sin(ra)*cos(rb), vrms*sin(ra)*sin(rb), vrms*cos(ra)]
    atoms.append(atom)

# The function for handling velocity after collisions between two atoms
def vcollision(a1p, a2p, a1v, a2v):
    v1prime = a1v - (a1p - a2p) * sum((a1v-a2v)*(a1p-a2p)) / sum((a1p-a2p)**2)
    v2prime = a2v - (a2p - a1p) * sum((a2v-a1v)*(a2p-a1p)) / sum((a2p-a1p)**2)
    return v1prime, v2prime

stage = 0
plot = 0
wall_v = L / (20000.0*dt)

def keyinput(evt): #keyboard callback function
    global stage, plot
    if evt.key == 'n':
        stage += 1
    if stage == 1:
        container.v = wall_v
        plot += 1
    elif stage == 2:
        container.v = 0
    elif stage == 3:
        container.length = 2*L
scene.bind('keydown', keyinput)

from decimal import Decimal, getcontext
getcontext().prec = 30
Decimal(1) / Decimal(7)

# main program
P_sum = 0
t, n = 0, 1

while True:
    t += dt

    # Calculate the new positions of all the atoms and renew them
    p_a += v_a*dt
    for i in range(N):
        atoms[i].pos = vector(p_a[i, 0], p_a[i, 1], p_a[i, 2])

    if stage == 0:
        obs_1.plot( data=np.sqrt(np.sum(np.square(v_a),-1)) )
    elif stage >= 2:
        obs_2.plot( data=np.sqrt(np.sum(np.square(v_a),-1)) )

    # stage 1
    if stage == 1:
        container.length -= wall_v*dt
        if container.length <= L:
            container.v = 0
            stage += 1
            
    ### Find collisions between pairs of atoms, and handle their collisions
    r_array = p_a - p_a[:, np.newaxis]
    rmag = np.sqrt(np.sum(np.square(r_array),-1))
    hit = np.less_equal(rmag,2*size) - np.identity(N)
    hitlist = np.sort(np.nonzero(hit.flat)[0]).tolist()
    for ij in hitlist:
        i, j = divmod(ij,N)
        hitlist.remove(j*N+i)
        if sum((p_a[i]-p_a[j])*(v_a[i]-v_a[j])) < 0 :
            v_a[i], v_a[j] = vcollision(p_a[i], p_a[j], v_a[i], v_a[j])

    # Find collisions between the atoms and the walls, and handle their collisions
    for i in range(N):
        if abs(p_a[i][0]) >= container.length/2 - size and p_a[i][0]*v_a[i][0] > 0 :
            v_a[i][0] = (abs(v_a[i][0]) + container.v) * -v_a[i][0] / abs(v_a[i][0])
            P_sum += 2*m*abs(v_a[i][0])
        if abs(p_a[i][1]) >= L - size and p_a[i][1]*v_a[i][1] > 0 :
            v_a[i][1] = - v_a[i][1]
            P_sum += 2*m*abs(v_a[i][1])
        if abs(p_a[i][2]) >= L - size and p_a[i][2]*v_a[i][2] > 0 :
            v_a[i][2] = - v_a[i][2]
            P_sum += 2*m*abs(v_a[i][2])

    if t / (1000*dt) > n:
        n += 1
        total_K = 0
        for i in range(N):
            total_K += 0.5 * m * v_a[i].dot(v_a[i])
        T = total_K / (1.5*N*k)
        P = P_sum/(1000*dt)/(2*(container.length*container.width + container.width*container.height + container.height*container.length))
        P_sum = 0
        V = container.length*container.width*container.height
        PV = P * V
        PVG = P * (V**gamma)
        NkT = N * k * T
        print('T=%.3f,P=%.3f,V=%.3E,PV=%.3E,NkT=%E,PV**(5/3)=%.3E' % (T, P, V, P*V, NkT, PVG))

    if plot == 1 and stage == 2:
        V = container.length * container.width * container.height
        for v in arange(0.,4201.+dv,dv): # new distribution
            theory_high_T.plot( pos=(v, (deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*(v**2)*dv) )
        plot += 1

