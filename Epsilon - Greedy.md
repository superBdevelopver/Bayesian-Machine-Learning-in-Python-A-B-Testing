---
typora-root-url: /Users/yuliang.liang/Desktop/Udemy Class
---

Epsilon Greedy Algorithm (E贪婪算法)

### Basic Concept

E贪婪算法，是强化学习中较为基础的概念，用于平衡exploration（探索）和 exploitation（利用）两者之间的抉择。

**exploration:**

在不同的选择中随机选择一个进行探索

**exploitation:**

基于目前的数据，得出一个最优的选择

### Background

Bandit Arms问题，赌场有一台老虎机，老虎机上有多个拉杆，每个拉杆对应不同的胜率。赌徒在尝试多次积累一定数据之后，面临着抉择的困难。是再随机拉动一个拉杆，还是基于目前数据计算的各拉杆胜率选择一个胜率最高，赌徒应该怎么做才能够提高自己的胜率。

### Description

E贪婪算法会设定一个参数E

参数E代表exploration的概率，如果参数E设置为10%

即做出下一步的抉择时，智慧体有10%概率进行exploration，90%概率进行exploitation。

算法缺点：

1. 随机探索，导致效率低下（考验参数E的设置是否合理）
2. 在复杂环境中的表现不佳

