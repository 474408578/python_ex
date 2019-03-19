import sys

'''
通用异常：Exception,它可以捕获任意异常

'''
# 自定义异常
class MyExcept(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise MyExcept('我的异常')
except MyExcept as ex:
    print(ex)