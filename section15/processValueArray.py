"""from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager)import logging
    """
import multiprocessing
import logging
import time

# プロセスセーフに値を共有する方法
# 共有メモリでは若干速度が早い

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')


def f(num, arr):
    logging.debug(num)
    num.value += 1.0
    logging.debug(arr)
    for i in range(len(arr)):
        arr[i] *= 2


if __name__ == '__main__':
    # これらの共有オブジェクトは、プロセスセーフでありスレッドセーフ
    num = multiprocessing.Value('f', 0.0)
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])

    p1 = multiprocessing.Process(target=f, args=(num, arr))
    p2 = multiprocessing.Process(target=f, args=(num, arr))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    logging.debug(num.value)
    logging.debug(arr[:])
