import threading
import time
import logging

# セマフォの動作確認

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(semaphore):

    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

    print(threading.currentThread().getName(), 'end')


def worker2(semaphore):

    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

    print(threading.currentThread().getName(), 'end')


def worker3(semaphore):

    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    d = {'x': 0}
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore,))
    t2 = threading.Thread(target=worker2, args=(semaphore,))
    t3 = threading.Thread(target=worker3, args=(semaphore,))
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
