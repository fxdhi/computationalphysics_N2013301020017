# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:07:23 2016

@author: fxdhi
"""

import pylab as pl
k=1

class harmonic():
    def __init__(self,_alpha=0,_x0=0,_v0=0,_dt=0,_time=0):
        self.alpha=_alpha
        self.x0=_x0
        self.v0=_v0
        self.dt=_dt
        self.time=_time
        
            
    def calculate(self):
        global k
        self.x=[]
        self.v=[]
        self.t=[]        
        self.x.append(self.x0)
        self.v.append(self.v0)
        self.t.append(0)
        nsteps=int(self.time/self.dt)
        for i in range(1, nsteps):
            self.v.append(self.v[i - 1]-k*self.x[i-1]**self.alpha*self.dt)
            self.x.append(self.x[i - 1]+self.v[i]*self.dt)
            self.t.append(self.t[i - 1] + self.dt)
        return 0
        
       
    def plot2D(self,color):
        pl.plot(self.t, self.x,color,label="$v0=%dm/s$,$\\alpha=%d$"%(self.v0,self.alpha))
        pl.title("motion state")
        pl.xlabel("time(/s)")
        pl.ylabel("x")
        
        
a = harmonic(1, 1, 10,0.1,20)
a.calculate()
a.plot2D("red")
b = harmonic(1, 1, 20,0.1,20)
b.calculate()
b.plot2D("green")
c = harmonic(1, 1, 30,0.1,20)
c.calculate()
c.plot2D("cyan")
pl.legend()
pl.show()
A = harmonic(3, 2, 10,0.01,20)
A.calculate()
A.plot2D("red")
B = harmonic(3, 2, 20,0.01,20)
B.calculate()
B.plot2D("blue")
C = harmonic(3, 2, 0,0.01,20)
C.calculate()
C.plot2D("purple")
pl.legend()
pl.show()
