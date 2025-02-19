import time
from string import Template
import pytest
import os
import multiprocessing
import threading

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# template_str = "Hello, $name! Welcome to $place. Lets play with $friend togther~"
# template = Template(template_str)
# data = {"name": "张三", "place": "beijing", "friend": "Kyle"}
# result = template.safe_substitute(data)
# print(result)


# def test_a():
#     pytest.assume(2 + 2 == 4)
#     pytest.assume(2 + 2 == 5)
#     pytest.assume(3 * 3 == 9)
#
# def test_b():
#     pytest.assume(2 + 2 == 4)
#
# def test_c():
#     eval("pytest.assume(2 + 2 == 5)")

def cpu_bound():
    while True:
        print(f"Worker process: {multiprocessing.current_process().name}")


glob_count = 10


def thread_worker():
    global glob_count
    for i in range(0, 10000):
        # print(f"Worker thread: {threading.current_thread().name},当前打印的数字是{i}")
        glob_count += 1
        glob_count -= 1


# if __name__ == '__main__':
#     # 创建多进程 有几个cpu 就创建几个进程 进程执行函数可以实现将cpu打满
#     num_cores = multiprocessing.cpu_count()
#     processes = []
#     for i in range(num_cores):
#         p = multiprocessing.Process(target=cpu_bound, name=f"我是进程，我的代号是{i}")
#         p.start()
#         processes.append(p)
#
#     print("主进程等待子进程结束")
#     for p in processes:
#         p.join()
#     print("主进程结束")
def subarray_sum(nums, k):
    prefix_sum = {0: 1}
    count = 0
    curr_sum = 0

    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_sum:
            count += prefix_sum[curr_sum - k]
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

    return count
if __name__ == '__main__':
    # num_cores = multiprocessing.cpu_count()
    # threads = []
    # for i in range(100):
    #     t = threading.Thread(target=thread_worker, name=f"我是线程，我的代号是{i}")
    #     t.start()
    #     threads.append(t)
    #
    # for t in threads:
    #     t.join()
    # print("主线程结束")
    # print(glob_count)
    count = subarray_sum([3,4,7,2,-3,1,4,2],7)
    print(count)


