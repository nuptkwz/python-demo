
def slice():
    data = [10, 20, 30, 40, 50, 60]
    # 左闭右开
    print(data[1:4])  # 切片索引1-3 → [20,30,40]
    print(data[:3])  # 前三个 → [10,20,30]
    print(data[::2])  # 步长2 → [10,30,50]
    reverse_data = data[::-1]  # 步长为负一，相当于反转列表 → [60,50,40,30,20,10]
    return reverse_data


def deepCopy():
    import copy

    original = [[1, 2], [3, 4]]
    shallow = original[:]  # 浅拷贝
    deep = copy.deepcopy(original)  # 深拷贝

    original[0][0] = 99
    print(shallow)  # [[99,2],[3,4]] - 嵌套列表受影响
    print(deep)  # [[1,2],[3,4]]  - 完全独立

def tupleTest():
    # 创建元组
    student = ("李明", 19, "计算机科学")
    empty_tuple = ()
    single_tuple = ("单个元素",)  # 注意末尾逗号

    # 不可变性验证
    try:
        student[1] = 20  # 抛出TypeError
    except TypeError:
        print("元组不可修改！")

    # 解包操作
    name, age, major = student
    print(f"{name}主修{major}")  # 李明主修计算机科学

def _asdict():
    from collections import namedtuple

    # 创建学生类型
    Student = namedtuple("Student", ["name", "age", "gpa"])

    # 实例化
    s = Student(name="王芳", age=20, gpa=3.8)
    print(s.name)  # 王芳
    print(s._asdict())

if __name__ == '__main__':
    students = []  # 用列表存储学生信息

    while True:
        print("\n===== 成绩管理系统 =====")
        print("1.添加学生  2.查看所有  3.查询成绩  4.修改成绩  5.退出")

        choice = input("请选择操作: ")

        # 添加学生信息
        if choice == "1":
            name = input("姓名: ")
            score = float(input("成绩: "))
            students.append((name, score))  # 使用元组存储单条记录
            print(f"{name}添加成功！")

        # 显示所有记录
        elif choice == "2":
            if not students:
                print("暂无记录")
            for i, (name, score) in enumerate(students, 1):
                print(f"{i}. {name}: {score}")

        # 按姓名查询
        elif choice == "3":
            name = input("查询姓名: ")
            found = [(n, s) for n, s in students if n == name]
            if found:
                for n, s in found:
                    print(f"{n}的成绩: {s}")
            else:
                print("未找到记录")

        # 修改成绩（利用元组不可变性）
        elif choice == "4":
            name = input("修改谁的分数: ")
            for index, (n, s) in enumerate(students):
                if n == name:
                    new_score = float(input("新分数: "))
                    # 创建新元组替换旧元组
                    students[index] = (n, new_score)
                    print("修改成功！")
                    break
            else:
                print("未找到学生")

        # 退出系统
        elif choice == "5":
            print("系统退出")
            break