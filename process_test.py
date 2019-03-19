import os
import time
from multiprocessing import Process


def double(number):
    result = number * 2
    process = os.getpid()
    print('{0} double to {1} by process id: {2}'.format(number, result, process))
    time.sleep(5)


def main():
    numbers = [5, 10, 15, 20, 25]
    processes = []
    for _, number in enumerate(numbers):
        process = Process(target=double, args=(number,))
        processes.append(process)
        process.start()
        print(process.is_alive())

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
