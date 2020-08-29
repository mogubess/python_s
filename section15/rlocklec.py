import threading
import time
import logging

# Rlockに変えると自分のスレッドがロックしている場合のみTrueを返す

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(d, lock):
    logging.debug('log start')
    print(threading.currentThread().getName(), 'start')
    with lock:
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            i = d['x']
            d['x'] = i + 1
            logging.debug(d)
    print(threading.currentThread().getName(), 'end')


def worker2(d, lock):
    print(threading.currentThread().getName(), 'start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
    print('started')
    t1.join()
    t2.join()
