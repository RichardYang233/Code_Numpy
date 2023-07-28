import numpy as np

print('-------- .asarray ---------')    # 从已有的数组创建数组
    # numpy.asarray(a, dtype = None, order = None)
x = [1, 2, 3]   # 元组
a = np.asarray(x)
print(a)
y = (1, 2, 3)   # 列表
b = np.asarray(y)
print(b)
z = [(1, 2, 3), (4, 5, 6)] # 元组列表
c = np.asarray(z)

print('-------- .frombuffer ---------') # 用于实现动态数组
    # numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
    #                   v v
    #                  buffer : 可以是任意对象，会以流的形式读入
s = b'Hello World'  # 字节字符串，以字节为单位储存
a = np.frombuffer(s, dtype = 'S1')
print(a)

print('-------- .fromiter ---------')   # 可迭代对象中建立 ndarray 对象，返回一维数组
    # numpy.fromiter(iterable, dtype, count=-1)
list = range(5)
it = iter(list)
x = np.fromiter(it, dtype = float)
print(x)

















