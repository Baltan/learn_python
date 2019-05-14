#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

print("------------------------------这是一条分割线------------------------------")

sum = 0

for x in range(5, 10):
    sum += x

print("sum:", sum)

print("------------------------------这是一条分割线------------------------------")

for i in range(0, 15, 2):
    if i == 10:
        # pass：不做任何事情
        pass
        print("has passed")
    else:
        print(i)
