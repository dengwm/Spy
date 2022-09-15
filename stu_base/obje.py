# 面向对象
# 类：具有相同特征或行为的事物的统称，抽象的
# 对象：由类创建出来的一个具体存在的事物，可以直接使用
# self参数：由哪一个对象调用的方法，方法内的self是就是哪一个对象的引用
# __init__()初始化方法，创建对象会自动调用，用来定义类具有哪些属性


# 类的定义
# class Cat:
#     def eat(self):
#         print("小猫爱吃鱼")
#
#     def drink(self):
#         print("小猫在喝水")
# # 类的调用
# tom = Cat()
# tom.eat()
# tom.drink()

class LittleCat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}爱吃鱼")

tom = LittleCat("Tom")
tom.eat()

