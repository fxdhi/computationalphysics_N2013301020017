# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 16:52:58 2016

@author: fxdhi
"""

import matplotlib.pyplot as pl
import math
g=9.8
B2m=0.00004
a=0.0065
T0=300
Alpha=2.5
dt=0.01
class cannon_trajectory:
    """
    show the trajectory of cannon
    """
    def __init__(self,x0,y0,v0,theta):
        """p is the angle"""
        self.x0=x0
        self.y0=y0
        self.v0=v0
        self.theta=theta
        p=self.theta*math.pi/180
        self.vx0=self.v0*math.cos(p)
        self.vy0=self.v0*math.sin(p)
    
    def F_drag(self,v_x,v_y,y=1):
        v=math.sqrt(v_x**2+v_y**2)
        self.Fx=-B2m*v_x*v*(1-a*y/T0)**Alpha
        self.Fy=-B2m*v_y*v*(1-a*y/T0)**Alpha
        return self.Fx,self.Fy

    def calculate(self):
        self.x=[self.x0]
        self.y=[self.y0]
        self.vx=[self.vx0]
        self.vy=[self.vy0]
        self.t=[0]
        while not(self.y[-1]<0):
            
            next_vx=self.vx[-1]-self.F_drag(self.vx[-1],self.vy[-1],self.y[-1])[0]*dt
            next_vy=self.vy[-1]-g*dt-self.F_drag(self.vx[-1],self.vy[-1])[1]*dt
            self.vx.append(next_vx)
            self.vy.append(next_vy)
            next_x=self.x[-1]+next_vx*dt 
            next_y=self.y[-1]+next_vy*dt
            self.x.append(next_x)
            self.y.append(next_y)
            
        r=-self.y[-2]/self.y[-1]
        self.x[-1]=(self.x[-2]+r*self.x[-1])/(r+1)
        self.y[-1]=0
    def plot(self,color):
        pl.title("cannon_trajectory")
        pl.xlabel("x/Km")
        pl.ylabel("y/Km")
        pl.plot(self.x,self.y,color,label="$v0=%dm/s$,$\\theta=%d\degree$"%(self.v0,self.theta))
        
        
        
    
        
A=cannon_trajectory(0,0,500,5)
A.calculate()
A.plot("red")
A=cannon_trajectory(0,0,500,10)
A.calculate()
A.plot("blue")
A=cannon_trajectory(0,0,500,15)
A.calculate()
A.plot("yellow")
A=cannon_trajectory(0,0,500,20)
A.calculate()
A.plot("pink")
A=cannon_trajectory(0,0,500,25)
A.calculate()
A.plot("purple")
A=cannon_trajectory(0,0,500,30)
A.calculate()
A.plot("black")
A=cannon_trajectory(0,0,500,35)
A.calculate()
A.plot("green")
A=cannon_trajectory(0,0,500,40)
A.calculate()
A.plot("orange")
A=cannon_trajectory(0,0,500,45)
A.calculate()
A.plot("brown")
A=cannon_trajectory(0,0,500,50)
A.calculate()
A.plot("gray")
A=cannon_trajectory(0,0,500,55)
A.calculate()
A.plot("cyan")
pl.legend(loc='upper right', frameon=False)
pl.show()


        
        
        
