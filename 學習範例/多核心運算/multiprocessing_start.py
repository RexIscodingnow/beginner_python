'''
Python 多核心運算

module: multiprocessing

'''

from multiprocessing import *


def add(num1, num2, queue):
    result = num1 + num2
    # print(result)
    queue.put(result)

def job(queue):
    result = 0
    for i in range(10000):
        result += i
    # print(result)
    queue.put(result)

# 判斷式 if __name__ == "__main__": 必要設置
if __name__ == "__main__":
    queue = Queue()
    process_1 = Process(target=add, args=(1, 2, queue))
    process_2 = Process(target=job, args=(queue, ))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    result_1 = queue.get()
    result_2 = queue.get()
    print(result_1)
    print(result_2)


