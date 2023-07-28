import numpy as np

print('-------- .arange ---------') # 创建数值范围并返回 ndarray 对象
    # numpy.arange(start, stop, step, dtype)
x = np.arange(5, dtype = float)
print(x)
x = np.arange(10, 20, 2)
print(x)

print('-------- .linspace ---------')   # 创建一维数组，由等差数列构成
    # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
a = np.linspace(10, 20, 5, endpoint = False) # 不包含终止值
print(a)

print('-------- .logspace ---------')   # 用于创建一个于等比数列
    # np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
a = np.logspace(1.0, 2.0, num = 10)
print(a)


