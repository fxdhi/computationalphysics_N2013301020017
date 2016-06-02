##姓名：周一凡
##学号：2013301020017
##exercise7.3
###背景
本章重点讨论了随机系统，随机系统不同于我们通常所研究的系统，他拥有非常多的自由度，通常不能运用以往的像是描述抛体运动的微分方程组这类的模型来描述，而且在某个时间点上，随机系统出现的结果并不确定，而是概率事件，所以我们可以用统计模型去研究随机系统。
###正文
一维方向上的随机运动，以原点为起点，每个步长是确定的，但是向左向右在某一个时间点确实不确定的，但是在没有其他外力的条件下，向左向右的概率相等，这可以视作扩散运动的一维描述，具体实现这种模型的方案如下：
>1.初始化一个随机数生成器，并将其放入循环中。
>2.初始化列表$x$以及<$x^2$>,在每个循环中记录他们的数据。
>3.在0~1之间取随机数，当x<0.5时，向左，即x-1,否则，向右，即x+1。
>4.记下每一步的$x$以及$<x^2>$,其中$<x^2>$为$x^2$的平均值。

得出如下结果：

这是x关于步数的分布：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter7/exercise7.3.1.png)
这是$<x^2>$关于步数的分布：
![](https://github.com/fxdhi/computationalphysics_N2013301020017/blob/master/chapter7/exercise7.3.2.png?raw=true)
拟合之后的图像为：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter7/exercise7.3.3.png)
可以发现$<x^2>$与时间t近似呈正比，满足扩散规律。
而本体让我们讨论的是这种情况的变式：
即向左向右运动的概率不等，具体为向左的概率为0.25，向右的概率为0.75，这点只需在源程序上稍作修改即可得到。
计算结果如下：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter7/exercise7.3.4.png)
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter7/exercise7.3.5.png)

###结论
从上述图示，不难发现，如果改变了相应的统计规律，粒子的运动会以一个大趋势向某一个方向运动，尽管偶尔会有涨落，但是趋势是确定的，而从$<x^2>$与时间t的关系来看，后来的关系已经大幅偏离原来的拟合结果，故在此种情况下，该运动不在具有扩散的特征。

