import threading

n = 1000000
balance = 0

def add(n, lock):
    global balance
    for i in range(n):
        lock.acquire()
        balance += 1
        lock.release()

def sub(n, lock):
    global balance
    for i in range(n):
        lock.acquire()
        balance -= 1
        lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    # add(n)
    # sub(n)
    # print(balance)

    t1 = threading.Thread(target=add, args=(n, lock))
    t2 = threading.Thread(target=sub, args=(n, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

    