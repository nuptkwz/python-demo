class Animal(object):
    def run(self):
        print('Animal is running')


## 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承
class Dog(Animal):
    pass


class Cat(Animal):
    pass


Dog().run()