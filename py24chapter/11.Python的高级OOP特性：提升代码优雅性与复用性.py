
class TimeConverter:
    __DAYS_IN_YEAR = 365  # 类私有属性

    def __init__(self, hours):
        self.hours = hours

    @classmethod
    def from_days(cls, days):
        """创建基于天数的实例"""
        return cls(days * 24)

    @staticmethod
    def is_valid_hour(value):
        """验证小时数值是否有效"""
        return 0 <= value < 24


class Circle:
    def __init__(self, radius):
        self._radius = radius  # 保护属性

    @property
    def radius(self):
        """获取半径值"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """设置半径值的验证逻辑"""
        if value <= 0:
            raise ValueError("半径必须为正数")
        self._radius = value

    @property
    def area(self):
        """计算圆面积（只读属性）"""
        return 3.14 * self._radius ** 2


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """重载 + 运算符"""
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """重载 * 运算符（标量乘法）"""
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        """重载字符串输出"""
        return f"Vector({self.x}, {self.y})"


class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("必须提供向量分量")
        self.components = list(components)

    def __abs__(self):
        """计算向量模长"""
        return sum(x ** 2 for x in self.components) ** 0.5

    @property
    def magnitude(self):
        """模长属性（通过property实现）"""
        return abs(self)

    def __matmul__(self, other):
        """重载 @ 运算符实现点积"""
        if len(self) != len(other):
            raise ValueError("向量维度不匹配")
        return sum(a * b for a, b in zip(self, other))

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __repr__(self):
        return f"Vector{tuple(self.components)}"

if __name__ == '__main__':
    # 1.使用示例
    # t1 = TimeConverter.from_days(10)  # 类方法构造实例
    # print(t1.hours)  # 输出：240
    # print(TimeConverter.is_valid_hour(25))  # 静态方法调用：False

    # 2.使用示例
    # c = Circle(5)
    # print(c.area)  # 输出：78.5
    # c.radius = 7  # 通过setter修改
    # # c.radius = -1  # 触发ValueError异常

    # 3.复写方法
    # v1 = Vector(2, 3)
    # v2 = Vector(4, 5)
    # print(v1 + v2)  # 输出：Vector(6, 8)
    # print(v1 * 3)  # 输出：Vector(6, 9)

    #4.实战例子
    v = Vector(3,4)
    print(f"模长：{v.magnitude:.2f}")  # 输出：模长：5.00

    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(v1 @ v2)  # 点积运算：输出 32
