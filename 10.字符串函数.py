import numpy as np

print("-- np.char.add() --")    # 字符串连接
print(np.char.add(['hello'], ['  xyz']))
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))
print('\n')

print("-- np.char.multiply() --")   # 多重连接
print(np.char.multiply('Runoob ', 3))
print('\n')

print("-- np.char.center() --")     # 将字符串居中，并使用指定字符在左侧和右侧进行填充
# np.char.center(str, width, fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print(np.char.center('Runoob', 20, fillchar = '*'))
print('\n')

print("-- np.char.capitalize() --") # 第一个字母转换为大写
print(np.char.capitalize('runoob'))
print('\n')

# 下面太多了...
# 后续的：数学函数，算术函数，统计函数。先按下不表，用的时候再查

