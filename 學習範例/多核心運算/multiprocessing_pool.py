'''
Python 多核心運算

module: multiprocessing

Pool 進程池
    ** 可接收含有 return 函式 **

    Pool()
        param processes: 使用的核心數，預設為電腦所有核心數

    map( 函式 , 可疊代資料(函式參數) ,  )
    :param func: 函式
    :param iterable: 可疊代資料(函式參數)
    :param chunksize: 資料分割大小

'''

from multiprocessing import Pool, cpu_count
from time import process_time, perf_counter

def pow(x):
    return x * x


def multicore():
    # 設置只用 3 個核心運行
    pool = Pool(processes=3)

    t1 = perf_counter()
    # 取得目標函式的 回傳值
    result = pool.map(pow, (1, 2), chunksize=100)   # 方式 1
    t2 = perf_counter()
    print(result)
    print(t2 - t1)
    # result = pool.apply_async(pow, (2, ))   # 方式 2
    # print(result.get())

    # # 比較 Python 風格的寫法
    # multi_result = [pool.apply_async(pow, (i, ))for i in range(10)]
    # print([results.get() for results in multi_result])


if __name__ == "__main__":
    multicore()
    print(cpu_count())

