## 面向对象示例
class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_score(self):
        print('%s: %s' % (self.name, self.age))


bar = Student('Bar', 59)
bar.print_score()
