import numpy as np

# numpy.dtype(object, align, copy)

print('-----------------')
dt = np.dtype(np.int32)
print(dt)

print('-----------------')
dt = np.dtype( [('age', np.int8)] )
print(dt)

print('-----------------')
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype =  dt)
print(a)
print(a['age'])  # 类型字段名可以用于存取实际的 age 列

print('-------- 结构化数据类型的使用 ---------')  
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
data = [             # 列表元素为元组 
    ('Alice', 22, 89.5),
    ('Bob', 21, 78.0),
    ('Charlie', 20, 92.3)
]
a = np.array(data, dtype = student)
print(a)

