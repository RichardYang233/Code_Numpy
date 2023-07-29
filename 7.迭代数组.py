import numpy as np

# 迭代器对象 numpy.nditer 
# 提供了一种灵活访问一个或者多个数组元素的方式

print('-------- 关于遍历顺序 ---------')
a = np.arange(6).reshape(2, 3)
print ('原始数组是：')
print (a)

print ('迭代输出元素：')
for x in np.nditer(a):      # 返回一个迭代器对象
    print (x, end = ",")    # end 
print ('\n')

for x in np.nditer(a.T):
    print (x, end = ',')
print ('\n')

for x in np.nditer(a.T.copy(order = 'C')):  # 遍历结果不同，因为和前两种存储方式不一样
    print (x, end = ',')
print ('\n')


print('-------- 修改数组值 ---------')
# nditer 将视待迭代遍历的数组为 只读对象
a = np.arange(0, 60 , 5).reshape(3, 4)
print('原始数组是：')
print(a)
for x in np.nditer(a, op_flags = ['readwrite']):
    x[...] = 2 * x              # 指定 readwrite 或者 writeonly 的模式
print('修改后的数组是：')
print(a)


print('-------- 使用外部数值 ---------')
a = np.arange(0, 60 , 5).reshape(3, 4)
print('原始数组是：')
print(a)
print('修改后的数组是：')
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
    print(x)


print('-------- 广播迭代 ---------')
# 如果两个数组是可广播的，nditer 组合对象能够同时迭代它们

