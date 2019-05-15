#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_generator(iterable):
    for i in iterable:
        yield 2 ** i


ranges = range(1, 900000000)

for i in my_generator(ranges):
    print(i)
    if i >= 1000000:
        break
