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
print("sorted_result2:" , sorted_result2)

sorted_result3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
## ['Zoo', 'Credit', 'bob', 'about']
print("sorted_result3:", sorted_result3)
