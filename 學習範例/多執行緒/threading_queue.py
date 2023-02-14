'''
Python 多執行緒

處理 有 return 函式

在多執行緒處理是不能 return 的，因此用 Queue 的方法取得 返回值

'''

import threading
from time import *
from queue import Queue


def list_pow(ls: list, queue):
    for i in range(len(ls)):
        ls[i] = ls[i] ** 2

    queue.put(ls)   # 此處不用 return，改用 queue.put() 儲存結果值

def multiple_Reading(data):
    queue = Queue()
    threads = []

    quantity = 4    # 總線程數
    for i in range(quantity):
        working = threading.Thread(target=list_pow, args=(data[i], queue))
        working.start()
        threads.append(working)

    for i in range(quantity):
        threads[i].join()
    
    results = []
    for i in range(quantity):
        results.append(queue.get())
    
    print(results)

start = perf_counter()
multiple_Reading([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
end = perf_counter()

# 執行總時長
print(end - start)


