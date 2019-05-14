#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# is比较两个对象是否指向同一个变量
print("0 == 0:", 0 == 0)
print("0 is 0:", 0 is 0)
print("\"abc\" == \"abc\":", "abc" == "abc")
print("\"abc\" is \"abc\"", "abc" is "abc")
print("True == True:", True == True)
print("True is True:", True is True)
print("None == None:", None == None)
print("None is None:", None is None)
print("[1, 2, 3] == [1, 2, 3]:", [1, 2, 3] == [1, 2, 3])
print("[1, 2, 3] is [1, 2, 3]:", [1, 2, 3] is [1, 2, 3])
print("(1, 2, 3) == (1, 2, 3):", (1, 2, 3) == (1, 2, 3))
# (1, 2, 3) is (1, 2, 3)： Python2返回False，Python3返回True
print("(1, 2, 3) is (1, 2, 3):", (1, 2, 3) is (1, 2, 3))
print("{1, 2, 3} == {1, 2, 3}:", {1, 2, 3} == {1, 2, 3})
print("{1, 2, 3} is {1, 2, 3}:", {1, 2, 3} is {1, 2, 3})
print("{1, 2, 3} == {1, 2, 3, 2, 1}:", {1, 2, 3} == {1, 2, 3, 2, 1})
print("{1, 2, 3} is {1, 2, 3, 2, 1}:", {1, 2, 3} is {1, 2, 3, 2, 1})
