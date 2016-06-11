# -*- coding: utf-8 -*-
"""
Created on Tue Jun 07 20:53:34 2016

@author: fxdhi
"""
import pylab as pl
import numpy as np
x=0
y=0
t=0
c=[0]
d=[0]
m=[0]
for i in range(1,100000):
    a=np.random.uniform(0,1)
    b=np.random.uniform(0,1)
    if a<=0.5:
        x=x-1
    else:
        x=x+1
    if b<=0.5:
        y=y-1
    else:
        y=y+1

        
    t=t+1
    c.append(x)
    m.append(t)
    d.append(y)
    


pl.scatter(c,d,s=1)


pl.grid(True)
pl.show()


