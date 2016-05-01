##姓名：周一凡
##学号：2013031020017
exercise3.26 洛仑兹吸引子
###背景
我们之前已经讨论过单摆的混沌系统，尽管那是很简单的系统，但却表现出了极为丰富的行为，所以当我们考虑稍微复杂一点的系统时，该系统能够表现出混沌行为也就不那么让人奇怪了。习题3.26讨论的洛仑兹模型是研究流体力学的微分方程，而且讨论的是其中一种特殊情况——瑞利—伯纳德模型。
###正文
该模型可以概括为一个三元的微分方程组：
> - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/gif.latex1.gif)


> - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/gif.latex2.gif)
 

> - ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/gif.latex3.gif)

---------
此处不涉及二阶微分，故euler法就可以保证运算在一定程度下的准确性，
分别讨论了r=5,10,25的情形，做出z（t）图像，发现只有r=25出出现混沌现象，而r=5或10都是逐渐衰减至平稳。以下是各情况的图像对比：
 ![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/exercise3.26.1.png)
 理论计算发现出现混沌现象的r的临界值为470/19=24.74,图像显示结过与此吻合。参照前面研究单摆混沌系统的方法，我们可以做出x-z的相空间图像，可以发现轨迹随r的变化，即无混沌到混沌的变化十分显著：
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/exercise3.26.2.png)
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/exercise3.26.3.png)
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/exercise3.26.4.png)
无混沌时，轨迹呈现收缩，趋向于一点，而混沌系统中，轨迹呈现出某种周期性。
进一步的，我们取这根三维曲线在x=0平面与y=0平面所截出的图像，可以发现即使该系统是高度混沌的，但是相空间中的吸引子表面还是体现很好的规律性的，并且是独立于初始条件的。
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/exercise3.26.5.png)
![enter image description here](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter3/exercise3.26/exercise3.26.6.png)
###结论
相空间中的吸引子图像与初值条件无关，即混沌系统中在某些参数确定后相对规则的一部分。