import numpy as np

# 广播 是 numpy 对不同 shape 的数组进行数值计算的方式
# 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制

a = np.array([[ 0,  0,  0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]
              ])
b = np.array([0, 1, 2])
print(a + b)

# 广播规则：

# 所有数组向形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
# 输出数组的形状是输入数组形状的各个维度上的最大值。
# 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
# 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。

# 简单理解：对两个数组，分别比较他们的每一个维度（若其中一个数组没有当前维度则忽略），满足：

# 数组拥有相同形状。
# 当前维度的值相等。
# 当前维度的值有一个是 1。
# 若条件不满足，抛出 "ValueError: frames are not aligned" 异常