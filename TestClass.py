#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    # 类属性
    species = "Person"
    # 类的私有属性，在类外部无法直接进行访问
    __secret = "个人隐私"

    # 构造方法
    def __init__(self, age, name="无名氏"):
        self.name = name
        self.age = age

    # 实例方法，第一个参数是self（可自定义参数名），指向当前实例
    def introduce_myself(self):
        print("我叫{}，今年{}岁，我是一个Human being。".format(self.name, self.age))

    # 类方法，第一个参数是cls（可自定义参数名），指向当前类
    @classmethod
    def show_species(cls):
        print("我们是{}。".format(cls.species))

    @classmethod
    def show_secret(cls):
        print("{}".format(cls.__secret))

    # 静态方法，调用时没有实例或类的绑定。
    @staticmethod
    def greet():
        print("你好。")


print("------------------------------这是一条分割线------------------------------")

zs = Person(20, "张三")
zs.introduce_myself()
# Person.show_species()
zs.show_species()
# Person.show_secret()
zs.show_secret()
# Person.greet()
zs.greet()

no_name = Person(22)
no_name.introduce_myself()

print("------------------------------这是一条分割线------------------------------")

Person.species = "Genius"

zs.show_species()
no_name.show_species()

print("------------------------------这是一条分割线------------------------------")


# Teacher类继承Person类，如果是继承其他模块中的类，写成"ModuleName.ClassName"，
# Python支持多继承，若是基类中有相同的方法名，而在子类中为重写，从左到右查找基类中是否包含此方法
class Teacher(Person):
    # 构造方法
    def __init__(self, age, name):
        self.name = name
        self.age = age

    # 实例方法，第一个参数是self（可自定义参数名），指向当前实例
    def introduce_myself(self):
        # 子类对象调用父类对象被重写的方法
        super().introduce_myself()
        print("我叫{}，今年{}岁，我是一个Teacher。".format(self.name, self.age))
        self.__praise_myself()

    # 类的私有方法，只能在类内部调用
    def __praise_myself(self):
        print("我德艺双馨。")


print("------------------------------这是一条分割线------------------------------")

cjm = Teacher(30, "苍井满")
cjm.show_species()
cjm.show_secret()
cjm.introduce_myself()
# 子类对象调用父类对象被重写的方法
super(Teacher, cjm).introduce_myself()
cjm.greet()

print("------------------------------这是一条分割线------------------------------")

# 类的帮助信息
print("Person.__doc__:", Person.__doc__)
print("Person.__class__:", Person.__class__)
print("no_name.__class__:", no_name.__class__)
