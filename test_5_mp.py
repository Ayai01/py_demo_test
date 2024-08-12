import multiprocessing
import numpy as np


# 定义一个工作函数，用于计算数字的平方
def worker(num):
    result = num * num
    print(f"Process {multiprocessing.current_process().name[-1]} : {num}^2 = {result}")
    return result


if __name__ == "__main__":
    # 创建一个进程池，指定进程数量
    with multiprocessing.Pool(processes=4) as pool:
        # 定义要处理的数字列表
        numbers = np.arange(100)

        # 使用进程池的map方法，将任务分配给多个进程
        results = pool.map(worker, numbers)

    # 输出所有结果
    print(f"Final results: {results}")
