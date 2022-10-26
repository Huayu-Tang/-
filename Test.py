# @Time:2022/8/9 22:10
# @Author: Huayu
# @File:Test.py
# @Software:PyCharm

# 单行注释
print("hello,world")  # 注释

'''
多行注释 ctrl+/
print("hello,world1")
'''
# 1.变量定义 见名知意
a = 10  # 整数变量
# a = b = c = 100
# a, b, c = 1, 100, "hello"
b = "huayu"  # 字符串变量
c = 5.20  # 浮点数变量
name_1001 = "张三"
zhangsanAge = 10
_ = "hello"
# print(_)
名字 = "张三"
# print(名字)
# 可以使用中文，不建议


# 2.变量类型与赋值
print(type(a))
print(type(b))

# 3.标识符和关键字
import keyword
print(keyword.kwlist)
