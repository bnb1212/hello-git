import time
import threading
import multiprocessing
from multiprocessing import freeze_support



def calc_square(num_list):
    for n in num_list:
        time.sleep(0.1)

def calc_cube(num_list):
    for n in num_list:
        time.sleep(0.1)

def main():
    arr = list(range(1,11))
    # ---- serial ----
    s = time.time()
    calc_square(arr)
    calc_cube(arr)
    print("serial processing = ", time.time()-s)
    # ---- multi-threading ----
    t1 = threading.Thread(target=calc_cube, args=(arr,))
    t2 = threading.Thread(target=calc_square, args=(arr,))
    s = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("multi-threading = ", time.time()-s)
    # ---- multi-processing ---
    p1 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p2 = multiprocessing.Process(target=calc_square, args=(arr,))
    s = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("multi-processing = ", time.time()-s)

if __name__ == '__main__':
    freeze_support()
    main()

