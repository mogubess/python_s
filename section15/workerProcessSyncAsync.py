import multiprocessing
import time
import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('log start')
    logging.debug(i)
    time.sleep(5)
    logging.debug('log end')
    return i


if __name__ == '__main__':
    with multiprocessing.Pool(5) as p:
        # 並列化させたくないときは、apply(同期処理となるため、次に進まない)
        logging.debug(p.apply(worker1, (200, )))
        logging.debug('executed apply')
        # apply_async非同期で動作するので、次のプールもすぐに動作する
        p1 = p.apply_async(worker1, (100,))
        p2 = p.apply_async(worker1, (100,))
        logging.debug('executed')
        logging.debug(p1.get())  # timeoutを設定できる
        logging.debug(p2.get())
