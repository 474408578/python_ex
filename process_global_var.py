import time
from multiprocessing import Process

i = 100
def plus():
    global i
    count = 1
    while True:
        print('plus >>', i)
        i = i+2
        time.sleep(1)
        if count == 5:
            break
        count = count+1


def subtract():
    global i
    count = 1
    while True:
        print('subtract >>', i)
        i = i-3
        time.sleep(1)
        if count == 5:
            break
        count = count+1

def main():
    proc1 = Process(target=plus)
    proc2 = Process(target=subtract)
    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    print(i)

if __name__ == '__main__':
    main()