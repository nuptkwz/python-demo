import threading

class SafeThread:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

def worker(counter,n):
    for _ in range(n):
        counter.increment()

counter = SafeThread()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter, 1000))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


from queue import Queue
import time

def producer(q,items):
    for item in items:
        q.put(item)
        print(f"生产: {item}")
        time.sleep(0.1)

def consumer(q):
    while True:
        item = q.get()
        if item is None: break
        print(f"消费: {item}")
        q.task_done()

q = Queue()
producer_thread = threading.Thread(target=producer, args=(q, ["A", "B", "C"]))
consumer_thread = threading.Thread(target=consumer, args=(q,))

from multiprocessing import Pool
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    # 1.输出counter
    print(counter.value)  # 输出10000（无锁时结果可能小于10000）

    # 2.
    # producer_thread.start()
    # consumer_thread.start()
    # producer_thread.join()
    # q.put(None)  # 发送结束信号
    # consumer_thread.join()
    # whith Pool(processes=4) as pool:
    #     numbers = range(1_000_000, 1_000_500)
    #     results = pool.map(is_prime, numbers)  # 自动分配任务
    #     print(f"素数数量: {sum(results)}")  # 输出47（多进程加速计算）
