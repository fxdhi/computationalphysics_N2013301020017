# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:16:18 2016

@author: fxdhi
"""

from math import *
import pylab as pl

u0I=1


class coils():
    def __init__(self,_r=0,_z0=0,_Bz0=0,_dz=0,_zt=0):
        self.dz=_dz
        self.r=_r
        self.z0=_z0
        self.Bz0=_Bz0
        self.zt=_zt
        
    
    def calculate(self):
        self.z=[]
        self.Bz=[]
        self.z.append(self.z0)
        self.Bz.append(self.Bz0)
        nsteps=int(self.zt/self.dz)
        for i in range(1,nsteps):
            self.z.append(self.z[i-1]+self.dz)
            self.Bz.append(0.5*self.r**2*(1/(self.r**2+(0.5*self.r+self.z[i])**2)**1.5+1/(self.r**2+(-0.5*self.r+self.z[i])**2)**1.5))
                       
        return 0
    def plot(self):
            pl.scatter(self.z,self.Bz,s=0.5)
            pl.title("Helmholtz_coils")
            pl.xlabel("z")
            pl.ylabel("B_z")
            pl.show()
            
A=coils(1,-4,0.031,0.0001,8)
A.calculate()
A.plot()

        
    
    
        
    
    
