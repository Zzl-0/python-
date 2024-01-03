import threading
import time
import logging

def thread_function(name):
    logging.info("Thread %s: starting", name)
    # 线程休眠了2秒钟，模拟一个较短的工作负载
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt='"%H:%M:%S')
    logging.info("Main    :  before creat thread")
    # 子进程名字为 1   从threading.Thread对象启动线程
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)  # daemon=True 是开启守护进程，一般是默认的
    logging.info("Main    :  before running thread")
    # 启动子进程
    x.start()
    logging.info("Main    :  wait for the thread to finish")
    # 如果这行代码不被注释掉，主线程会等待子线程执行完毕后才会继续执行。但在注释掉的情况下，主线程会继续执行，不等待子线程。
    # x.join()
    logging.info("Main    :  all done")



'''
输出结果：
    第一次： 注释掉 x.join()
        "12:38:24: Main    :  before creat thread
        "12:38:24: Main    :  before running thread
        "12:38:24: Thread 1: starting
        "12:38:24: Main    :  wait for the thread to finish
        "12:38:24: Main    :  all done
        等待两秒之后显示（主程序未等待子程序完成，先结束
        "12:38:26: Thread 1: finishing
        
    第二次：  未注释
        "12:39:52: Main    :  before creat thread
        "12:39:52: Main    :  before running thread
        "12:39:52: Thread 1: starting
        "12:39:52: Main    :  wait for the thread to finish
        等待两秒之后显示（主程序等待子程序完成后，才完成）
        "12:39:54: Thread 1: finishing
        "12:39:54: Main    :  all done
        
    第三次：  在创建子进程时添加daemon守护线程为True
        "12:46:25: Main    :  before creat thread
        "12:46:25: Main    :  before running thread
        "12:46:25: Thread 1: starting
        "12:46:25: Main    :  wait for the thread to finish
        "12:46:25: Main    :  all done
        直接结束，未等待两秒
        
        文档解释：thread_function()没有机会完成。它是一个daemon线程，因此当__main__到达其代码末尾并且程序想要结束时，守护进程被终止。
                未注释join()的话，就是告诉另一个线程，等该线程结束在结束，（有守护线程也是一样）
'''