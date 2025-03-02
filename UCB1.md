UCB全称，Upper Confidence Bound

UCB存在较多版本，其中应用较为广泛的UCB1 Version



Epsilon Greedy Algorithm 存在的缺点：

对于一些win rate很差的bandit arm，Epsilon Greedy Algorithm也会以相同的概率进行探索。然而事实上，对于win rate很差的bandit arm，仅仅需要探索几次之后就可以选择放弃（因为强化学习算法目的是找出最优的bandit arm），所以**Epsilon Greedy Algorithm在win rate较差的动作上浪费了不必要的成本**

-- UCB1算发主要就是针对以上问题的解决所提出的



UCB1详细算法介绍：

https://www.bilibili.com/video/BV1Kg411N7kx?spm_id_from=333.788.videopod.sections&vd_source=9e148ff2452c6acf65727fb306b977bc