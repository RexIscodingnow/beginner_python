"""
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


"""

import numpy as np


class DoubleListNode:
    """
    雙向鏈結串列: 節點
    """
    def __init__(self, data: int | float | str = 0, left=None, right=None):
        """
        : param data: 資料欄位
        : param left: 左邊鏈結欄位
        : param right: 右邊鏈結欄位
        """
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    二元搜尋樹

    Implemented in Double Linked List.
    """
    def __init__(self, dataStructure="DoubleLinkedList"):
        """
        : param dataStructure: 資料結構表示  1. DoubleLinkedList  2. Array
        """
        structure = ["DoubleLinkedList", "Array"]

        if dataStructure.lower() == structure[0].lower():
            self.root = DoubleListNode()
        
        elif dataStructure.lower() == structure[1].lower():
            self.index = 1
            self.size = 10
            self.root = [None] * self.size

    def preOrder(self):
        """
        走訪節點: 前序
                        -- 走訪方向 (visit node -> 左 subtree -> 右 subtree)
        """
        if type(self.root) == DoubleListNode:
            self._preOrder(self.root)

        elif type(self.root) == list:
            self._preOrder(self.index)

    def inOrder(self):
        """
        走訪節點: 中序
                        -- 走訪方向 (左 subtree -> visit node -> 右 subtree)
        """
        if type(self.root) == DoubleListNode:
            self._inOrder(self.root)

        elif type(self.root) == list:
            self._inOrder(self.index)
    
    def postOrder(self):
        """
        走訪節點: 中序
                        -- 走訪方向 (左 subtree -> visit node -> 右 subtree)
        """
        if type(self.root) == DoubleListNode:
            self._postOrder(self.root)

        elif type(self.root) == list:
            self._postOrder(self.index)


    def _preOrder(self, node: DoubleListNode | int):
        """
        : param node: 節點
        """
        if type(node) == DoubleListNode:
            if node != None:
                print(node.data)
                self._preOrder(node.left)
                self._preOrder(node.right)

        elif type(node) == list:
            print(self.root[self.index])
            self._preOrder(self.index * 2)
            self._preOrder(self.index * 2 + 1)

    def _inOrder(self, node: DoubleListNode | int):
        """
        : param node: 節點
        """
        if type(node) == DoubleListNode:
            if node != None:
                self._inOrder(node.left)
                print(node.data)
                self._inOrder(node.right)

        elif type(node) == list:
            self._inOrder(self.index * 2)
            print(self.root[self.index])
            self._inOrder(self.index * 2 + 1)

    def _postOrder(self, node: DoubleListNode | int):
        """
        : param node: 節點
        """
        if type(node) == DoubleListNode:
            if node != None:
                self._postOrder(node.left)
                self._postOrder(node.right)
                print(node.data)

        elif type(node) == list:
            self._postOrder(self.index * 2)
            self._postOrder(self.index * 2 + 1)
            print(self.root[self.index])


    def addNode(self, data):
        """
        加入新節點
            規則: 新加入的數值，比當前的 "祖先節點(ancestor) / 每一個樹根(root)" 大，
                    加到右子樹; 反之，加到左子樹
                                                -- by 二元搜尋樹 (Binary Search Tree)

        : param data: 節點資料
        """
        if type(self.root) == DoubleListNode:
            self._ls_addNode(data)

        elif type(self.root) == list:
            self._arr_addNode(data)

    def searchNode(self, data):
        """
        搜尋節點
        """
        if type(self.root) == DoubleListNode:
            return self._ls_searchNode(data)

        elif type(self.root) == list:
            self._arr_addNode(data)


    def deleteNode(self, data):
        """
        刪除節點
        """
        if type(self.root) == DoubleListNode:
            self._ls_delNode(data)

        elif type(self.root) == list:
            pass


    def _ls_addNode(self, data):
        """
        Stored in Binary Search Tree. (Linked List)
        
        : param data: 節點資料
        """
        newNode = DoubleListNode(data)

        if self.root == None:
            self.root = newNode

        else:
            current = self.root

            while True:
                # 新節點數值 < 當前比對中的節點
                # 往左邊的 subtree
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                        break

                # 新節點數值 > 當前比對中的節點
                # 往右邊的 subtree
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        break

    def _ls_searchNode(self, data):
        """
        Search existed node (Linked List)
        """
        if self.root == None:
            return

        current = self.root

        while True:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right

            if current == None:
                return None

    def _ls_delNode(self, data):
        """
        Delete existed node (Linked List)
        """
        if self.root == None:
            return
        
        current = self._ls_searchNode(data)

        if current:
            # terminal node 位置
            if current.left == None and current.right == None:
                del current

            # 只有一個子節點 (左邊 or 右邊)
            elif current.left:
                current = current.left
            elif current.right:
                current = current.right

            # 兩邊都有子節點
            else:
                # 後繼節點
                successor = self._ls_find_successor(current.right)

                # pass
                # 前驅節點

        else:
            return
        
    def _ls_find_successor(self, node: DoubleListNode):
        """
        找後繼節點
        """
        if node.left == None:
            return node
        
        return self._ls_find_successor(node.left)

    # ===============================================================================
    # ===============================================================================
    # ===============================================================================

    def _arr_addNode(self, data):
        """
        Add new node in array
        """
        pass


