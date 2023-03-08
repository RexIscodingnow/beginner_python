'''
Python 資料結構: 執行區

        Chapter                File Name
   __________________________________________
    1. Array (陣列)       => unit_1_array.py
    2. List (串列)        => unit_2_list.py
    3. Stack (堆疊)       => unit_3_stack.py
    4. Queue (佇列)       => unit_4_queue.py
    5. Tree (樹狀結構)
    6. Graph (圖形結構)
    7. Sorting (排序)
    8. Search (搜尋)
'''

import numpy as np

from unit_1_array import ArrayOperation, Row_Column
from unit_2_list import Sequential_List, Linked_List
from unit_3_stack import Stack, Stack_Example, Recursion_Example
from unit_4_queue import Queue


class Sorting():
    def swap(self, data_1, data_2):
        temp = data_1
        data_1 = data_2
        data_2 = temp

        return data_1, data_2

    def selection_sort(self, data):
        '''
        1D array 選擇排序法

        O(n ^ 2)
        '''
        for i in range(data.shape[0]):
            for j in range(i, data.shape[0]):
                if data[i] > data[j]:
                    data[i], data[j] = self.swap(data[i], data[j])

        print("selection sort")
        print(data)

    def quick_sort(self, data, left, right):
        '''
        1D array 快速排序法
        '''
        i = left
        j = right
        pivot = data[left]  # 基準點

        while i != j:
            while data[j] >= pivot and i < j:
                j -= 1
            while data[i] <= pivot and i < j:
                i += 1
            
            if i < j:
                data[i], data[j] = self.swap(data[i], data[j])

        data[left] = data[i]
        data[i] = pivot

        self.quick_sort(data, left, i-1)
        self.quick_sort(data, i+1, right)



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

    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------

    ''' List '''
    # seq_ls = Sequential_List()
    # seq_ls.list_array()

    # Linked List
    
    # ls_node = Linked_List()
    # for i in range(6):
    #     ls_node.insert(i+1)

    # ls_node.printNode()

    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------

    ''' Stack '''
    stack_1 = Stack_Example()
    stack_1.common_operation()

    # recursion = Recursion_Example()
    # n = int(input("factorial number => "))
    # result = recursion.factorial(n)
    # print(n, "!")
    # print(result)

    # result = recursion.fibonacci_sequence(n)
    # print("費氏數列 項次:", n)
    # print(n, "項次的 費氏數列:", result)
    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------

    ''' queue '''
    # queue = Queue(5, int)

    # for i in range(queue.length):
    #     queue.add(i+1)
    #     print(i + 1)
    #     i += 1

    # print("----------")
    # for i in range(queue.length - 1):
    #     print(queue.delete())

    # queue.add(8)
    # print(queue.delete())
    # print(queue.delete())

    pass

