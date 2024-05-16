# 高阶函数
## map/reduce

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
