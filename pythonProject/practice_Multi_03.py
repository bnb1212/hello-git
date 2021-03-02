import time
import threading
import multiprocessing
from multiprocessing import freeze_support

arr = [1,2,3,4,5]
shared_q = multiprocessing.Queue()

def calc_square(num_list, q):
    for idx, n in enumerate(num_list):
        q.put(n * n)

def main():
    p1 = multiprocessing.Process(target=calc_square, args=(arr, shared_q))
    p2 = multiprocessing.Process(target=calc_square, args=(arr, shared_q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("--- q_print --- ")
    while not shared_q.empty():
        print(shared_q.get(), end=', ')

if __name__ == '__main__':
    freeze_support
    main()
