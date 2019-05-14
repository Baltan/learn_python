#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 元素必须是不可变对象
some_set = set()
# other_set = set((3, 4, 5, 6))或other_set = set([3, 4, 5, 6])不会抛出TypeError
# other_set = set((1, 2, [1, 2, 3]))会抛出TypeError
other_set = {3, 4, 5, 6}
print("some_set:", some_set)
some_set = {1, 1, 2, 2, 3, 4}
print("some_set:", some_set)
some_set.add(5)
some_set.add((7, 8, 9))
some_set.add((10, 11))
# 抛出TypeError，列表不是不可变对象
# some_set.add([7, 8, 9])
print("some_set:", some_set)
# remove()移除指定的元素，移除不存在的元素会抛出KeyError
some_set.remove(1)
some_set.remove((10, 11))
print("some_set:", some_set)
print("other_set:", other_set)

print("------------------------------这是一条分割线------------------------------")

# 取交集
print("some_set & other_set:", some_set & other_set)
# 取并集
print("some_set | other_set:", some_set | other_set)
# 取补集
print("some_set - other_set:", some_set - other_set)

print("------------------------------这是一条分割线------------------------------")

# in判断某个值在不在集合中
print("1 in some_set:", 1 in some_set)
print("7 in some_set", 7 in some_set)
