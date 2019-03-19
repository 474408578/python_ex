import threading

class MyThread(threading.Thread):
    def __init__(self, count, name):
        super(MyThread, self).__init__()
        self.count = count
        self.name = name

    def run(self):
        while self.count > 0:
            print('hello', self.name)
            self.count -= 1


def say_hi(count, name):
    print('hello', name)

def main():
    usernames = ['Bob', 'Jack', 'Pony', 'Jone', 'Mike']
    for i in range(5):
        thread = MyThread(1, usernames[i])
        thread.start()
        # print(thread.getName(), thread.isDaemon(), thread.isAlive())

if __name__ == '__main__':
    main()
