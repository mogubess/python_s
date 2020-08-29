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
    # threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
        # threads.append(t)

    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()
