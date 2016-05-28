##姓名：周一凡
##学号：2013301020017
##exercise6.6
###背景
一维波动方程利用差分法来求解，验证在一根两端边界固定的弦在初始时刻给一个扰动，之后的过程中，产生的两个波包，在碰撞后，速度以及振幅不变的事实。
###正文
本次的问题与以往不同的是，这是一个二元函数，迭代的过程与两个变元有关，时间用n$\delta t$代替,位移用i$\delta x$代替，继而推出迭代公式为：
>y(i,n+1)=2[1-$r^2$]y(i,n)-y(i,n-1)+$r^2$[y(i+1,n)+y(i-1,n)]
>

其中
>r=c$\frac{\delta t}{\delta x}$

边界条件
y(0,n)=y(M,n)=0
y(x,0)=$e^{-k(x-x0)^2}$
这是通过数值计算得到的波的运动状态：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter6/Animation.gif) 
这是从中选取的两张截图：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter6/exercise6.6.2.png)
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter6/exercise6.6.1.png)

###结论
从上图中可以看出两个波包在碰撞到边界后，发生半波损失，振幅反向，且可以看出，两个波包在碰撞前后，相速以及振幅都不变，各自沿着原来的方向运动。
###致谢
本次联系由于不会使用python编写相关的迭代程序故查找了相关matlab在这次联系中的解法。
[matlab源码地址](http://www.doc88.com/p-4387072961988.html)
