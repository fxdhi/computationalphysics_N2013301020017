# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 15:54:14 2016

@author: fxdhi
"""

import random
import pylab as pl

x=0
x2ave=0
t=0
k=[0]
h=[0]
dk=1
c=[0]
p=[0]
m=[0]
cm=[0]
for i in range(1,500):
    a=random.uniform(0,1)
    if a<0.25:
        x=x-1
    else:
        x=x+1
    t=t+1
    h.append(h[i-1]+1*dk)
    k.append(k[i-1]+dk)
    m.append(t)
    p.append(x)
    x2ave=x2ave+x**2
    c.append(x2ave)
    cm.append(round(x2ave,2)/i+1)
    #print c,m,cm
pl.scatter(m,p,s=1)
pl.title("Random walk in one dimension")
pl.xlabel("step number")
pl.ylabel("y")
#pl.ylim(-50,50)

pl.show()

pl.scatter(m,cm,s=1)
pl.plot(k,h)
pl.title("random walk in one dimension")
pl.xlabel("step number")
pl.ylabel("<$x^2$>")
pl.show()
 
    
        
    