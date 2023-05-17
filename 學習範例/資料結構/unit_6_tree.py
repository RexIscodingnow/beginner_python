'''
Python Data Structure: Tree (樹狀結構，待補...)

Sample Binary Tree: 底下為示例，
                    在二元數的數值，樹根為分界
                    左子樹 < 右子樹

            11  ----------- 1
           /  \
         12    13  -------- 2
        /  \     \
       14  15    16  ------ 3
      /         /  \
     17        18   19  --- 4
     
    1. root (樹根節點): 11
    2. level (階層數): 1 ~ 4
    3. depth (深度): 4 -----------> Max Level
    4. node (節點): 11, 12, 13, ...... , 18, 19
    5. terminal node (終端節點): 15, 17, 18, 19
    6. Non-terminal node (非終端節點): 11, 12, 13, 14, 16
    7. ancestor (祖先節點):
            子孫        祖先 (12, 14: root of left subtree; 13, 16: root of right subtree)
           (12 ~ 19) --> 11,
        (14, 15, 17) --> 12,
        (16, 18, 19) --> 13,
                (17) --> 14,
            (18, 19) --> 16
    8. descendant (子孫節點): 
            子孫        祖先
           (12 ~ 19) <-- 11,
        (14, 15, 17) <-- 12,
        (16, 18, 19) <-- 13,
                (17) <-- 14,
            (18, 19) <-- 16
    
    9. siblings (兄弟節點):
            (12, 13),
        (14, 15, 16),
        (17, 18, 19)

代號:
    D: root (root node)
    L: left (left subtree/child tree)
    R: right (right subtree/child tree)

走訪: L 與 R 的順位沒動過，變動只有 D 順位

    1. Pre-Order (前序) => D -> L -> R  (DLR)
        --> 11, 12, 14, 17, 15, 13, 16, 18, 19

    2. In-Order (中序) => L -> D -> R  (LDR)
        --> 17, 14, 12, 15, 11, 13, 18, 16, 19

    3. Post-order (後序) => L -> R -> D  (LRD)
        --> 17, 14, 15, 12, 18, 19, 16, 13, 11


'''

import numpy as np



class DoubleLinkedList:
    '''
    雙向鏈結串列
    '''
    def __init__(self, data, left=None, right=None):
        '''
        : param data: 資料欄位
        : param left: 左邊鏈結欄位
        : param right: 右邊鏈結欄位
        '''
        self.data = data
        self.left = left
        self.right = right



class BinaryTree:
    '''
    二元樹
    '''
    def __init__(self, dataStructure="DoubleLinkedList", length=0):
        if dataStructure == "DoubleLinkedList":
            self.root = DoubleLinkedList()
        
        elif dataStructure == "array" and length > 0:
            self.length = length
            self.root = np.empty([self.length])


    def addNode(self, data):
        '''
        加入新節點
            規則: 新加入的數值，比當前的 "祖先節點(ancestor) / 每一個樹根(root)" 大，
                    加到右子樹; 反之，加到左子樹
                                                -- by 二元搜尋樹 (Binary Search Tree)

        : param data: 節點資料
        '''
        if type(self.root) == DoubleLinkedList:
            self._lsNode_add(data)

        elif type(self.root) == np.ndarray:
            self._arrNode_add(data)


    def _lsNode_add(self, data):
        '''
        stored from double linked list
        '''
        newNode = DoubleLinkedList(data)

        if self.root == None:
            self.root = newNode

        else:
            current = self.root


    # ===============================================================================
    # ===============================================================================
    # ===============================================================================

    def _arrNode_add(self, data):
        '''
        stored from array
        '''
        pass


