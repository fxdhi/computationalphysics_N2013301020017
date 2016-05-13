from visual import *

Sun=sphere(pos=(0,0,0),radius=10,color=color.orange,make_trail=true)
earth=sphere(pos=(-200,0,0),radius=10,material=materials.earth,make_trail=true)
jupiter=sphere(pos=(-1000,0,0),radius=10,color=color.yellow,make_trail=true)
Sunv=vector(0,0,0)
earthv=vector(0,5,0)
jupiterv=vector(0,2.2,0)
for i in range (2000):
    rate(1000)
    earth.pos=earth.pos+earthv
    Sun.pos=Sun.pos+Sunv
    jupiter.pos=jupiter.pos+jupiterv
    dist1=((earth.x-Sun.x)**2+(earth.y-Sun.y)**2+(earth.z-Sun.z)**2)**0.5
    dist2=((earth.x-jupiter.x)**2+(earth.y-jupiter.y)**2+(earth.z-jupiter.z)**2)**0.5
    dist3=((Sun.x-jupiter.x)**2+(Sun.y-jupiter.y)**2+(Sun.z-jupiter.z)**2)**0.5
    RadialVector1=(earth.pos-Sun.pos)/dist1
    RadialVector2=(earth.pos-jupiter.pos)/dist2
    RadialVector3=(jupiter.pos-Sun.pos)/dist3
    Fgrav1=-10000*RadialVector1/dist1**2
    Fgrav2=-9.500*RadialVector2/dist2**2
    Fgrav3=0.03*RadialVector1/dist1**2
    Fgrav4=9.500*RadialVector3/dist3**2
    Fgrav5=10000*RadialVector2/dist2**2
    Fgrav6=-0.03*RadialVector3/dist3**2
    
    earthv=earthv+Fgrav1+Fgrav2
    earth.pos+=earthv
    Sunv=Sunv+Fgrav3+Fgrav4
    Sun.pos+=Sunv
    jupiterv=jupiterv+Fgrav5+Fgrav6
    jupiter.pos+=jupiterv
    
    
    
    
