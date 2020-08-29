import threading
import time
import logging

# スレッドをDaemon化して、終わるのをjoinするプログラム

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('log start')
    print(threading.currentThread().getName(), 'start')
    time.sleep(5)
    print(threading.currentThread().getName(), 'end')


def worker2(x, y=1):
    print(threading.currentThread().getName(), 'start')
    logging.debug(x)
    logging.debug(y)
    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t1.setDaemon(True)
    t2 = threading.Thread(target=worker2, args=(100,), kwargs={'y': 200})
    t1.start()
    t2.start()
    print('started')
    t1.join()
    t2.join()
