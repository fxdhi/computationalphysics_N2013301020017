# -*- coding: utf-8 -*-
"""
Created on Sat May 07 16:03:00 2016

@author: fxdhi
"""

import matplotlib.pyplot as pl
import math


class planet():
    def __init__(self,_x0=0,_y0=0,_vx0=0,_vy0=0,_dt=0,_m1=0,_m2=0,_time=0):
        self.x0=_x0
        self.y0=_y0
        self.vx0=_vx0
        self.vy0=_vy0
        self.dt=_dt
        self.m1=_m1
        self.m2=_m2
        self.time=_time
    
    def calculate(self):
        self.x=[]
        self.y=[]
        self.vx=[]
        self.vy=[]        
        self.r=[]
        self.t=[]
        self.x.append(self.x0)
        self.y.append(self.y0)
        self.vx.append(self.vx0)
        self.vy.append(self.vy0)
        self.r.append(math.sqrt(self.x0**2+self.y0**2))
        self.t.append(0)
        nsteps=int(self.time/self.dt)
        for i in range(1,nsteps):
            self.vx.append(self.vx[i-1]-((self.m1+self.m2)*self.m1/self.m2**2)*(4*(math.pi)**2)*(self.x[i-1]/(self.r[i-1])**3)*self.dt)
            self.x.append(self.x[i-1]+self.vx[i]*self.dt)
            self.vy.append(self.vy[i-1]-((self.m1+self.m2)*self.m1/self.m2**2)*(4*(math.pi)**2)*self.y[i-1]/self.r[i-1]**3*self.dt)
            self.y.append(self.y[i-1]+self.vy[i]*self.dt)
            self.r.append(math.sqrt(self.x[i]**2+self.y[i]**2))
            self.t.append(self.t[i-1]+self.dt)
        return 0
    def plot(self,color):
        pl.plot(self.x,self.y,color)
        pl.title("planet motion")
        pl.xlabel("x(AU)")
        pl.ylabel("y(AU)")

A=planet(1,0,0,2*math.pi,0.002,10,10,1)
A.calculate()
A.plot("blue")
pl.show()
        
