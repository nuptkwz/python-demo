from functools import reduce


def lambda_test_1():
    # 计算平方
    square = lambda x: x ** 2
    print(square(3))  # 输出: 9

    # 直接作为参数传递
    print(sorted([("Alice", 85), ("Bob", 60)], key=lambda x: x[1], reverse=True))
    # 输出: [('Alice', 85), ('Bob', 60)]

def lambda_map_squared():
    numbers = [1, 2, 3]
    test = map(lambda x: x ** 2, numbers)
    squared = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9]
    print(squared)

def lambda_filter():
    even_nums = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # [2, 4]
    print(even_nums)

def lambda_reduce():
    from functools import reduce
    product = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24
    print(product)


def power_factory(exponent):
    def power(base):
        return base ** exponent  # 记住exponent的值

    return power

def factorial():
    from functools import partial

    def multiply(a, b):
        return a * b

    double = partial(multiply, b=2)
    print(double(5))  # 10

    # 应用：创建专用文件读取器
    read_json = partial(open, mode='r', encoding='utf-8')
    print(read_json)

def add_grade(student):
    score = student["score"]
    grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "D"
    return {**student, "grade": grade}  # 返回新字典，避免修改原数据


def is_passing(student):
    return student["score"] >= 60

if __name__ == '__main__':
    #1.闭包与偏函数：提升函数复用性
    # square = power_factory(2)
    # print(square(3))  # 9

    # 2.
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 45},
        {"name": "Charlie", "score": 92}
    ]

    # 组合map/filter/reduce
    processed = list(map(add_grade, students))
    passed_students = list(filter(is_passing, processed))
    avg_score = reduce(lambda x, y: x + y["score"], passed_students, 0) / len(passed_students)

    print(f"及格学生: {passed_students}")
    print(f"平均分: {avg_score:.1f}")