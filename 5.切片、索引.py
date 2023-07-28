import numpy as np

# ndarray 对象的内容可以通过 索引、切片 来访问和修改，与 Python 中 list 的切片操作一样

a = np.arange(10)

print('-----------------')
s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2 
print(a[s])  

print('---------1--------') 
b = a[2:7:2]
print(b)

print('---------2--------')
print(a[2:])

print('---------3--------')
print(a[2:5])

print('---------4--------')
a = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [4, 5, 6]
])
print(a)
print('从 a[1:] 开始切割：')
print(a[1:])

print('---------5--------')
a = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [4, 5, 6]
]) 
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素
