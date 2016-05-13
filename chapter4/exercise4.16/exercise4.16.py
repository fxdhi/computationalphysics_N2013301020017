# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:17:33 2016

@author: fxdhi
"""

import matplotlib.pyplot as pl
import math


class three_body():
    def __init__(self,_xs0=0,_ys0=0,_xe0=0,_ye0=0,_xj0=0,_yj0=0,_vxs0=0,_vys0=0,_vxe0=0,_vye0=0,_vxj0=0,_vyj0=0,_dt=0,_m1=0,_m2=0,_m3=0,_time=0):
        self.xs0=_xs0
        self.ys0=_ys0
        self.vxs0=_vxs0
        self.vys0=_vys0
        self.xe0=_xe0
        self.ye0=_ye0
        self.vxe0=_vxe0
        self.vye0=_vye0
        self.xj0=_xj0
        self.yj0=_yj0
        self.vxj0=_vxj0
        self.vyj0=_vyj0        
        self.dt=_dt
        self.m1=_m1
        self.m2=_m2
        self.m3=_m3
        self.time=_time
    
    def calculate(self):
        self.xs=[]        
        self.xe=[]
        self.xj=[]
        self.ys=[]
        self.ye=[]
        self.yj=[]
        self.vxs=[]
        self.vxe=[]
        self.vxj=[]
        self.vys=[]
        self.vye=[]
        self.vyj=[]
        self.rse=[]
        self.rej=[]
        self.rjs=[]
        self.t=[]
        self.xs.append(self.xs0)
        self.ys.append(self.ys0)
        self.vxs.append(self.vxs0)
        self.vys.append(self.vys0)
        self.xe.append(self.xe0)
        self.ye.append(self.ye0)
        self.vxe.append(self.vxe0)
        self.vye.append(self.vye0)
        self.xj.append(self.xj0)
        self.yj.append(self.yj0)
        self.vxj.append(self.vxj0)
        self.vyj.append(self.vyj0)
        self.rse.append(math.sqrt((self.xs0-self.xe0)**2+(self.ys0-self.ye0)**2))
        self.rjs.append(math.sqrt((self.xj0-self.xs0)**2+(self.yj0-self.ys0)**2))
        self.rej.append(math.sqrt((self.xe0-self.xj0)**2+(self.ye0-self.yj0)**2))
        self.t.append(0)
        nsteps=int(self.time/self.dt)
        for i in range(1,nsteps):
            self.vxs.append(self.vxs[i-1]-(4*(math.pi)**2)*self.m2/self.m1*((self.xs[i-1]-self.xe[i-1])/(self.rse[i-1])**3)*self.dt-(4*(math.pi)**2)*self.m3/self.m1*(self.xs[i-1]-self.xj[i-1])/self.rjs[i-1]**3*self.dt)
            self.xs.append(self.xs[i-1]+self.vxs[i]*self.dt)
            self.vys.append(self.vys[i-1]-(4*(math.pi)**2)*self.m2/self.m1*((self.ys[i-1]-self.ye[i-1])/(self.rse[i-1])**3)*self.dt-(4*(math.pi)**2)*self.m3/self.m1*(self.ys[i-1]-self.yj[i-1])/self.rjs[i-1]**3*self.dt)
            self.ys.append(self.ys[i-1]+self.vys[i]*self.dt)        
            self.vxe.append(self.vxe[i-1]-(4*(math.pi)**2)*((self.xe[i-1]-self.xs[i-1])/(self.rse[i-1])**3)*self.dt-(4*(math.pi)**2)*self.m3/self.m1*(self.xe[i-1]-self.xj[i-1])/self.rej[i-1]**3*self.dt)
            self.xe.append(self.xe[i-1]+self.vxe[i]*self.dt)
            self.vye.append(self.vye[i-1]-(4*(math.pi)**2)*((self.ye[i-1]-self.ys[i-1])/(self.rse[i-1])**3)*self.dt-(4*(math.pi)**2)*self.m3/self.m1*(self.ye[i-1]-self.yj[i-1])/self.rej[i-1]**3*self.dt)
            self.ye.append(self.ye[i-1]+self.vye[i]*self.dt)
            self.vxj.append(self.vxj[i-1]-(4*(math.pi)**2)*((self.xj[i-1]-self.xs[i-1])/(self.rjs[i-1])**3)*self.dt-(4*(math.pi)**2)*self.m2/self.m1*(self.xj[i-1]-self.xe[i-1])/self.rej[i-1]**3*self.dt)
            self.xj.append(self.xj[i-1]+self.vxj[i]*self.dt)
            self.vyj.append(self.vyj[i-1]-(4*(math.pi)**2)*((self.xj[i-1]-self.xs[i-1])/(self.rjs[i-1])**3)*self.dt-(4*(math.pi)**2)*self.m2/self.m1*(self.yj[i-1]-self.yj[i-1])/self.rej[i-1]**3*self.dt)
            self.yj.append(self.yj[i-1]+self.vyj[i]*self.dt)
            self.rse.append(math.sqrt((self.xs[i]-self.xe[i])**2+(self.ys[i]-self.ye[i])**2))
            self.rjs.append(math.sqrt((self.xj[i]-self.xs[i])**2+(self.yj[i]-self.ys[i])**2))
            self.rej.append(math.sqrt((self.xe[i]-self.xj[i])**2+(self.ye[i]-self.yj[i])**2))
            self.t.append(self.t[i-1]+self.dt)
        return 0
    def plot1(self):
        pl.scatter(self.xs,self.ys,color="red",label="solar",s=1)        
        pl.scatter(self.xe,self.ye,color="blue",label="earth",s=1)
        pl.scatter(self.xj,self.yj,color="yellow",label="jupiter",s=1)
        pl.title("3-body simulation")
        pl.xlabel("x")
        pl.ylabel("y")
    
A=three_body(-4.93e-3,0,1-4.93e-3,0,5.2-4.93e-3,0,0,-8.4e-4*math.pi,0,2*math.pi,0,0.878*math.pi,0.002,2e6,6,1900,8)
A.calculate()
A.plot1()
pl.legend()
pl.show()
A=three_body(-0.0489,0,1-0.0489,0,5.2-0.0489,0,0,-8.3e-3*math.pi,0,2*math.pi,0,0.878*math.pi,0.002,2e6,6,19000,8)
A.calculate()
A.plot1()
pl.legend()
pl.show()
A=three_body(-0.45,0,0.55,0,4.75,0,0,-0.083*math.pi,0,2*math.pi,0,0.878*math.pi,0.002,2e6,6,190000,8)
A.calculate()
A.plot1()
pl.legend()
pl.show()
A=three_body(-2.53,0,-1.53,0,2.67,0,0,-0.83*math.pi,0,2*math.pi,0,0.878*math.pi,0.002,2e6,6,1900000,50)
A.calculate()
A.plot1()
pl.legend()
pl.show()
   