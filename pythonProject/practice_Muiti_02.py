import time
import threading
import multiprocessing
from multiprocessing import freeze_support

arr = [1,2,3,4,5]
global_result = []
shared_memory = multiprocessing.Array('i', len(arr))

def calc_square(num_list, result):
    for idx, n in enumerate(num_list):
        result[idx] = n * n
        #global_result.append(n * n)
    # print('내부 print-global 변수영역: ', global_result)

def main():
    p1 = multiprocessing.Process(target=calc_square, args=(arr, shared_memory))
    p1.start()
    p1.join()

    # print("외부 print-global 변수 영역: ", global_result)
    print('shared memory: ', shared_memory[:])
if __name__ == '__main__':

    # calc_square(arr)
    main()

