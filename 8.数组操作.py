import numpy as np

print('-------- 修改数组形状 ---------')
print("-- numpy.reshape -- ")    # 在不改变数据的条件下修改形状
a = np.arange(8)
print(a)
b = a.reshape(4, 2)
print(b, '\n')

print("-- numpy.adarray.flat --")     # 是一个数组元素迭代器
a = np.arange(9).reshape(3, 3)
for row in a :      # row
    print(row)
for element in a.flat :     # element
    print(element)
print('\n')

print("-- numpy.adarray.flatten --")     # 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
# ndarray.flatten(order = 'C')
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
a = np.arange(8).reshape(2, 4)
print(a)
print(a.flatten())      # 展开
print(a.flatten(order = 'F'))       # 按列展开

print("-- numpy.ravel --")      #  展平的数组元素，修改会影响原始数组
# numpy.ravel(a, order='C')
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
a = np.arange(8).reshape(2, 4)
print(a)
print(a.ravel())
print(a.ravel(order = 'F'))

print('-------- 翻转数组 ---------')
print("-- numpy.transpose -- ") 
# numpy.transpose(arr, axes)    转置矩阵
# arr.T     也可以

print("-- numpy.rollaxis -- ") 
# numpy.rollaxis(arr, axis, start)

print("-- numpy.swapaxes -- ") 
# numpy.swapaxes(arr, axis1, axis2)

print('-------- 修改数组维度 ---------')
print("-- numpy.broadcast -- ") 
print("-- numpy.broadcast_to -- ") 
print("-- numpy.expand_dims -- ") 
print("-- numpy.squeeze -- ") 

print('-------- 连接数组 ---------')
print("-- numpy.concatenate -- ") 
print("-- numpy.stack -- ") 
print("-- numpy.hstack -- ") 
print("-- numpy.vstack -- ") 

print('-------- 分割数组 ---------')
print("-- numpy.split -- ") 
print("-- numpy.hsplit -- ") 
print("-- numpy.vsplit -- ") 

print('-------- 元素添加和删除 ---------')
print("-- numpy.resize -- ")
print("-- numpy.append -- ") 
print("-- numpy.insert -- ") 
print("-- numpy.delete -- ") 

# 返回从输入数组中删除指定子数组的新数组
print("-- numpy.unique -- ") 
# 去除数组中的重复元素