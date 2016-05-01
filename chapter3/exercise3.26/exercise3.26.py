# -*- coding: utf-8 -*-
"""
Created on Sun May 01 12:55:36 2016

@author: fxdhi
"""

import matplotlib.pyplot as pl


sigma=10
b=float(8.0/3)

class lorenz_model():
    def __init__(self,_x0=0,_y0=0,_z0=0,_r=0,_dt=0,_time=0):
        self.x0=_x0
        self.y0=_y0
        self.z0=_z0
        self.dt=_dt
        self.time=_time
        self.r=_r
        
    def calculate(self):
        sigma=10
        b=float(8.0/3)
        self.x=[]
        self.y=[]
        self.z=[]
        self.t=[]
        self.x.append(self.x0)
        self.y.append(self.y0)
        self.z.append(self.z0)
        self.t.append(0)
        nsteps=int(self.time/self.dt)
        for i in range(1,nsteps):
            self.x.append(self.x[i-1]+sigma*(self.y[i-1]-self.x[i-1])*self.dt)
            self.y.append(self.y[i-1]-(self.x[i-1]*self.z[i-1]-self.r*self.x[i-1]+self.y[i-1])*self.dt)
            self.z.append(self.z[i-1]+(self.x[i-1]*self.y[i-1]-b*self.z[i-1])*self.dt)
            self.t.append(self.t[i-1]+self.dt)
        
        return 0
    def calculate_1(self):
        self.a=[]
        self.c=[]
        nsteps=int(self.time/self.dt)     
        for i in range(300000,nsteps):
            if -0.001<=self.x[i]<=0.001:
                self.a.append(self.y[i])
                self.c.append(self.z[i])
        return 0        
    def calculate_2(self):
        self.e=[]
        self.f=[]
        nsteps=int(self.time/self.dt)
        for i in range (300000,nsteps):        
                if -0.001<=self.y[i]<=0.001:
                    self.e.append(self.x[i])
                    self.f.append(self.z[i])
        return 0
    def plot_time(self,color):
        pl.plot(self.t,self.x,color,label="r=%r"%(self.r))
        pl.title("Lorenz model z versus time")
        pl.xlabel("Time(s)")
        pl.ylabel("z")
    def plot_phase1(self):
        pl.plot(self.x,self.z,label="r=%r"%(self.r))
        pl.title("Phase space plot:z versus x")
        pl.xlabel("x")
        pl.ylabel("z")
    def plot_phase2(self,color):
        pl.plot(self.y,self.z,color)
        pl.title("Phase space plot:z versus y")
        pl.xlabel("y")
        pl.ylabel("z")
    def plot_1(self):
        pl.scatter(self.a,self.c,s=1,label="r=%r"%(self.r))
        pl.title("Phase space plot:z versus y whenx=0")
        pl.xlabel("y")
        pl.ylabel("z")
    def plot_2(self):
        pl.scatter(self.e,self.f,s=1,label="r=%r"%(self.r))
        pl.title("Phase space plot:z versus x wheny=0")
        pl.xlabel("x")
        pl.ylabel("z")
    


A= lorenz_model(1,0,0,5,0.0001,50)
A.calculate()
A.plot_time("blue")
A= lorenz_model(1,0,0,10,0.0001,50)
A.calculate()
A.plot_time("red")
A= lorenz_model(1,0,0,25,0.01,50)
A.calculate()
A.plot_time("black")
pl.legend()
pl.show()
   

A= lorenz_model(1,0,0,5,0.0001,50)
A.calculate()
A.plot_phase1()
pl.legend()
pl.show()
A= lorenz_model(1,0,0,10,0.0001,50)
A.calculate()
A.plot_phase1()
pl.legend()
pl.show()
A= lorenz_model(1,0,0,25,0.0001,50)
A.calculate()
A.plot_phase1()
pl.legend()
pl.show()


A= lorenz_model(1,0,0,25,0.0001,2000)
A.calculate()
A.calculate_1()
A.plot_1()
A.calculate_2()
A.plot_2()
pl.legend()
pl.show()



            
            