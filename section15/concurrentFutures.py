import multiprocessing
import time
import logging
import concurrent.futures

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker(x, y):
    logging.debug('worker start')
    r = x * y
    logging.debug(r)
    logging.debug('worker end')
    return r


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # f1 = executor.submit(worker, 2, 5)
        # f2 = executor.submit(worker, 2, 5)
        # logging.debug(f1.result())
        # logging.debug(f2.result())

        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


if __name__ == '__main__':
    main()
