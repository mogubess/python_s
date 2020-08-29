"""from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager)import logging
    """
import multiprocessing
import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')


# 共有メモリでは若干速度が遅い


def worker1(lll, d, n):
    lll.reverse()
    d['x'] += 1
    n.y += 1


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        lll = manager.list()
        d = manager.dict()
        n = manager.Namespace()

        lll.append(1)
        lll.append(2)
        lll.append(3)
        d['x'] = 0
        n.y = 0

        p1 = multiprocessing.Process(target=worker1, args=(lll, d, n))
        p1.start()
        p1.join()

        logging.debug(lll)
        logging.debug(d)
        logging.debug(n)
