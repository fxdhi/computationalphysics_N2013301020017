# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:50:58 2016

@author: fxdhi
"""

import matplotlib.pyplot as pl
import math
q=0.5
l=9.8
g=9.8
omega_d=float(2.0/3)


class nonlinear_pendulum():
    def __init__(self,_omega0=0,_theta0=0,_dt=0,_time=0,_Fd=0):
        self.omega0=_omega0
        self.theta0=_theta0
        self.dt=_dt
        self.time=_time
        self.Fd=_Fd
        
    def calculate(self):
        q=0.5
        l=9.8
        g=9.8
        omega_d=float(2.0/3)
        self.omega=[]
        self.theta=[]
        self.t=[]
        self.omega.append(self.omega0)
        self.theta.append(self.theta0)
        self.t.append(0)
        nsteps=int(self.time/self.dt)
        for i in range(1,nsteps):
            self.omega.append(self.omega[i-1]+(-g/l*math.sin(self.theta[i-1])-q*self.omega[i-1]+self.Fd*math.sin(omega_d*self.t[i-1]))*self.dt)
            self.theta.append(self.theta[i-1]+self.omega[i]*self.dt)
            self.t.append(self.t[i-1]+self.dt)
            if self.theta[i]<-math.pi:
                self.theta[i]=self.theta[i]+2*math.pi
            if self.theta[i]>math.pi:
                self.theta[i]=self.theta[i]-2*math.pi
        #print self.theta
        return 0
    def calculate_1(self):
        self.a=[]
        self.b=[]
        self.a.append(self.omega0)
        self.b.append(self.theta0)
        nsteps=int(self.time/self.dt)
        i=0        
        while i<nsteps:
            self.a.append(self.omega[i])
            self.b.append(self.theta[i])
            i=i+400
        return 0
           
           
            

        
    def plot_2D(self,color):
        pl.plot(self.t,self.theta,color,label="Fd=%r"%(self.Fd))
        pl.title("nonlinear pendulum")
        pl.xlabel("time(/s)")
        pl.ylabel("angle")
    def plot_phase(self,color):
        global nsteps
        pl.title("phase space")
        pl.xlabel("$\\theta$(radians)")
        pl.ylabel("$\\omega$(radians/s)")
        pl.scatter(self.theta,self.omega,s=1,label='Fd=%r'%(self.Fd))
    def plot_attractor(self):
        pl.scatter(self.b,self.a,s=2,label='$t=0.375n\\pi$')
        pl.title("phase space")
        pl.xlabel("$\\theta$(radians)")
        pl.ylabel("$\\omega$(radians/s)")


a=nonlinear_pendulum(0,0.2,0.04,60,0)
a.calculate()
a.plot_2D("red")
pl.legend()
pl.show()


a=nonlinear_pendulum(0,0.2,0.04,60,0.5)
a.calculate()
a.plot_2D("blue")
pl.legend()
pl.show()


a=nonlinear_pendulum(0,0.2,0.04,60,1.2)
a.calculate()
a.plot_2D("cyan")
pl.legend()
pl.show()


b=nonlinear_pendulum(0,0.2,0.04,60,0.5)
b.calculate()
b.plot_phase("blue")
pl.legend()
pl.show()

b=nonlinear_pendulum(0,0.2,0.04,60,1.2)
b.calculate()
b.plot_phase("blue")
pl.legend()
pl.show()


b=nonlinear_pendulum(0,0.2,3*math.pi/800,20000*math.pi,1.2)
b.calculate()
b.calculate_1()
b.plot_attractor()
pl.legend()
pl.show()

b=nonlinear_pendulum(0,0.2,0.75*math.pi/800,20000*math.pi,1.2)
b.calculate()
b.calculate_1()
b.plot_attractor()
pl.legend()
pl.show()

b=nonlinear_pendulum(0,0.2,0.375*math.pi/400,10000*math.pi,1.2)
b.calculate()
b.calculate_1()
b.plot_attractor()
pl.legend()
pl.show()         