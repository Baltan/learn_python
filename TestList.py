#!/usr/bin/env python3
# -*- coding: utf-8 -*-

li = []
other_li = [4, 5, 6]
copy_li = other_li.copy()
multiple_li = other_li * 3
li.append(1)
li.append(2)
li.append(3)
li.insert(2, 4)
print("li:", li)
# pop()删除列表队尾元素，pop(i)删除指定位置元素
print("li.pop():", li.pop())
print("li:", li)
li.append(3)
print("li:", li)
print("li.pop(0):", li.pop(0))
print("li:", li)
li.insert(0, 1)
print("li:", li)
print("other_li:", other_li)
print("copy_li:", copy_li)
copy_li[0] = 40
print("other_li:", other_li)
print("copy_li:", copy_li)
copy_li.sort()
print("copy_li:", copy_li)
copy_li.reverse()
print("copy_li:", copy_li)
print("multiple_li:", multiple_li)

print("------------------------------这是一条分割线------------------------------")

print("li[0]:", li[0])
print("li[-2]:", li[-2])
# li[始:终:步伐]
print("li[1:3]:", li[1:3])
print("li[2:]:", li[2:])
print("li[:3]:", li[:3])
print("li[::2]:", li[::2])
# 倒序排列列表
print("li[::-1]:", li[::-1])
print("li[:]:", li[:])

print("------------------------------这是一条分割线------------------------------")

# 两个列表相加，原来的列表都不变
union_li = li + other_li
print("li:", li)
print("other_li:", other_li)
print("union_li:", union_li)

print("------------------------------这是一条分割线------------------------------")

# extend()将一个列表追加到另一个列表后面
li.extend(other_li)
print("li:", li)
print("other_li:", other_li)

print("------------------------------这是一条分割线------------------------------")

# in判断某个元素在不在列表中
print("6 in li:", 6 in li)
print("7 in li:", 7 in li)
# len()获取列表长度
print("len(li):", len(li))
# del删除列表中指定索引的元素
del li[-1]
print("li:", li)
