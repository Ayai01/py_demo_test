import threading
import time
import numpy as np

# 定义全局变量
count = 0
color = ["\033[91m", "\033[92m", "\033[93m", "\033[94m"]

# 定义锁
lock = threading.Lock()


# 定义一个函数，多个线程将同时执行这个函数
def increment_counter(use_lock, th):
    global count
    for _ in range(100):
        time.sleep(np.random.rand() * 0.03)  # 模拟其他操作导致的延迟

        ##################################
        if use_lock:
            with lock:  # 使用锁保护共享变量
                temp = count  # 读取当前值
                time.sleep(np.random.rand() * 0.02)  # 模拟其他操作导致的延迟
                count = temp + 1  # 写回新值
        else:
            temp = count  # 读取当前值
            time.sleep(np.random.rand() * 0.02)  # 模拟其他操作导致的延迟
            count = temp + 1  # 写回新值
        ##################################

        print(f"{color[th]}{count}\033[0m", end=", ", flush=True)


# 主函数，分别测试加锁和不加锁的情况
def main(use_lock):
    # 记录开始时间
    start_time = time.time()

    global count
    count = 0  # 重置count
    threads = []

    for i in range(4):
        thread = threading.Thread(target=increment_counter, args=(use_lock, i))
        threads.append(thread)
        thread.start()
        time.sleep(0.01)

    for thread in threads:
        thread.join()

    # 记录结束时间
    end_time = time.time()

    # 计算并打印执行时间
    elapsed_time = end_time - start_time
    print(f"\nFinal count value (use_lock={use_lock}): {count}")
    print(f"Execution time: {elapsed_time:.4f} seconds")


# 测试不加锁的情况
main(use_lock=False)

print("-" * 60)
