##姓名：周一凡
##学号：2013301020017
exercise4.16
三体运动状况讨论
###背景：
>由于木星质量较大，所以对于地球的万有引力作用不可忽略，考虑由太阳，地球，木星构成的三体运动体系，并在初始时刻，选定三者的质心为原点，并保持体系的总动量为零。并讨论10倍木星质量，100倍木星质量，1000倍木星质量状况下，体系的运动状况。
###正文：
由于太阳在此处已不再为原点，所以需要对原公式做出相应的修正，具体如下:

----
```
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

```
调整参数，正常木星质量：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter4/exercise4.16/exercise4.16.1.png)
可以看出，地球轨道是稳定的，几乎不受影响，但是木星轨道在在这之后产生了极大的偏离。
10倍木星质量：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter4/exercise4.16/exercise4.16.2.png)
在10倍木星质量时，就可以看出地球，包括太阳都在发生向着某个方向的进动，木星轨道依旧偏离较大。

------
100倍木星质量：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter4/exercise4.16/exercise4.16.3.png)
从这里开始，整个系统都极不稳定，三个形体甚至会发生碰撞。
1000倍木星质量；
在这个数量级下，木星质量与太阳处于同一个量级：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter4/exercise4.16/exercise4.16.4.png)
系统明显表现出混沌状态。
进一步的，利用vpython模拟了三者的运动状态，但不太会使用录屏软件，这里未能附上gif，但是给出了[源文件](https://github.com/fxdhi/computationalphysics_N2013301020017/blob/master/chapter4/exercise4.16/threebody.py)
###结论
三体运动呈现出一种混沌系统的特性。