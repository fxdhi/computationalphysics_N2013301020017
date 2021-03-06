##chapter2
##exercise2.9
###摘要
第二章作业主要围绕物体考虑空气阻力的情形下，如何使用euler法来解决相关的物理问题。
###背景介绍
本次作业共分为3个难度层次。

    作业L1 2.9题
    作业L2 2.10题强化版（引入风阻）————“辅助精确打击系统”
    作业L3 发展“超级辅助精确打击系统”（考虑炮弹初始发射的时候发射角度误差1%，速度有5%的误差，风阻误差10%，可以考虑引入Coriolis force等，以炮弹落点与打击目标距离差平方均值最小为优胜）
> - 作业第一个层次，主要是要求在考虑风阻以及空气密度随海拔的变化对弹道区县的影响，并且求出在哪个角度下发射能使炮弹飞的最远。
> - 作业的第二个层次是要求开发一套精确打击目标的程序，所给的目标是与炮弹有高度差，要求目标处于炮弹的轨迹上，并求出能够打击目标的最小发射角。
> - 作业的第三个层次是要求在上一个层次的基础上考虑炮弹发射时的误差以及风阻变化带来的误差，以求进行更准确的打击。

###正文
####level 1:
作业2.9题要求考虑风阻以及空气密度变化带来的风阻的变化，采用了绝热过程的近似，选取初速度为500m/s的炮弹，以5°为梯度进行扫描，通过画出不同角度的轨迹，来判断最远距离是由哪个角度产生的。
__________
绝热过程空气密度变化：
![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter2/exercise2.9/gif.latex.gif)
![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter2/exercise2.9/exercise2.9.1.png)
![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter2/exercise2.9/exercise2.9.2.png)
![](https://raw.githubusercontent.com/fxdhi/computationalphysics_N2013301020017/master/chapter2/exercise2.9/exercise2.9.3.png)

###结论
经过修正的曲线明显高于未加密度修正的曲线，并且可以得出炮弹发射的最远距离是在发射角为45°时产生的。
###致谢
参考了王世兴同学关于终止条件的代码。

