#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

"""
参数列表组合的顺序必须是：位置参数、默认参数、可变参数、命名关键字参数、关键字参数
"""


# 计算矩形面积
# width的值如果在函数调用时没有传入，默认为4，默认参数在必选参数后面
def area(length, width=4):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width


# 必备参数（位置参数）调用函数
# 实参的数量必须和形参一致，否则抛出TypeError
# 实参类型如果不符合函数要求，也会抛出TypeError
print("area(5, 3) =", area(5, 3))
# 关键字参数调用函数，实参的顺序可以和形参不一致，Python 解释器能够用参数名匹配参数值
print("area(width=3, length=5) =", area(width=3, length=5))
# 默认参数调用
print("area(6) =", area(6))

print("------------------------------这是一条分割线------------------------------")


# 默认参数的陷阱
# Reference: https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888


def add_end(L=[]):
    L.append('END')
    return L


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
print("add_end([1, 2, 3]) =", add_end([1, 2, 3]))
print("add_end(['x', 'y', 'z']) =", add_end(['x', 'y', 'z']))
print("add_end() =", add_end())
print("add_end() =", add_end())
print("add_end() =", add_end())


# 定义默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print("add_end([1, 2, 3]) =", add_end([1, 2, 3]))
print("add_end(['x', 'y', 'z']) =", add_end(['x', 'y', 'z']))
print("add_end() =", add_end())
print("add_end() =", add_end())
print("add_end() =", add_end())

print("------------------------------这是一条分割线------------------------------")


def show_languages(*languages):
    # 函数内部解析成元组
    # print(isinstance(languages, tuple))
    for language in languages:
        print(language)


# 不定长参数（可变函数）调用
show_languages("Java", "JavaScript", "Python")
# 在一个iterable前加"*"表示把其中的所有元素当做可变参数传入函数
show_languages(*("C", "C++", "C#"))
show_languages(*["Ruby", "Swift", "Objective-C"])
show_languages(*{"Lisp", "Go", "PHP"})

print("------------------------------这是一条分割线------------------------------")


def show_personal_info(**infos):
    # 函数内部解析成字典
    # print(isinstance(infos, dict))
    print(infos)


# 关键字参数调用
show_personal_info(name="张三", age=20, gender="男")
# 传入函数的是字典的一份拷贝，对字典的修改不会影响原有字典对象
show_personal_info(**{"name": "李四", "age": 21, "gender": "男"})

print("------------------------------这是一条分割线------------------------------")


# 命名关键字参数调用，分隔符"*"后面的参数是命名关键字参数
# 如果参数列表中有可变参数了，后面的命名关键字参数前不需要分隔符"*"
# 只能传入指定参数名的参数
def show_discriptions(*, color="yellow", size):
    print("color:", color)
    print("size:", size)


# 命名关键字参数必须传入参数名
show_discriptions(color="red", size=500)
show_discriptions(**{"color": "green", "size": 400})
show_discriptions(size=300)

print("------------------------------这是一条分割线------------------------------")

x = 10


# 修改局部作用域变量
def change_local_variable():
    x = 5
    print("x:", x)
    x = 6
    print("x:", x)


change_local_variable()
print("x:", x)


# 修改全局作用域变量
def change_global_variable():
    global x
    x = 5
    print("x:", x)


change_global_variable()
print("x:", x)

print("------------------------------这是一条分割线------------------------------")


def create_func():
    def func():
        print("函数内部可以返回函数")

    return func


create_func()()

print("------------------------------这是一条分割线------------------------------")

# 计算圆的周长
# 匿名函数，lambda函数
circumference = lambda radius: 2 * math.pi * radius

print("circumference(1) =", circumference(1))

print("(lambda x: x > 2)(3) =", (lambda x: x > 2)(3))

print("------------------------------这是一条分割线------------------------------")

circle_circumference_values = []
# map()：Pyhton2.x 返回列表，Python3.x 返回迭代器对象
map_results = map(circumference, [1, 2, 3, 4])
print("type(map_results):", type(map_results))
for result in map_results:
    circle_circumference_values.append(result)
    print(result)

# filter()：Pyhton2.x 返回列表，Python3.x 返回迭代器对象
filter_results = filter(lambda value: value > 15, circle_circumference_values)
print("type(filter_results):", type(filter_results))
for result in filter_results:
    print(result)

print("------------------------------这是一条分割线------------------------------")

# 列表推导式
print("[circumference(i) for i in [1, 2, 3]]:", [circumference(i) for i in [1, 2, 3]])
print("[x for x in [3, 4, 5, 6, 7] if x > 5]:", [x for x in [3, 4, 5, 6, 7] if x > 5])

print("------------------------------这是一条分割线------------------------------")


# 一元二次方程求根公式，返回值是一个元组
def quadratic(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


roots = quadratic(1, 0, -4)
print("roots:", roots)
print("x1 =", roots[0])
print("x2 =", roots[1])

print("------------------------------这是一条分割线------------------------------")


# 乘法运算
def product(*x):
    if not x:
        raise TypeError()
    res = 1
    for v in x:
        res *= v
    return res


# print(product())
print(product(5))
print(product(5, 6))
print(product(5, 6, 7))
print(product(5, 6, 7, 9))

print("------------------------------这是一条分割线------------------------------")


# 汉诺塔
def hanoi(n, a, b, c):
    # 如果只有一个片，直接从a柱移到c柱
    if n == 1:
        print(a, '-->', c)
    # 如果有n(n>1)个片，先把a柱上面的n-1个片从a柱移到b柱，
    # 再把a柱最下面的片移到c柱，
    # 最后把b柱的n-1个片移到c柱
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)


hanoi(4, 'A', 'B', 'C')

print("------------------------------这是一条分割线------------------------------")


# 删除字符串两段的空格
def my_trim(s):
    if len(s) == 0:
        return s
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]
    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    return s


print(my_trim(""))
print(my_trim(" "))
print(my_trim(" a"))
print(my_trim("a "))
print(my_trim(" a "))
print(my_trim("        a         "))
