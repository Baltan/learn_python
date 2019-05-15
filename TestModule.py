#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python模块就是普通的Python文件，模块名就是文件名

# 导入math模块
# import math

# 导入模块中的指定值
from math import pow

# 导入模块中的所有值，不建议这么写
# from math import *

# 重命名导入的模块
import sys as s

val_1 = pow(2, 4)

val_2 = 2 ** 4

print("val_1:", val_1)
print("val_2:", val_2)
print("val_1 == val_2:", val_1 == val_2)

print("------------------------------这是一条分割线------------------------------")

print("s.copyright", s.copyright)
