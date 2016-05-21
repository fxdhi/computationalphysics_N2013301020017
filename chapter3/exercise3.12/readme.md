##姓名：周一凡
##学号：2013301020017
###习题3.12
> - 背景
物理摆在加了阻尼与周期性的驱动力之后，当周期性的驱动力的最大值F_d达到一定值时，产生了不可预测的轨迹，然而当F_d较小时，其运动状况又是可以预测的，这就是一个混沌系统所具备的条件。

---
> - 正文
本次计算依然使用euler-cromer法，所用的微分方程组为：
> - ![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/gif.latex.3.12gif.gif)
> - ![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/gif.latex.gif3.12.1.gif)
用子程序形式即为：
> - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/gif.latex3.12.2.gif)
> - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/gif.latex3.12.3.gif)
> - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/gif.latex3.12.4.gif)
所得F_d在各种取值下$\theta(t)$ 的图像
![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.12.1.png)
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.12.2.png)
![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.12.3.png)
由于在F_d较大的情况下，混沌系统的运动状况无法预测，且角度与时间的图像不够直观，所以绘制相图$\theta$-$\omega$:
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.12.4.png)
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.12.5.png)
本题的目标是绘出在特定的时间节点形成奇异吸子构成的相图，并与书中所给的$2\pi$ 的情况做对比:
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.12.6.png)
以下是$\pi/2$ 的情况，即驱动力最大的点
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.12.7.png)
接着是$\pi/4$ 的情况
![enter image description here](https://github.com/fxdhi/computationalphysics_N2013301020017/blob/master/chapter3/exercise3.12.8.png?raw=true)
###结论
取不同的时间节点绘制出的吸相图是不同的，具备一定的分形结构，在细节出的图像与图像的整体形貌是一致的。
