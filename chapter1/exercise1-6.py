# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:33:24 2016

@author: fxdhi
"""

from matplotlib.pylab import *
N=[]
t=[]
a=0
b=0
dt=0
n=0

def population(N,t,_a,_b,_dt,_n):
    global a,b,dt,n
    print "initial number of the people:"
    N.append(float(raw_input()))
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
    print N
    print t
    print a
    print b
    print dt
    print n
    for i in range(1,n):
        N.append(N[i-1]+(a*N[i-1]-b*(N[i-1])**2)*dt)
        t.append(t[i-1]+dt)
    return 0
population(N,t,a,b,dt,n)
calculate(N,t,a,b,dt,n)
plot(t,N,label="$N(t)$",color="red")
xlim(0,20)
legend()
title("exercise1-6")
xlabel("Time(year)")
ylabel("poplation")
show()