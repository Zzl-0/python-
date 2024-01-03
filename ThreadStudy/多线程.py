import concurrent.futures
import threading
import time
import logging


def thread_function(name):
    logging.info("Thread %s: starting", name)
    # 线程休眠了2秒钟，模拟一个较短的工作负载
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO, datefmt='"%H:%M:%S')
#
#     threads = list()
#
#     for index in range(3):
#         # 添加日志
#         logging.info("Main  : creat and start thread %d .", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         print("x : ", x)
#         threads.append(x)
#         x.start()
#
#     for index, thread in enumerate(threads):
#         logging.info("Main  : before joining thread %d .", index)
#         thread.join()
#         logging.info("Main  : thread %d is done", index)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # 初始化线程池。可以指定池中的线程数，通常根据可用的处理器核心数量来选择
    # 使用 with 语句块，可以确保在线程池使用完毕后正确清理资源
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
