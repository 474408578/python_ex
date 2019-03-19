


def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b # yield返回表达式的值，默认为None
        a, b = b, a+b
        i += 1

def main_fib():
    # for loop 调用next()方法
    for i in fib(10):
        print(i)

# 生成器----->协程
def simple_coroutine():
    print('启动协程')
    y = 10
    x = yield y
    print('协程接受到了x的值:{}'.format(x))

def main_simple_coroutine():
    my_coro = simple_coroutine()
    ret = next(my_coro)
    print(ret)
    my_coro.send(20)

if __name__ == '__main__':
    # main_fib()
    main_simple_coroutine()