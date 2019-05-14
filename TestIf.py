#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = 1.68
weight = 70
bmi = round(weight / height ** 2, 2)

print("bmi:", bmi)

if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
