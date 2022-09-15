
# 数据类型
# 数值、字符、布尔
a = "4"
b = "6"
print(a+b) # 46
a = 4
b = 6
print(a+b) # 10


# 字符串
# len：计算长度
# string(开始:结束:步长)：截取
st = "python test"
print(len(st))
print(st[1:5:3])


# 运算符
# 算术、赋值、比较、逻辑(与或非)、类型转换(数值和字符)
a = "π = "
b = 3.14
print(a+str(b))   # π = 3.14
print(a+repr(b))  # π = 3.14


# 输入输出
# s = input("input: ")
# print(s)


# 数据结构
# 列表
# 定义
a = [1, 2, 3, 4]
b = []
print(a)
# 访问
print(a[2])
# 添加
a.append(5)
print(a)
# 删除
del a[2]
print(a)

# 元祖：不可修改
# 定义
a = (1, 2, 3, 4)
# 访问
print(a[2])
# 删除
del a
# 计算长度
a = (1, 2, 3)
print(len(a))
# 迭代
b = a * 3
print(b) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 字典：键值对
# 实例化定义
dic = dict()
# 定义
dic = {"name":"admin","pwd":"123456"}
# 新增
dic["sex"] = "女"
print(dic)
# 删除
dic.pop("sex")
# 查询
print(dic.get("name"))
# 遍历字典的key
for key in dic.keys():
    print(key)
# 遍历字典的value
for value in dic.values():
    print(value)
# 遍历字典的value和key
for k,v in dic.items():
    print(f"key={k} value={v}")
# 字典切片
# 数据[起始索引:结束索引:步长]
name = "abcdefg"
print(name[2:5:1])
# 键值对个数
print(len(name))


# 函数
# 定义
def hello():
    print("hello")
# 调用
hello()
# 传参
def get_max(x,y):
    if x>y:
        return x
    else:
        return y
print(get_max(5,6))
# 缺省函数
def print_info(name,gender="女生"):
    print(f"{name}是{gender}")
print_info("dd")
# 多参函数
def demo(num, *args):
    print(num)
    print(args)
demo(1,2,3,4,5)
# 匿名函数
sum = lambda arg1,arg2:arg1 + arg2
print(sum(10,20))