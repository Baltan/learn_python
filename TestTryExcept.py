#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    # raise抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    print(e)
# 同时处理不同类的错误
except (TypeError, NameError) as e:
    print(e)
# else语句可选，必须在所有的except之后
else:
    print("All good!")

print("------------------------------这是一条分割线------------------------------")

try:
    # raise抛出异常
    raise NameError("This is an name error")
except IndexError as e:
    print(e)
# 同时处理不同类的错误
except (TypeError, NameError) as e:
    print(e)
# else语句可选，必须在所有的except之后
else:
    print("All good!")

print("------------------------------这是一条分割线------------------------------")

try:
    # pass：不做任何事情
    pass
except IndexError as e:
    print(e)
# 同时处理不同类的错误
except (TypeError, NameError) as e:
    print(e)
# else语句可选，必须在所有的except之后
else:
    print("All good!")
