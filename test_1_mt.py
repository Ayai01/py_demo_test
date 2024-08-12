import threading
import time


# 定义一个函数，用于模拟下载文件的任务
def download_file(url, destination):
    start_time = time.time()
    print(f"[{time.strftime('%H:%M:%S', time.localtime(start_time))}] Start downloading from {url} to {destination}")
    time.sleep(2)  # 模拟下载需要2秒钟
    print(f"[{time.strftime('%H:%M:%S', time.localtime())}] Download completed for {url}")


# 定义一个主函数来创建和管理线程
def main():
    files_to_download = [
        ("http://example.com/file1.zip", "/local/path/file1.zip"),
        ("http://example.com/file2.zip", "/local/path/file2.zip"),
        ("http://example.com/file3.zip", "/local/path/file3.zip"),
    ]

    threads = []
    start_time = time.time()

    for url, destination in files_to_download:
        thread = threading.Thread(target=download_file, args=(url, destination))
        threads.append(thread)
        thread.start()  # 启动线程

    for thread in threads:
        thread.join()  # 等待所有线程结束

    total_time = time.time() - start_time
    print(f"All downloads completed in {total_time:.2f} seconds")


# 调用主函数
if __name__ == "__main__":
    main()
