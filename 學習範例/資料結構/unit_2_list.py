'''
Python Data Structure: List (串列，待補)

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
 宣告方式 | dtype name[length]; |  node = ListNode(data, nextNode)
--------------------------------------------------------

    |------|-----|      |------|-----|
    | data | ptr |      | data | ptr |
    |------|-----|      |------|-----|
              |            ^      |
              |------------|      |------------> 以此類推，連接節點 (資料 data)


註記: 在兩者處理同一件事，效率差不多的時候，
        一般情況還是使用陣列比較好

    ** 若使用鏈結串列的話，會多花 2 倍(以上)的記憶體空間，才達到陣列的效率 **
                ** 是不值得的方法 **

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
    鏈結串列: 節點
    '''
    def __init__(self, data=0, link=None):
        '''
        : param data: 資料欄位
        : param link: 鏈結欄位 (連向另一個節點位置)
        '''
        self.data = data
        self.link = link


class Linked_List():
    '''
    鏈結串列: 單向鏈結串列 (Singly Linked List)

    由一組 節點 (Node) 所組成的 "有序串列"，各 Node 除了 資料欄 之外，
    另外有 大於等於 1 個的指標欄，儲存指向下一個節點的資料
    '''
    def __init__(self):
        self.listNode = ListNode()  # (原)頭節點

    def isEmpty(self):
        '''
        檢查節點是否空
        '''
        # 狀態: 空空的，也就是啥都沒有
        # (連個節點的影子都沒見到的狀態，連個屁都沒有)
        return self.listNode == None
    
    def addFront(self, data):
        '''
        添加前頭 (頭節點)

        : param data: 添加的節點資料

        1. 新節點的存放下一節點(欄位)，連接頭節點位址

        |----| *link* |----| link    (其他節點)
        | 新 |------> | 原 |------> ............
        |----|        |----|

        2. (原)頭節點的資料 指(洗)派(掉) 成新節點位置

        |----|  link *|----|*
        | 原 |------> | 新 |------> ...........
        |----|        |----|
        '''
        current = self.listNode   # 當前的頭節點
        new_node = ListNode(data, current)   # 建立新節點，並與當前的頭節點連接
        
        # 調換身分 ( new_node(頭) --> self.listNode )
        # 調換後   ( self.lisNode(頭) --> new_node )
        self.listNode = new_node

    def addBack(self, data):
        '''
        添加在尾段 (最後一個節點的後方 (接在屁股後面))
        '''
        new_node = ListNode(data)   # 建立新節點

        if self.listNode == None:   # 若頭節點為空，則直接上新節點
            self.listNode = new_node
        else:
            current = self.listNode   # 當前頭節點
            
            # 若有連接下一個節點，則一路順下去
            # 直到沒有任何節點，連在這個隊伍屁股
            while current.link:
                # 下一個節點 = 下一個節點的位置 (前一個節點儲存的)
                current = current.link

            current.link = new_node

    def insert(self, data, node):
        '''
        插入節點

        : param data: 要插入的節點資料
        : param node: 插入節點的位置 (節點資料)
                        -- 在插入節點的位置，往前一個，是實際插入位置

        : type data: ListNode.data
        : type node: ListNode.data
                        -- 寫入節點資料的型別
        '''
        if self.listNode == None:
            return

        current = self.listNode

        # 在頭節點位置
        if node == current.data:
            self.addFront(data)
            return

        # 非頭節點位置
        while current.link:
            nextNode = current.link

            if node == nextNode.data:
                newNode = ListNode(data, nextNode)
                current.link = newNode
                return

            current = current.link

    def delete(self, data):
        '''
        刪除節點

        : param data: 刪除的目標節點的資料
        '''
        if self.listNode == None:
            return

        current = self.listNode

        # 刪除位置: 在頭節點
        if data == current.data:
            self.listNode = current.link
            del current
            return
        
        # 刪除位置: 從頭節點 (不包含) ~ 最後一個節點
        while current.link:
            nextNode = current.link   # 當前節點的下一個節點

            if data == nextNode.data:
                # 繞過要刪除的節點
                # 跟要刪除的目標節點，下一個節點的位置連接
                current.link = nextNode.link
                del nextNode
                return

            current = current.link

    def search(self, data):
        '''
        搜尋節點

        : param data: 要搜尋的節點資料
        : rtype: ListNode() | None
        '''
        if self.listNode == None:
            return

        current = self.listNode
        
        while current:
            if data == current.data:
                return current
            
            current = current.link
        
        return None
    
    def get_rootNode(self):
        '''
        取得頭節點
        '''
        if self.isEmpty():
            return
        
        # 在建構子，已經建立一個節點
        # 使用到本類的建構子，一起建立之節點
        # 節點資料: 0
        return self.listNode.link

    def get_lastNode(self):
        '''
        取得最尾部的節點
        ''' 
        if self.isEmpty():
            return
        
        current = self.listNode
        while current.link:
            current = current.link

        return current

    def printNode(self):
        '''
        印出所有節點
        '''
        if self.listNode == None:
            return

        current = self.listNode.link   # 

        while current:
            print(current.data, end=' ')
            if current.link:
                print("->", end=' ')

            current = current.link
        
        print()

    def listNode_Example(self):
        values = inputValues(5, int, "學生_1 分數 => ", "學生_2 分數 => ", "學生_3 分數 => ", "學生_4 分數 => ", "學生_5 分數 => ")
        
        student_5 = ListNode(values[4], None)
        student_4 = ListNode(values[3], student_5)
        student_3 = ListNode(values[2], student_4)
        student_2 = ListNode(values[1], student_3)
        student_1 = ListNode(values[0], student_2)

        # self.listNode = student_1
        # self.printNode()

        print("[%d] -> [%d] -> [%d] -> [%d] -> [%d] -> None" %
                (student_1.data, student_2.data, student_3.data, student_4.data, student_5.data))


