'''
Python Data Structure: List

    Compare Array with List:
    
                Array                   List
________________________________________________________
 資料結構 |  連續的資料         |    非連續的資料
--------------------------------------------------------
     長度 | 要事先宣告好長度    |      不定長度
--------------------------------------------------------
 找尋資料 |     索引值          |   查詢特定節點 (node)，
          |                    |   要從"頭節點" 開始走訪
--------------------------------------------------------

    |------|-----|      |------|-----|
    | data | ptr |      | data | ptr |
    |------|-----|      |------|-----|
              |            ^      |
              |------------|      |------------> 以此類推，連接節點 (資料 data)

'''

import numpy as np

from unit_1_array import ArrayOperation


def inputValues(quantity, dtype=str, *msg: str | list):
    '''
    rtype: list
    '''
    values = []
    for i in range(quantity):
        values.append(dtype(input(msg[i])))

    return values


class Sequential_List():
    '''
    循環串列: 元素 與 元素 之間有線性關係，已循續方式儲存

        ex: array
    '''
    def __init__(self):
        self.array = np.empty([5])

    def list_array(self):
        values = inputValues(5, int, "0 => ", "1 => ", "2 => ", "3 => ", "4 => ")
        for i in range(self.array.shape[0]):
            self.array[i] = values[i]

        print(self.array)


class ListNode:
    '''
    鏈結串列
    '''
    def __init__(self, data=0, link=None):
        self.data = data
        self.link = link


class Linked_List():
    '''
    鏈結串列

    由一組 節點 (Node) 所組成的 "有序串列"，各 Node 除了 資料欄 之外，
    另外有 大於等於 1 個
    '''
    def __init__(self):
        self.listNode = ListNode()

    def listNode_Example(self):
        values = inputValues(5, int, "學生_1 分數 => ", "學生_2 分數 => ", "學生_3 分數 => ", "學生_4 分數 => ", "學生_5 分數 => ")
        
        student_5 = ListNode(values[4], None)
        student_4 = ListNode(values[3], student_5)
        student_3 = ListNode(values[2], student_4)
        student_2 = ListNode(values[1], student_3)
        student_1 = ListNode(values[0], student_2)

        print("[%d] -> [%d] -> [%d] -> [%d] -> [%d] -> None" %
                (student_1.data, student_2.data, student_3.data, student_4.data, student_5.data))


    def isEmpty(self):
        return self.listNode == None
    
    def insert(self, data):
        newNode = ListNode(data)

        if self.isEmpty():
            self.listNode = newNode
        
        else:
            current = ListNode(data)

            while current.link != None:
                current = current.link
            
            current.link = newNode

    def printNode(self):
        current = self.listNode

        while current.link != None:
            print(current.data)
            current = current.link

        print()


