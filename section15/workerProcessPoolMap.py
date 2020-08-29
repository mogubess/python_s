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
        r = p.map(worker1, [100, 300])  # ASYNC処理をまとめた機能
        # 両方のプロセスから結果が戻ってきたら次の処理に進む
        logging.debug('executed')
        logging.debug(r)

        r = p.imap(worker1, [100, 300])  # イテレータで戻り値を決める
        # 両方のプロセスから結果が戻ってきたら次の処理に進む
        logging.debug('executed')
        logging.debug([i for i in r])
        # p1 = p.apply_async(worker1, (100,))
        # p2 = p.apply_async(worker1, (100,))
        # logging.debug('executed')
        # logging.debug(p1.get())  # timeoutを設定できる
        # logging.debug(p2.get())
