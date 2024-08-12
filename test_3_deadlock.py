import threading
import time

# 创建两把锁
lock1 = threading.Lock()
lock2 = threading.Lock()


# 线程1 尝试按顺序获取锁
def thread1_routine():
    print("Thread 1: trying to acquire lock 1...")
    with lock1:
        print("Thread 1: acquired lock 1, now trying to acquire lock 2...")
        time.sleep(1)  # 模拟某些操作的延迟
        with lock2:
            print("Thread 1: acquired lock 2")


# 线程2 尝试按相反的顺序获取锁
def thread2_routine():
    print("Thread 2: trying to acquire lock 2...")
    with lock2:
        print("Thread 2: acquired lock 2, now trying to acquire lock 1...")
        time.sleep(1)  # 模拟某些操作的延迟
        with lock1:
            print("Thread 2: acquired lock 1")


# 创建并启动线程
thread1 = threading.Thread(target=thread1_routine)
thread2 = threading.Thread(target=thread2_routine)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads completed (this message may never print if deadlock occurs)")
