import asyncio
import numpy as np


# 模拟一个异步网络请求函数
async def fetch_data(id):
    print(f"Task {id}: Start fetching data...")
    await asyncio.sleep(np.random.rand() * 4)  # 模拟网络延迟
    print(f"Task {id}: Data fetched.")
    return f"Data from task {id}"


# 主函数
async def main():
    # 创建并发任务
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(4)]

    # 等待所有任务完成
    results = await asyncio.gather(*tasks)

    # 处理结果
    for result in results:
        print(result)


# 运行主函数
asyncio.run(main())
