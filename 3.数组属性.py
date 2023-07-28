import numpy as np

# NumPy 数组的维数称为 秩（axis）
# 每一个线性的数组称为是一个 轴（axis），也是 维度（dimensions）

print('-------- .ndim ---------')
a = np.arange(24)  # 0 -> 23 依次排列
print(a.ndim)      # 维度
b = a.reshape(2, 4, 3)   # 第一维有2个元素，第二维有4个元素，第三维有3个元素
print(b)

print('-------- .shape ---------') # 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)
a = np.array( [[1, 2, 3], 
               [4, 5, 6]] )
print(a.shape)
a.shape = (3, 2)  # 调整数组维度
b = a.reshape(3, 2)   # 调整数组维度
print(a)
print(b)

print('-------- .itemsize ---------') # 以字节的形式 返回数组中每一个元素的大小
x = np.array([1, 2, 3, 4, 5], dtype = np.int8)
print(x.itemsize)
y = np.array([1, 2, 3, 4, 5], dtype = np.float64)
print(y.itemsize)

print('-------- .flags ---------') # 返回 ndarray 对象的内存信息
x = np.array([1, 2, 3, 4, 5])
print(x.flags)

