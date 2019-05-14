#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# key必须是不可变对象
# filled_dict = {[1, 2, 3]: 'list'}抛出TypeError
filled_dict = {"one": 1, "two": 2, "three": 3}
print("filled_dict:", filled_dict)
# keys()获得所有的键
print("list(filled_dict.keys()):", list(filled_dict.keys()))
# values()获得所有的值
print("list(filled_dict.values()):", list(filled_dict.values()))

print("------------------------------这是一条分割线------------------------------")

# in判断某个键在不在字典中
print("'one' in filled_dict:", 'one' in filled_dict)
print("'four' in filled_dict:", 'four' in filled_dict)

print("------------------------------这是一条分割线------------------------------")

# 抛出KeyError，访问不存在的键
# filled_dict["four"]
print("filled_dict[\"one\"]:", filled_dict["one"])
# get()不会抛出KeyError，访问不存在的键默认返回None，可以设置返回的默认值
print("filled_dict.get('one'):", filled_dict.get('one'))
print("filled_dict.get('four'):", filled_dict.get('four'))
print("filled_dict.get('four', 4):", filled_dict.get('four', 4))

print("------------------------------这是一条分割线------------------------------")

# setdefault()只有当键不存在的时候插入新值
filled_dict.setdefault('five', 5)
print("filled_dict.get('five'):", filled_dict.get('five'))
filled_dict.setdefault('five', 6)
print("filled_dict.get('five'):", filled_dict.get('five'))
# 字典赋值
filled_dict.update({"six": 6})
print("filled_dict:", filled_dict)
filled_dict["seven"] = 7
print("filled_dict:", filled_dict)
# del删除字典中指定的键
del filled_dict["one"]
print("filled_dict:", filled_dict)
# pop()删除字典中指定的键
filled_dict.pop('two')
print("filled_dict:", filled_dict)
