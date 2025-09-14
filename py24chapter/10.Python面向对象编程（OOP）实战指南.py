class Dog:
    # 构造函数：初始化对象属性
    def __init__(self, name, breed):
        self.name = name  # 实例变量
        self.breed = breed  # 实例变量

    def bark(self):  # 实例方法
        return f"{self.name}：汪！"


class TemperatureSensor:
    def __init__(self):
        self.__temperature = 0  # 私有变量

    def update(self, value):
        if -20 <= value <= 60:  # 数据校验
            self.__temperature = value
        else:
            print("无效温度值")

    def current(self):  # 公共接口
        return self.__temperature


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类需实现此方法")


class Cat(Animal):  # 继承Animal
    def speak(self):  # 方法重写
        return "喵~"


class Parrot(Animal):
    def speak(self):
        return "你好！"


def animal_hello(animal):
    print(animal.speak())  # 同一方法不同表现


if __name__ == '__main__':
    # 1. 创建对象实例
    # my_dog = Dog("阿黄", "金毛")
    # print(my_dog.bark())  # 输出：阿黄：汪！
    # print(f"品种：{my_dog.breed}")  # 输出：品种：金毛

    # 2. TemperatureSensor
    # sensor = TemperatureSensor()
    # sensor.update(25)
    # print(sensor.current())  # 输出：25
    # sensor.update(100)  # 输出：无效温度值

    # 3.继承
    # animals = [Cat("咖啡"), Parrot("小蓝")]
    # for a in animals:
    #     print(f"{a.name} 说：{a.speak()}")
    # # 输出：
    # # 咖啡 说：喵~
    # # 小蓝 说：你好！

    # 4. 多态
    # animal_hello(Cat("雪球"))  # 输出：喵~
    # animal_hello(Parrot("金刚"))  # 输出：你好！

    class BankAccount:
        def __init__(self, account_holder, balance=0.0):
            self.account_holder = account_holder
            self.__balance = balance  # 封装余额

        def deposit(self, amount):
            """存款"""
            if amount > 0:
                self.__balance += amount
                return f"存款成功！余额：¥{self.__balance:.2f}"
            return "存款金额必须大于0"

        def withdraw(self, amount):
            """取款"""
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                return f"取款成功！余额：¥{self.__balance:.2f}"
            return "余额不足或金额无效"

        def transfer(self, other_account, amount):
            """转账"""
            if self.withdraw(amount) != "余额不足或金额无效":
                other_account.deposit(amount)
                return f"向 {other_account.account_holder} 转账 ¥{amount:.2f} 成功！"
            return "转账失败：余额不足"

        def check_balance(self):
            """查询余额"""
            return f"当前余额：¥{self.__balance:.2f}"


    # 创建两个账户
    alice = BankAccount("Alice", 1000)
    bob = BankAccount("Bob", 500)

    print(alice.deposit(200))  # 存款成功！余额：¥1200.00
    print(alice.withdraw(300))  # 取款成功！余额：¥900.00
    print(alice.transfer(bob, 400))  # 向 Bob 转账 ¥400.00 成功！

    print(alice.check_balance())  # 当前余额：¥500.00
    print(bob.check_balance())  # 当前余额：¥900.00

    print(bob.transfer(alice, 1000))  # 转账失败：余额不足
