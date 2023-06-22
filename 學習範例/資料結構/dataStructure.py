'''
Python 資料結構: 執行區

        Chapter                File Name
   __________________________________________
    1. Array (陣列)       => unit_1_array.py
    2. List (串列)        => unit_2_list.py
    3. Stack (堆疊)       => unit_3_stack.py
    4. Queue (佇列)       => unit_4_queue.py
    5. Tree (樹狀結構)    => unit_5_tree.py
    6. Graph (圖形結構)
    7. Sorting (排序)     => unit_7_sort.py     (後續: algorithm 學習)
    8. Search (搜尋)      => unit_8_search.py   (後續: algorithm 學習)
    9. experiment (實驗)  => experiment.py
'''

import numpy as np
import random

from time import *
from unit_1_array import ArrayOperation, Row_Column
from unit_2_list import Sequential_List, Linked_List
from unit_3_stack import Stack, Stack_Example, Recursion_Example, Stack_ByList
from unit_4_queue import Queue, LineUp, Circular_Queue
from unit_5_tree import BinarySearchTree
from unit_7_sort import Sorting
from unit_8_search import Search, HashTable, HashMap




# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

if __name__ == "__main__":
    ''' Array '''
    # array_1 = Row_Column(0, 2, 3, int)

    # array_1.arrange(1)
    # array_2 = Row_Column(0, 2, 3, int)
    # array_2 = array_2.arrange(7)
    # print(array_2)

    # matrixAdd = array_1.matrixAdd(array_2)
    # print(matrixAdd)

    # testing_arr = Row_Column(row=5, dtype=int)
    # testing_arr.custom_array([89, 34, 23, 78, 67])
    # testing_arr.rand()
    # result = testing_arr.selection_sort()
    # print(testing_arr.array)


    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------

    ''' Linked List '''
    # seq_ls = Sequential_List()
    # seq_ls.list_array()

    # Linked List
    
    ls_node = Linked_List()
    # # ls_node.listNode_Example()

    # for i in range(6):
    #     ls_node.addBack(i+1)

    # for i in range(6, 10):
    #     ls_node.addFront(i+1)

    # ls_node.printNode()
    # print("----------------------------")
    # ls_node.delete(6)
    # ls_node.insert(10, 4)
    # ls_node.printNode()


    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------

    ''' Stack '''
    # stack_1 = Stack_Example()
    # stack_1.common_operation()

    recursion = Recursion_Example()

    # n = int(input("費氏數列 n => "))

    # result = recursion.fibonacci_sequence(n, "loop")
    # print("費氏數列:", result)

    # n = int(input("factorial number => "))
    # result = recursion.factorial(n)
    # print(n, "!")
    # print(result)

    # data = [22, 44, 77, 88, 99]
    # res = recursion.binary_search(data, 22, 0, len(data))
    # print(res)

    # n = int(input("費氏數列 n => "))
    # start_t = time_ns()
    # start_t_CPU = process_time_ns()
    
    # result = recursion.fibonacci_sequence(n, "loop")
    
    # end_t = time_ns()
    # end_t_CPU = process_time_ns()

    # print("費氏數列 項次:", n)
    # print(n, "項次的 費氏數列:", result)
    
    # # 執行時間長度計算: 精度至奈秒
    # ns = end_t_CPU - start_t_CPU
    # ms, ns = divmod(ns, 1000000)
    # s, ms = divmod(ms, 1000)
    # min, s = divmod(s, 60)
    # print(f"共耗時 (CPU): {min} 分. {s} 秒. {ms} 毫秒. {ns} 奈秒")

    # result = stack_1.arithmetic("465 - 123 * ( 1 + 2 )")
    # print(result)

    # famula = ""

    # stack_ls = Stack_ByList()

    # arr = np.random.randint(0, 50, 10)
    # print(arr)
    # for data in arr:
    #     stack_ls.push(data)

    # print("list:")
    # stack_ls.show_list()

    # for _ in range(arr.shape[0]):
    #     print(stack_ls.pop())

    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------

    ''' queue '''
    # queue = Queue(5, int)

    # for i in range(5):
    #     queue.add(i+1)
    #     print(i + 1)
    #     i += 1

    # print("----------")
    # for i in range(5 - 1):
    #     print(queue.delete())

    # queue.add(8)
    # print(queue.delete())
    # print(queue.delete())


    # queue_cycle = Circular_Queue(5)

    # for i in range(5):
    #     queue_cycle.add(i+1)

    #     # print(queue_cycle.queue)
    
    # # queue_cycle.add(8)

    # for _ in range(5):
    #     print(queue_cycle.delete())
    #     # print(queue_cycle.queue)

    
    # 練習題: 顧客排隊，隊伍長最多 20 人
    # line_up = LineUp(20)

    # customer_list = [
    #     'Jack', 'Amy', 'lis', 'Os', 'Amelia', 'Radoof', 'Wfo', 'Okwf', 'Pjifew', 'Few',
    #     'Jposvk', 'Kjsc', 'Okop', 'Tckj', 'Mk', 'Pmk', 'Doksd', 'KKl', 'Qkjo', 'Avsvd',
    #     'Vhuo', 'Juwfods', 'Jesus', 'Skvsk', 'Xjifd'
    # ]
    
    # i = 0
    # while i < len(customer_list):
    #     if i < 10:
    #         line_up.join_line(customer_list[i])

    #     i += 1

    ''' Tree '''
    b_search_tree = BinarySearchTree()

    node_data = [10, 8, 13, 7, 9, 6, 12, 15]
    node_data = sorted(node_data)
    node_data.reverse()
    print(node_data)

    for data in node_data:
        b_search_tree.addNode(data)

    print("pre-order (前序):")
    b_search_tree.preOrder()

    print("in-order (中序):")
    b_search_tree.inOrder()

    print("post-order (後序):")
    b_search_tree.postOrder()

    node = b_search_tree.searchNode(13)
    print("------------")
    print(node.data)


    ''' Sort '''
    sorting = Sorting()

    # # test case
    # data = Row_Column(row=10, dtype=int).custom_array([
    #     12, 456, 12, 79, 4, 87, 15, 4845, 123, 45
    # ])
    # data = [12, 456, 12, 79, 4, 87, 15, 4845, 123, 45]
    # print("origin:\n", data)

    # bubble sort
    # sorting.bubble_sort(data)
    
    # selection sort
    # sorting.selection_sort(data)

    # insertion sort
    # sorting.insert_sort(data)

    # quick sort
    # sorting.quick_sort(data, 0, data.shape[0]-1)

    # data = Row_Column(row=10, dtype=int).rand(6, True)

    # data = sorting.merge_sort(data)

    # print("sorted result:\n", data)
    

    ''' Search '''
    search = Search()

    # data = Row_Column(row=10, dtype=int)
    # data = data.custom_array([8, 2, 7, 4, 9, 5, 10, 6, 3, 1])

    # result = search.sequential_search(data, 12)
    # result = search.jumps_search(data, 45)

    # result = search.binary_search(data, 15)
    # print("search index:", result)

    hashing = HashTable(10)

    # hashing.put("1231czxfd", 1231)
    # hashing.put("1231czxfd", 1231)
    # hashing.put("rfewrewr", 4567)
    # hashing.put("csc1as1as1c", 456789)
    # hashing.put("c1asd1as1d", 456789)
    # hashing.put("f65dsf4e68a5", 7890)
    # hashing.put("5rf498ed", 12345)
    # hashing.put("4f6rs5df4s", 456789)
    # hashing.put("32f1as1d", 5614651)

    # print(hashing.stored_size)

    # hashing.view()

    # result = hashing.get("rfewrewr")
    # print(result)

    
    hash_map = HashMap()

    # store_keys = []

    # keys = []
    # c_int = 65

    # for _ in range(26 * 2):
    #     if c_int == 90:
    #         c_int = 97
    #         # continue
    #     elif c_int == 123:
    #         break
    #     keys.append(chr(c_int))
    #     c_int += 1

    # for _ in range(5):
    #     temp = ""
    #     key = random.sample(keys, 5)

    #     for i in range(5):
    #         temp += key[i]
        
    #     store_keys.append(temp)
    #     hash_map.put(temp, random.randint(1, 10))

    # hash_map.put(store_keys[2], 88)
    # hash_map.print_map()

    # print(hash_map.get(store_keys[2]))

    # hash_map.remove(store_keys[2])
    # hash_map.print_map()


    pass

