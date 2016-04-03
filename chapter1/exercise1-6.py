# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:33:24 2016

@author: fxdhi
"""

from pylab import *
import visual as vs
import easygui
N_O=20
N=[]
t=[]
a=0
b=0
dt=0
n=0

def population(N,t,_a,_b,_dt,_n):
    global a,b,dt,n,time,N_O
    
    print "a:"
    a=float(raw_input())
    print "b:"
    b=float(raw_input())
    print "dt:"
    dt=float(raw_input())
    print "end time:"
    t.append(0)
    time=float(raw_input())
    n=int(time/dt)
    return 0
def calculate(N,t,a,b,dt,n):
    
    print t
    print a
    print b
    print dt
    print n
    N.append(N_O)
    for i in range(1,n):
        N.append(N[i-1]+(a*N[i-1]-b*(N[i-1])**2)*dt)
        t.append(t[i-1]+dt)
    return 0
def plot3D():
    axis_length=10.0
    vs.xaxis=vs.arrow(pos=(-5,-5,0),axis=(axis_length,0,0),shaftwidth=0.05)
    vs.yaxis=vs.arrow(pos=(-5, -5, 0), axis=(0, axis_length, 0), shaftwidth=0.05)
    balls=[]
    for (i,j) in zip(N,t):
        balls.append(vs.sphere(pos=(((j/time)*axis_length*0.9-4.9,(i/N_O)*axis_length*0.9-4.9,0)),radius=0.2,color=vs.color.red))
    vs.xlabel = vs.label(text = "time", pos = (5, -5, 0))
    vs.ylabel = vs.label(text = "Number of people", pos = (-5,5,0))
def set_up():
    easygui.enterbox("How many people at the beginning?")
    

    
set_up()    
population(N,t,a,b,dt,n)
calculate(N,t,a,b,dt,n)
plot(t,N,label="$N(t)$",color="red")
xlim(0,20)
legend()
title("exercise1-6")
xlabel("Time(year)")
ylabel("poplation")
show()
plot3D()
