
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

# 元祖

