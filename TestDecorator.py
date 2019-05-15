#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        question, answer = target_function(*args, **kwargs)
        if not answer:
            return "问题：{}\n回答：{}".format(question, "滚犊子！")
        return "问题：{}\n回答：{}".format(question, "你最美！")

    return wrapper


@beg
def ask(answer=False):
    question = "吾孰与徐公美？"
    return (question, answer)


print(ask())

print("------------------------------这是一条分割线------------------------------")

print(ask(answer=True))
