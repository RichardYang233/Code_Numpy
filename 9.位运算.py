import numpy as np

print('-------- 位运算 ---------')
print("-- bitwise_and() --")    # 对数组中整数的二进制形式执行位与运算
a, b = 13, 17
print(bin(a), bin(b))
print(np.bitwise_and(13, 17))

print("-- bitwise_or() --")
print(np.bitwise_or (13, 17))

print("-- invert() --")     # 对数组中整数进行位取反运算
print ('13 的位反转，其中 ndarray 的 dtype 是 uint8:')
a = np.array([13], dtype = np.uint8)
b = np.invert(a)
print(b)
print ('13 的二进制表示：')
print(np.binary_repr(13, width = 8))
print ('242 的二进制表示：')
print(np.binary_repr(242, width = 8))

print("-- left_shift() --")     # 将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的 0
print(np.left_shift(10, 2))     # 将 10 左移 2 位
print(np.binary_repr(10, width = 8))    # 10 的二进制
print(np.binary_repr(40, width = 8))    # 左移后

print("-- right_shift() --")

