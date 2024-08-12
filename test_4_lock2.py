import multiprocessing as mp

manager = mp.Manager()
count = manager.Value("i", 0)
lock = manager.Lock()


def increment_value(num):
    for _ in range(num):
        # with lock:
        count.value += 1  # 共享变量的自增操作


#  MOV R1, [0x4000]    ; 将内存地址 0x4000 处的值加载到寄存器 R1 中
#  ADD R1, R1, #1      ; 将寄存器 R1 的值加 1
#  MOV [0x4000], R1    ; 将寄存器 R1 中的值存回内存地址 0x4000


if __name__ == "__main__":
    # 创建一个Manager对象，并从中创建一个共享的Value对象，初始值为0

    # 定义要运行的进程数量和每个进程的自增次数
    num = 100

    # 创建多个进程
    processes = []
    for _ in range(8):
        process = mp.Process(target=increment_value, args=(num,))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    # 打印最终的共享变量的值
    print(f"Final value: {count.value}")


##
