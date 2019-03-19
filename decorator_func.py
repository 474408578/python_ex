def outer(func):
    def inner():
        print('认证成功')
        result = func()
        print('日志添加成功')
        return result
    return inner

@outer
def f1():
    print('业务部门1数据接口')
    return 123


a = f1()
print(a)