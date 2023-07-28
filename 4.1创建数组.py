import numpy as np

print('-------- .empty ---------')  # 创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
    # numpy.empty(shape, dtype = float, order = 'C')
x = np.empty([3, 2], dtype = int)
print(x)    # 未初始化，是随机数

print('-------- .zeros ---------')  # 创建指定大小的数组，数组元素以 0 来填充
    # numpy.zeros(shape, dtype = float, order = 'C')
y = np.zeros((2,2), dtype = int)
print(y)
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(x)

print('-------- .ones ---------')   # 创建指定形状的数组，数组元素以 1 来填充
x = np.ones(5) 
print(x)

print('-------- .zeros_like ---------') # 可以直接指定要创建的数组的形状
arr = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
zeros_arr = np.zeros_like(arr)
print(zeros_arr)

print('-------- .ones_like ---------')  # 同上
print('\n')
