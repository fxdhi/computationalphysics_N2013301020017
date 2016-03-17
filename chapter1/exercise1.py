#coding:utf-8
import matplotlib.pyplot as plt
v_m=[]
t=[]
a=0
b=0
dt=0
n=0

def initialize(v_m,t,_a,_b,_dt,_n):
    global a,b,dt,n
    print "initial number of velocity->",
    v_m.append(float(raw_input()))
    print "Gravitational acceleration ->",
    a=float(raw_input())
    print "frictional force factor->",
    b=float(raw_input())
    print "time step->",
    dt=float(raw_input())
    print "total time->",
    time=float(raw_input())
    t.append(0)
    n=int(time/dt)
    return 0
def calculate(v_m,t,a,b,dt,n):
    print v_m
    print t
    print a
    print b
    print dt
    print n
    for i in range(1,n):
        v_m.append(v_m[i-1]+(a-b*v_m[i-1])*dt)
        t.append(t[i-1]+dt)
    return 0

initialize(v_m,t,a,b,dt,n)
calculate(v_m,t,a,b,dt,n)

plt.plot(t,v_m,"--*",label="$v(t)$",color="red")
plt.ylim(0,20)
plt.xlim(0,20)
plt.legend()
plt.title("exercise1-3")
plt.grid(True)
plt.xlabel("Time(s)")
plt.ylabel("Velocity(m/s)")
#scatter(t,v_m)
plt.show()
