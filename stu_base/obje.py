# 面向对象
# 类：具有相同特征或行为的事物的统称，抽象的
# 对象：由类创建出来的一个具体存在的事物，可以直接使用
# self参数：由哪一个对象调用的方法，方法内的self是就是哪一个对象的引用
# __init__()初始化方法，创建对象会自动调用，用来定义类具有哪些属性
# 面向对象三大特征：封装、继承、多态
# 封装：将属性和方法封装到一个抽象类中
# 继承：实现代码的重用，相同的代码不需要反复编写
# 多态：不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度
# 类属性和类方法：给类对象定义的属性和方法.(需要保证生成的对象始终只有一个时可以用)
# 类方法装饰器：@classmethod
# 私有属性和私有方法：只能在类定义内部使用
# 静态方法：方法既不需要访问实例属性或调用实例方法，也不需要访问类属性或调用类方法，可封装成静态方法
# 静态方法装饰器：@staticmethod
# # 类的定义
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

# class LittleCat:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name}爱吃鱼")
#
# tom = LittleCat("Tom")
# tom.eat()


# # 封装案例
# class LoginPage:
#
#     def __init__(self,username,password,verify_code):
#         self.username = username
#         self.password = password
#         self.verify_code = verify_code
#
#     def login(self):
#         print(f'输入用户名:{self.username}')
#         print(f'输入密码:{self.password}')
#         print(f'输入验证码:{self.verify_code}')
#         print('点击登录按钮')
#
# if __name__=='__main__':
#     login_page = LoginPage('admin','123456','7777')
#     login_page.login()

# # 继承案例
# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("eat")
#
#     def sleep(self):
#         print("sleep")
#
# class Cat(Animal):
#     def catch(self):
#         print("catch")
#
# class Jerry(Cat):
#     def run(self):
#         print("run")
#
# tom = Jerry("Jerry",2)
# tom.eat()
# tom.sleep()
# tom.catch()
# tom.run()

# # 多态案例
# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#
#     def game(self):
#         print(f"{self.name} game")
#
# class Wangwang(Dog):
#     def game(self):
#         print(f"{self.name} fly")
#
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#
#     def game_with_dog(self,dog):
#         print(f"{self.name} with {dog.name} play")
#         dog.game()
#
# wangwang = Wangwang("wangwang")
# person = Person("Lily")
# person.game_with_dog(wangwang)


# # 类属性案例
# class Tool(object):
#     count = 0
#
#     def __init__(self,name):
#         self.name = name
#         Tool.count +=1
#
# tool1 = Tool("1")
# tool2 = Tool("2")
# tool3 = Tool("3")
#
# print(f"sum = {Tool.count}")


# # 类方法案例，需要装饰器@classmethod来标识
# class Tool(object):
#     count = 0
#
#     def __init__(self,name):
#         self.name = name
#         Tool.count +=1
#
#     @classmethod
#     def show_sum(cls):
#         print(f"sum = {cls.count}")
#
# tool1 = Tool("1")
# tool2 = Tool("2")
# tool3 = Tool("3")
#
# Tool.show_sum()


# 综合案例
class Game(object):
    # 游戏最高分，类属性
    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name

    # 查看帮助信息，静态方法
    @staticmethod
    def show_help():
        print("help info")

    # 查看最高分，类方法
    @classmethod
    def show_top_score(cls):
        print(f"top score: {cls.top_score}")

    # 开始游戏，实例方法
    def start_game(self):
        print(f"{self.player_name} start game")

# 调用类方法，设置最高分
Game.top_score = 999
Game.show_help()
Game.show_top_score()
game = Game("Lily")
Game.start_game(game)