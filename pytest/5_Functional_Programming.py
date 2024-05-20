# 高阶函数
## map/reduce
import functools


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
print(list(r))

test_str = map(str, [1, 2, 3, 4, 5])
print(list(test_str))

## reduce用法
## 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

from functools import reduce


def add(x, y):
    return x + y


result = reduce(add, [1, 3, 5, 7, 9])
print(result)


def fn(x, y):
    return x * 10 + y


result = reduce(fn, [1, 3, 5, 7, 9])
print(result)


## 将字符串转换成数字
def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


result = reduce(fn, map(char2num, "13579"))
print(result)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# filter函数用于过滤
## 例如过滤出奇数
def is_odd(x):
    return x % 2 == 1


filter_res = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print(list(filter_res))

## sorted排序算法
sorted_list = sorted([1, 2, -1, -3, 4])
print(sorted_list)
print(list(sorted_list))

## 字符串排序的例子
sorted_result = sorted(['bob', 'about', 'Zoo', 'Credit'])
## ['Credit', 'Zoo', 'about', 'bob']
print("sorted_result:", sorted_result)

sorted_result2 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
## ['about', 'bob', 'Credit', 'Zoo']
print("sorted_result2:", sorted_result2)

sorted_result3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
## ['Zoo', 'Credit', 'bob', 'about']
print("sorted_result3:", sorted_result3)

# 匿名函数
anonymous_func = map(lambda x: x * x, [1, 2, 3, 4, 5])
## [1, 4, 9, 16, 25]
print(list(anonymous_func))


# lambda x: x * x 实际上就是：
def f(x):
    return x * x


## 利用变量来调用该函数
f1 = lambda x: x * x
print(f1(5))


## 利用变量来调用该函数
def build(x, y):
    return x * x + y * y


print(build(5, 5))


## 函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2024-05-18')


f = now

print(f())
print(now.__name__)
print(f.__name__)


# python装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-03-25')


now()

print("log(now())")
log(now())

## 偏函数,Python的functools模块提供了很多有用的功能
int_value = int("12345")
print("int(\"12345\"):", int_value)

## 就可以做N进制的转换：
int_value_base_8 = int('12345', base=8)
print(int_value_base_8)


def int2(x, base=2):
    return int(x, base)


int_value_base_2 = int2('10000')
print(int_value_base_2)

## functools中的偏函数
int_2 = functools.partial(int, base=2)
func_tools_func = int_2('10000')
print(func_tools_func)

def __hello__(name):
    return "hello:"+name
