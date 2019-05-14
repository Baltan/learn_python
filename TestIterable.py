#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filled_dict = {"one": 1, "two": 2, "three": 3}
# keys_iterable是一个实现可迭代接口的对象
keys_iterable = filled_dict.keys()
# values_iterable = filled_dict.values()
print("keys_iterable:", keys_iterable)

print("------------------------------这是一条分割线------------------------------")

for key in keys_iterable:
    print(key)

print("------------------------------这是一条分割线------------------------------")

# 抛出TypeError，可迭代对象不可以随机访问
# print(keys_iterable[0])

# 生成迭代器
key_iterator = iter(keys_iterable)
print("key_iterator.__next__():", key_iterator.__next__())
print("key_iterator.__next__():", key_iterator.__next__())
print("key_iterator.__next__():", key_iterator.__next__())
# 抛出StopIteration
# print("key_iterator.__next__():", key_iterator.__next__())

print("------------------------------这是一条分割线------------------------------")

print("list(keys_iterable):", list(keys_iterable))
print("set(keys_iterable):", set(keys_iterable))
print("tuple(keys_iterable):", tuple(keys_iterable))
