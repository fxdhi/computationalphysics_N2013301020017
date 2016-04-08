# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 10:54:46 2016

@author: fxdhi
"""

import math
import pylab as pl
from visual import *


g=9.8
S0m=0.00041
omega=209
a=0.0039
b=0.0058
c=1
vd=35
deltav=5
class flight_state:
    def __init__(self, _x = 0, _y = 0,_z = 0, _vx = 0, _vy = 0,_vz = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.z = _z
        self.vx = _vx
        self.vy = _vy
        self.vz = _vz
        self.t = _t
class baseball:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0, 0, 0), _dt = 0.01):
        self.baseball_flight_state = []
        self.baseball_flight_state.append(_fs)
        self.dt = _dt
        print self.baseball_flight_state[-1].x, self.baseball_flight_state[-1].y,self.baseball_flight_state[-1].z,self.baseball_flight_state[-1].vx, self.baseball_flight_state[-1].vy,self.baseball_flight_state[-1].vz
    def next_state(self, current_state):
        g=9.8
        S0m=0.00041
        a=0.0039
        b=0.0058
        c=1
        vd=35
        deltav=5
        v=math.sqrt(current_state.x**2+current_state.vy**2+current_state.vz**2)
        B2m=a+b/(c+math.exp((v-vd)/deltav))
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx-B2m*v*current_state.vx*self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        next_z = current_state.z + current_state.vz * self.dt
        next_vz = current_state.vz-S0m*current_state.vx*omega*self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y,next_z, next_vx, next_vy,next_vz, current_state.t + self.dt)
    def shoot(self):
        while not(self.baseball_flight_state[-1].z < 0):
            self.baseball_flight_state.append(self.next_state(self.baseball_flight_state[-1]))
            #print self.baseball_flight_state[-1].x, self.baseball_flight_state[-1].y,self.baseball_flight_state[-1].z, self.baseball_flight_state[-1].vx, self.baseball_flight_state[-1].vy,self.baseball_flight_state[-1].vz

        r = - self.baseball_flight_state[-2].z / self.baseball_flight_state[-1].z
        self.baseball_flight_state[-1].x = (self.baseball_flight_state[-2].x + r * self.baseball_flight_state[-1].x) / (r + 1)
    def show_trajectory(self,color):
        x = []
        y = []
        z=  []
        for fs in self.baseball_flight_state:
            x.append(fs.x)
            y.append(fs.y)
            z.append(fs.z)
        pl.plot(x,z,color,label="$vx=%dm/s$,$vz=%dm/s$,$\omega=209$"%(self.baseball_flight_state[0].vx,self.baseball_flight_state[0].vz))
           
        
a = baseball(flight_state(0,0,0,10,0,2,0), _dt = 0.01)
a.shoot()
a.show_trajectory("red")
b = baseball(flight_state(0,0,0,20,0,2,0), _dt = 0.01)
b.shoot()
b.show_trajectory("blue")
c = baseball(flight_state(0,0,0,25,0,2,0), _dt = 0.01)
c.shoot()
c.show_trajectory("yellow")
d = baseball(flight_state(0,0,0,31,0,2,0), _dt = 0.01)
d.shoot()
d.show_trajectory("cyan")
pl.legend()
pl.show()
e = baseball(flight_state(0,0,0,31,0,2,0), _dt = 0.01)
e.shoot()
e.show_trajectory("orange")
f = baseball(flight_state(0,0,0,31,0,4,0), _dt = 0.01)
f.shoot()
f.show_trajectory("pink")
g = baseball(flight_state(0,0,0,31,0,6,0), _dt = 0.01)
g.shoot()
g.show_trajectory("green")
h = baseball(flight_state(0,0,0,31,0,8,0), _dt = 0.01)
h.shoot()
h.show_trajectory("violet")
pl.legend()
pl.show()

    
