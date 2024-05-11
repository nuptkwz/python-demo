# if 判断
a = 100
if a > 0:
    print(a)
else:
    print(-a)

# 整数、浮点数、字符串、
# 转义
print("I\'m \"OK\"!")
print('I\'m learning \n Python.')
print('\\\n\\')

print('''line1
line2
line3''')

# 布尔值
print(False)
print(3 > 5)

# not运算是非运算
print(not False)

# 空值 用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值
print(None)

t_007 = 'T007'
print(t_007)

# 在Python中，通常用全部大写的变量名表示常量
print(10 / 3)

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：3.0
print(9 / 3)

# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数,//除法只取结果的整数部分 3
print(9 // 3)

# 中文
print('包含中文的str')

# 字符编码转换
print(ord('a'))  # 97
print(ord('中'))  # 20013
print(chr(66))  # 'B'
print(chr(20016))

print('\u4e2d\u6587')

# 长度
le = len("ABC")
print(le)

enc = '中文'.encode('utf-8')
print(enc)
print(len(enc))

# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

t = (1, 2, 3)
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
# 获取最后一个元素
print(t[-1])
print(t[-2])

# 循环
age = 3
if age >= 18:
    print("18")
elif age > 6:
    print("6")
else:
    print("end")

# 输入比较
# birth = input('birth: ')
# if birth < "2000":
#     print('00前')
# else:
#     print('00后')

# match语句类似于switch case
score = 'B'
match score:
    case 'A':
        print("score is :", "A")
    case 'B':
        print("score is :", "B")
    case _:
        print("match others")

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range(5)生成的序列是从0开始小于5的整数：
num_list = list(range(5))
# [0, 1, 2, 3, 4]
print(num_list)

# dict，相当于Java的map,dict的key必须是不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

d['Bob'] = 100
print(d['Bob'])

d.pop('Bob')
print(d)

# set
s = set([1, 1, 2, 3])
print(s)

s.add(4)
s.add(4)
s.remove(1)
print(s)

# set的交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) # {2, 3}
print(s1 | s2) #{1, 2, 3, 4}


