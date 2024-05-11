# 普通方法构造数组
L = []
for i in range(1, 100):
    if i % 2 == 1:
        L.append(i)

print(L)

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[-1])

# 取前3个元素，用一行代码就可以完成切片,索引0，1，2
print(L[0:3])

# 如果第一个索引是0，还可以省略：
print(L[:3])

# 迭代
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k)
print("----------------------")

for k in d.keys():
    print(k)
print("----------------------")

for v in d.values():
    print(v)
print("----------------------")

for k, v in d.items():
    print(k, v)
print("--------k,v--------------")

# 字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABCDEF':
    print(ch)

# 判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：
from collections.abc import Iterable

instanceResult = isinstance('abc', Iterable)
print("instanceResult:", instanceResult)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

