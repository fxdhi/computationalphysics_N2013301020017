##姓名：周一凡
##学号：2013301020017
##exerciese5.16
###背景
计算亥姆霍兹线圈内外的磁场强度，并将计算结果与准确值比较。
###正文
 - 亥姆霍兹线圈在一些工程问题中有重要的应用,教科书上讨论亥姆霍兹线圈的磁场分布问题时只考虑轴线上的磁场分布, 跟实际的应用有一定
的距离。
 - 这里本想讨论整个空间磁场分布的求法，但是我不知道如何用python求积分运算，退而求其次还是只讨论了轴向的磁场分布，但是我参考了相关的文献，找出了关于空间磁场分布数值计算的结果。
[亥姆霍兹线圈空间磁场分布](https://github.com/fxdhi/computationalphysics_N2013301020017/blob/master/chapter5/%E4%BA%A5%E5%A7%86%E9%9C%8D%E5%85%B9%E7%BA%BF%E5%9C%88%E7%A9%BA%E9%97%B4%E7%9A%84%E7%A3%81%E5%9C%BA%E5%88%86%E5%B8%83.pdf)
 - 该文献中利用Mathematica计算出了磁场分布，磁场各分量的积分表达式为：
 - ![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter5/exercise5.16.2.PNG)
 - 这是在固定z的情况下，轴向磁场与y的关系:
 - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter5/exercise5.16.3.PNG) 
 - 可以发现，在z=0处，沿y轴方向上，磁场分布在线圈范围内也呈现出较为稳定的状态。
 这是固定y值，轴向磁场与z的关系：
 - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter5/exercise5.16.4.PNG) 
 - 这就是我们通常讨论的亥姆霍兹线圈的磁场分布关系的拓展，对比用python绘出的y=0处的图像：
 - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter5/exercise5.16.1.png) 
 
 -------
 发现两者在大致趋势上是相同的，但是单独讨论轴向磁场的图像在线圈边缘衰减的更为迅速，与从空间磁场出发得出的结果略有不同。
 进一步计算空间磁场，即三个方向的矢量和与y和z的关系：
 - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter5/exercise5.16.5.PNG) 
 - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter5/exercise5.16.6.PNG)

------- 
发现处在原点的磁场总是相当均匀的。
###结论
亥姆霍兹线圈在两线圈距离等于半径时，内部的磁场在原点的分布十分均匀，外部磁场从边缘处开始向外逐渐衰减。







