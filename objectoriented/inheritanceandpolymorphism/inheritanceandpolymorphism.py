class Animal(object):
    def run(self):
        print('Animal is running')


## 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承
class Dog(Animal):
    pass


## 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()
class Cat(Animal):
    def run(self):
        print('Cat is running')


Dog().run()
Cat().run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))

## 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
## 使用type()方法
print(type(123))
print(type('str'))
print(type(None))

## 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))

## 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数

## 可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))

##如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir(123))

