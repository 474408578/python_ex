from multiprocessing import Process, Queue
import os
import time
import random


# print(int(random.random() * 10))

def write(q):
    print("Process {} to write".format(os.getpid()))
    for i in ['A', 'B', 'C']:
        print('Put {} to queue'.format(i))
        q.put(i)
        time.sleep(random.random())


def read(q):
    print("Process {} to read".format(os.getpid()))
    time.sleep(5) # 为了防止还未put数据进入q, 便已经退出
    while True:
        if q.empty():
            print('read exit')
            break
        i = q.get(True)
        print("Get {} from queue".format(i))


def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    # pr.terminate()
    pr.join()


if __name__ == '__main__':
    main()
