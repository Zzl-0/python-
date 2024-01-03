# 一次只允许一个线程进入代码的读取——修改——写入部分， mutex （互斥量）
import concurrent.futures
import logging
import threading
import time


'''
当两个或多个线程访问共享数据或资源时，可能会出现竞争条件。
在此示例中，您将创建每次都会发生的大型竞争条件，但请注意，大多数竞争条件并不那么明显。
通常，它们很少发生，并且会产生令人困惑的结果。正如您可以想象的那样，这使得它们非常难以调试。
幸运的是，这种竞争条件每次都会发生，您将详细了解它以解释发生的情况。
'''


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: strating update", name)
        # 添加Lock的日志
        logging.debug("Thread %s about to lock ", name)

        with self._lock:
            logging.debug("Thread %S has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s : finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d .", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            # submit() 方法用于向线程池提交一个可调用对象（函数或方法）以进行并发执行。
            # submit() 方法返回一个 concurrent.futures.Future 对象，
            # 它代表将来某个时间完成的任务，并且允许您跟踪任务的状态和获取其结果
            executor.submit(database.update, index)
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("testing update. Ending value is %d . ", database.value)
