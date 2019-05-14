#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tup = (1,)，定义只有一个元素的tuple必须须加一个逗号，防止和小括号混淆
tup = (1, 2, 4, 3)
other_tup = (4, 5, 6)
print("tup:", tup)
print("tup[0]:", tup[0])
print("tup[-2]:", tup[-2])
# 抛出TypeError，元组是不可变的
# tuple[0] = 3

print("------------------------------这是一条分割线------------------------------")

# tuple[始:终:步伐]
print("tup[1:3]:", tup[1:3])
print("tup[2:]:", tup[2:])
print("tup[:3]:", tup[:3])
print("tup[::2]:", tup[::2])
# 倒序排列元组
print("tup[::-1]:", tup[::-1])
print("tup[:]:", tup[:])

print("------------------------------这是一条分割线------------------------------")

# 两个列表相加，原来的列表都不变
union_tup = tup + other_tup
print("tup:", tup)
print("other_tup:", other_tup)
print("union_tup:", union_tup)

print("------------------------------这是一条分割线------------------------------")

# in判断某个元素在不在列表中
print("6 in union_tup:", 6 in union_tup)
print("7 in union_tup:", 7 in union_tup)
# len()获取列表长度
print("len(union_tup):", len(union_tup))

print("------------------------------这是一条分割线------------------------------")

# 把元组解包赋值给变量
tup_a, tup_b, tup_c = (1, 2, 3)
print("tup_a:", tup_a)
print("tup_b:", tup_b)
print("tup_c:", tup_c)
# 元组周围的括号可以省略
# 无关闭分隔符：任意无符号的对象，以逗号隔开，默认为元组
tup_d, tup_e, tup_f = 4, 5, 6
print("tup_d:", tup_d)
print("tup_e:", tup_e)
print("tup_f:", tup_f)
# 交换两个变量
tup_e, tup_f = tup_f, tup_e
print("tup_e:", tup_e)
print("tup_f:", tup_f)
