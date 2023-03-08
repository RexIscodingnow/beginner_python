'''
Python Data Structure: Stack (堆疊)

    notes:
        1. Two operations in stack: Push, Pop
        2. 在 Stack 儲存、取得 資料，資料的出入口是 同一個，也就是 "出入口共用"
        3. 具有 First In Last Out (簡寫: FILO) 的特性
                    |
                    |--> 由於資料進出是同一邊，因此第一筆進去，
                         要等到前面的所有資料全部取出，才可出來
                         
                        ** 得: 最先進去，最後出來


        圖示:
                  出入口   位置
                |       |   5
                |       |   4
                |       |   3
                |       |   2
                |       |   1
                |_______|   0
                |.......|  -1  <-- 當前儲存高度 (索引值)

            以 -1 為起始點，
'''

import numpy as np


class Stack:
    def __init__(self, dtype=float, length=100, container=np):
        '''
        param dtype: 型別
        param length: 堆疊最大高度
        param container: 陣列、列表，二選一  np (numpy), list
        '''
        self.length = length
        self.index = -1
        if container == np:
            self.__stack = np.empty([self.length], dtype)   # private member variable
        elif container == list:
            self.__stack = []
        else:
            print("error contaier data type")

    def push(self, data):
        '''
        儲存資料: 推進 Stack
        '''
        if self.isFull():
            print("我已經滿了，不行了~~")
        else:
            if type(self.__stack) == np.ndarray:
                self.index += 1
                self.__stack[self.index] = data
            
            elif type(self.__stack) == list:
                self.__stack.append(data)
    
    def pop(self):
        '''
        刪除 且 返回 最頂端資料
        '''
        if self.isEmpty() == False:
            top_item = self.top()
            if type(self.__stack) == np.ndarray:
                self.__stack[self.index] = None
                self.index -= 1
            elif type(self.__stack) == list:
                self.__stack.pop()
            
        return top_item

    def top(self):
        '''
        返回 最頂端資料
        '''
        if self.isEmpty():
            return
        else:
            return self.__stack[self.index]

    def isEmpty(self):
        '''
        檢查 是否為空
        '''
        if self.index == -1:
            return True
        else:
            return False
        
    def isFull(self):
        '''
        檢查 是否堆疊已滿
        '''
        if self.index == self.length - 1:
            return True
        else:
            return False


class Stack_Example:
    def __init__(self, dtype=float):
        self.stack = Stack(dtype)

    def common_operation(self):
        '''
        Stack 常用操作: 推進、取出 (Push and Pop)
        '''
        print("長度:", self.stack.length)
        for i in range(self.stack.length):
            # print("index:", self.stack.index)
            self.stack.push(i)

        # print("index:", self.stack.index)
        # print(self.stack.push(80))

        for i in range(self.stack.length):
            # print("index:", self.stack.index)
            # print(self.stack.top())
            print(self.stack.pop())

    def vaild_parentheses(self, parentheses: str):
        '''
        合法的括號

        ex: 合法的 => 1. ()   2. {([])}   3. [{}()]
            不合法 => 2. (]   2. ([}}     3. ((((({}}}}}}
        
        param parentheses: 括號 
                    |
                    |-> type: string

        return type: bool
        '''
        if parentheses == None or len(parentheses) % 2 != 0:
            return False
        
        legal = True
        attach = {')': '(', ']': '[', '}': '{'}
        for char in parentheses:
            if char in attach.values():
                self.stack.push(char)

            elif char in attach.keys():
                if self.stack.isEmpty():
                    legal = False
                else:
                    if attach[char] != self.stack.pop():
                        legal = False
        
        # if self.stack.isEmpty() == False:    # 一般寫法
        if not self.stack.isEmpty():           # 很 Pythonic 的寫法
            legal = False

        return legal


class Recursion_Example():
    '''
    遞迴，其工作方式:
        
        |      | <-- 最後一次呼叫 (達到 終止條件)
        |      | <-- ......
        |      | <-- ......
        |      | <-- 第二次呼叫
        |      | <-- 第一次呼叫
        --------

    1. call function =>  first -> second -> ....... -> last call
    2. implement function => last call -> ....... -> second -> first
            |
            |--> 最後一次呼叫，從堆疊取出
                        |--> .......
                                |--> 第一次呼叫，從堆疊取出


    遞迴，用一句話形容: 我呼叫自己，套娃般的行動
    
    註1 : 套娃，想成 "俄羅斯娃娃"，大的娃娃拆開 有小一號的，
                再拆開 又有小一號，又再拆開，以此類推
    '''
    def factorial(self, n: int):
        '''
        階乘
        '''
        if n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def fibonacci_sequence(self, n: int, mode = "recursion"):
        '''
        費氏數列

        公式: F(n) = F(n - 1) + F(n - 2)

        0  1  2  3  4  5  6  ... 
       __________________________
        0  1  1  2  3  5  8  ... 

        缺點: 已經做過的，會再做一遍 甚至 二遍三遍 以上

            假設 n = 5  演示方式: tree
            
              F(n - 1)        F(n - 2)
                  ^               ^
                  |       5       |
                  |  ____/ \____  |
                  | /           \ |
                  |/             \|
                  4               3
                 / \             / \
                3   \           2   1
               / \   \         / \
              2   1   \       1   1
             / \       2
            1   1     / \
                     1   1

        總體有 n = 3 的部分 多做一遍計算
        
        間距
       i =   1  1  1  1  2  3  5   8
            ________________________________________
       j =  0  1  1  2  3  5  8  13  21
        結果
        '''
        if mode == "recursion":
            if n <= 2:    # 到 2 圈 還是 1
                return 1
            
            else:
                return self.fibonacci_sequence(n - 1) + self.fibonacci_sequence(n - 2)

        elif mode == "plus":
            # use while loop
            pass

