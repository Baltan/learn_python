#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(\"\"):", bool(""))
print("bool(\" \"):", bool(" "))
print("bool([]):", bool([]))
print("bool([1]):", bool([1]))
print("bool({}):", bool({}))
print("bool({\"1\": 1}):", bool({"1": 1}))
print("bool(()):", bool(()))
print("bool((1,)):", bool((1,)))
print("bool(None):", bool(None))
print("bool(...):", bool(...))
print("bool(Ellipsis):", bool(Ellipsis))
print("True and False:", True and False)
print("True or False:", True or False)
print("not False:", not False)
