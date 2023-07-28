import numpy as np

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#                     dtype 是数组元素的数据类型，下章会讲

print('-----------------')
a = np.array([1, 2, 3])
print(a)

print('-----------------')
a = np.array([ [1, 2], [3, 4] ])
print(a)

print('-----------------')
a = np.array([1, 2, 3], ndmin = 2) # 设置最小维度
print(a)

print('-----------------')
