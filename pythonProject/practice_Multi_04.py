import time
import threading
import multiprocessing
from multiprocessing import freeze_support
from multiprocessing import Pool

def calc_square(n):
    time.sleep(0.1)
    return n* n

arr =list(range(1,11))

def serial_p():
    s = time.time()
    result = list(map(calc_square, arr))
    print(result)
    print(time.time() - s)


def multi_p():
    s = time.time()
    p = Pool()
    result = p.map(calc_square, arr)
    p.close()
    p.join()
    print(result)
    print(time.time()-s)

if __name__ == '__main__':
    freeze_support
    serial_p()
    multi_p()

