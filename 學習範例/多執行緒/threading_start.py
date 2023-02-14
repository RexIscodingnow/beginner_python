'''
Python 多執行緒

module: threading

題外話:
    1.
    比較適合資料量小、資訊共用

    2.
    在執行大量資料時，要考慮到的一個問題
    全域直譯器鎖 (Global Interpreter Lock，簡稱 GIL)
    GIL 好比像個 "鎖頭"，一次執行只能使用一個執行緒

    因此在 GIL 的影(淫)響(威)下，對於多核心多執行緒的 CPU，會是一個效能瓶頸

                        -- python 比較臭名昭彰一點點

threading 的執行圖 (如下呈現)

                I/O              I/O       I/O
           run   |                |         |
Thread 1 ------->|                |         |
        _____________________________________
Thread 2         |--------------->|         |
        _____________________________________
Thread 3         |                |-------->|
                GIL              GIL
          release acquire  release acquire

還是會受到 GIL 的影響而有所限制

透過 CPU 不斷切換 (context-switch)，來實現平行運算的功能，但是把雙面刃
若資料量大，會因為大量的切換運算，反而造成執行速度變慢
'''

import threading

from time import sleep




# # 可使用的執行緒數目
# count = threading.active_count()
# # 列出所有可用的執行緒清單
# items = threading.enumerate()
# # 正在執行的執行緒
running_threads = threading.current_thread()

# print(count)
# print(items)
print(running_threads)


def thread_job():
    # print("這是新增的執行緒: %s" % threading.current_thread())
    print("T1 start job!")
    for i in range(10):
        sleep(0.1)
    print("T1 finish job!")

def thread_2_job():
    print("T2 start!")
    print("T2 finish!")

def pow(x, y):
    print(x ** y)


# 添加執行緒    name=命名執行緒名稱
add_thread = threading.Thread(target=thread_job, name="T1")
thread_2 = threading.Thread(target=thread_2_job, name="T2")
thread_pow = threading.Thread(target=pow, args=(2, 3), name="Pow")

# 執行添加的執行緒
add_thread.start()
thread_2.start()
thread_pow.start()

print(threading.enumerate())

# 等待該目標部分 執行完畢，才執行下一個程式
add_thread.join()
thread_2.join()
thread_pow.join()

print("all done!")



