# 调用函数 Python内置了很多有用的函数，我们可以直接调用
# python官方文档：https://docs.python.org/3/library/functions.html#abs
print(abs(-100))
print(abs(-100.12))

print(max(2, 3, 1, -5, 9))
print(int('123'))

print(int(12.34))

print(float('12.34'))

print(str(1.23))

# 函数指定别名
a = abs
print(a(-1))


# 定义函数,定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
def add(b, c):
    return b + c


print(add(1, 2))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-100))


# 空函数 pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass


print(nop())  # None

# 返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(10, 20, 30, 90))

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    temp = b * b - 4 * a * c
    fen_zi_1 = -b + math.sqrt(temp)
    fen_zi_2 = -b - math.sqrt(temp)
    return fen_zi_1 / (2 * a), fen_zi_2 / (2 * a)


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))


# 函数的参数

def power(x1):
    return x1 * x1


print(power(2))


# power2(x, n)
def power2(e, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * e
    return s


print(power2(2, 3))


# 默认函数,使用默认参数最大的好处是能降低调用函数的难度
def power_x_2(f, g=2):
    s = 1
    while g > 0:
        g = g - 1
        s = s * f
    return s


print(power_x_2(5))

print(power_x_2(5, 3))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


print(enroll('Sarah', 'F'))


# 传入一个list，添加一个end返回
def add_end(L=[]):
    L.append("end")
    return L


result = add_end(['a', 'b', 'c'])
print(result)

print(add_end())


def add_end_with_none(L=None):
    if L is None:
        L = []
    L.append("end")
    return L


print(add_end_with_none())
print(add_end_with_none())


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))


# 尾递归方式
def fact2(n):
    return fact_item(n, 1)


def fact_item(n, k):
    if n == 1:
        return k
    return fact_item(n - 1, k * n)


print(fact2(3))
