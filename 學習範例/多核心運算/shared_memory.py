'''
Python 多核心運算

module: multiprocessing

共享內存 (shared memory)

    1. Value(): 第一個參數宣告資料型別，第二個則是共享參數值
    2. Array(): 第一個參數宣告資料型別，第二個是放 list 共享資訊
 
        注意: 這裡的 Array 與 Numpy 不同，只能是一維，不能是多維的形式

各參數的型別代表 如下表  (source: https://docs.python.org/3/library/array.html)

| Type code | C Type             | Python Type       | Minimum size in bytes |
| --------- | ------------------ | ----------------- | --------------------- |
| `'b'`     | signed char        | int               | 1                     |
| `'B'`     | unsigned char      | int               | 1                     |
| `'u'`     | Py_UNICODE         | Unicode character | 2                     |
| `'h'`     | signed short       | int               | 2                     |
| `'H'`     | unsigned short     | int               | 2                     |
| `'i'`     | signed int         | int               | 2                     |
| `'I'`     | unsigned int       | int               | 2                     |
| `'l'`     | signed long        | int               | 4                     |
| `'L'`     | unsigned long      | int               | 4                     |
| `'q'`     | signed long long   | int               | 8                     |
| `'Q'`     | unsigned long long | int               | 8                     |
| `'f'`     | float              | float             | 4                     |
| `'d'`     | double             | float             | 8                     |

'''

from multiprocessing import Process, Value, Array, Queue


def list_plus(ls, num, queue):
    for i in range(len(ls)):
        ls[i] += num
        
    queue.put(ls)


shared_value = Value('i', 1)

# 只能是 一維的方式
shared_array = Array('i', [1, 2, 3])
# 錯誤形式
# shared_value = Array('i', [[1, 2], [3, 4]])


def multicore():
    queue = Queue()
    process = Process(target=list_plus, args=([1, 2, 3], 1, queue))

    process.start()
    process.join()
    print(queue.get())
    print(shared_value)
    print(shared_array)


if __name__ == "__main__":
    multicore()



