import time
from multiprocessing import Pool


def task_short(num):
    time.sleep(3)
    print("I am short task: {0}\n".format(num))

def task_long(num):
    while True:
        print("I am task: {0}\n".format(num))
        time.sleep(2)

def main():
    pool = Pool(processes=5)
    # pool.apply(task_short, args=(10, ))
    pool.apply_async(task_short, args=(10, ))

    pool.map(task_long, range(10))
    # pool.map_async(task_long, range(10))
    # pool.close()
    # pool.join()
    print("main process")

if __name__ == '__main__':
    main()

'''
apply 单个任务同步
apply_async 单个任务异步
map 多个任务同步
map_async 多个任务异步 其中不带async的方法都会阻塞到任务完成，才会继续运行其后的代码。    
'''