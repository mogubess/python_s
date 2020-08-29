import threading
import time
import logging
import queue

# キューの動作確認、queueにつまっているデータを全部確認して通知することを確認する
# join() -> task_done()

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1(queue):

    logging.debug('start')
    # queue.put(100)  # [100,200]
    # time.sleep(5)
    # queue.put(200)
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug('longggggggggggggggggggggggggggggggggg')
    logging.debug('end')


def worker2(queue):

    logging.debug('start')
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end')

    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(100000):
        queue.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)
    logging.debug('tasks are not done')

#    t1 = threading.Thread(target=worker1, args=(queue,))
#    t2 = threading.Thread(target=worker2, args=(queue,))

#    t1.start()
    queue.join()
    logging.debug('task are done')
    for _ in range(len(ts)):
        queue.put(None)
#    queue.put(None)
#    t2.start()

    [t.join() for t in ts]  # 内包リスト書式
