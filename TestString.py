#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r''字符串''中的内容不转义
s1 = r'Hello, \'Adam\''
s2 = r'''Hello,
Lisa!'''

print("s1:", s1)
print("s2:", s2)

print("------------------------------这是一条分割线------------------------------")

# chr()把编码转换为对应的字符
print("chr(28888):", chr(28888))
# encode()把字符串转换为指定编码的bytes
print("'ABC'.encode('ascii'):", 'ABC'.encode('ascii'))
print("'中文'.encode('utf-8'):", '中文'.encode('utf-8'))
# decode()把bytes转换为字符串，errors='ignore'忽略错误的字节
print("b'\\xe4\\xb8\\xad\\xff'.decode('utf-8', errors='ignore'):", b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

print("------------------------------这是一条分割线------------------------------")

# capitalize()把字符串转换为首字母大写
print("'baltan'.capitalize():", 'baltan'.capitalize())
# upper()把字符串转换为全部大写
print("'baltan'.upper():", 'baltan'.upper())
# lower()把字符串转换为全部小写
print("'BALTAN'.lower():", 'BALTAN'.lower())
# len()获取字符串长度
print("len('baltan'):", len('baltan'))

print("------------------------------这是一条分割线------------------------------")

# format()格式化字符串
print("{} can be {}".format("strings", "interpolated"))
print("{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick"))
print("{name} wants to eat {food}".format(name="Bob", food="lasagna"))
print("%s can be %s the %s way" % ("strings", "interpolated", "old"))
# %2d：整型，长度为2，前面补充空格
# %02d：整型，长度为2，前面补充0
print('%2d和%02d' % (3, 1))
print('%2d和%02d' % (30, 10))
print('%2d和%02d' % (30000, 10000))
# %.4f：浮点型，保留4位小数
print('%.4f' % 3.1415926)
print('%.4f' % 3.14)
print('%.4f' % 3)
# 如果字符串中有'%'，用'%%'来表示一个'%'
print('%.1f%%' % ((85 - 72) / 72 * 100))
