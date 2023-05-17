'''
Python Data Structure: Queue (佇列)

    notes:
        1. Queue is First In First Out within two ends.
            It is difference operation of Stack.

        2. The entrance and exit are difference side.
        3. Entrance is called rear. And exit is called front.

    圖示:

    rear (Entrance)                  front (exit)
        -----------------------------
  In -->                             --> Out
        -----------------------------

'''

class Queue():
    '''
    Linear Queue (線性佇列)

    一般情況，指標 rear 指到底部，基本上不能再放入資料
    
    不過 Python list 這個資料結構與內建的函式操作之下，
    因此避免掉上述情況
    '''
    def __init__(self, MaxLength=0):
        self.Maxlength = MaxLength
        # list 操作
        self.queueList = []

    def add(self, data):
        # use list
        if not self.isFull():
            self.queueList.append(data)

    def delete(self):
        # use list
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:
            return self.queueList.pop(0)
        
    def top(self):
        return self.queueList[-1]

    def isFull(self):
        # use list
        if len(self.queueList) == self.Maxlength:
            return True
        else:
            return False

    def isEmpty(self):
        # use list
        if len(self.queueList) == 0:
            return True
        else:
            return False


class LineUp:
    '''
    排隊 練習題
    '''
    def __init__(self, maxLine: int):
        self.queue = Queue(maxLine, str)

    def join_line(self, name):
        self.queue.add(name)

    def get_out(self):
        return self.queue.delete()
    
    def first_customer(self):
        return self.queue.top()



class Circular_Queue:
    '''
    Circular Queue (環狀佇列)

    為了解決 Linear Queue 還有空位，但被判斷為滿的問題

    當 rear 已經指到最大索引值，但還有空位可存放時
    就把 rear 繞一圈回來，回到索引值 0 (index = 0) 的位置

    一般情況會犧牲掉一個位置，給 front 使用，因此會有一個空位
    '''
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.rear = -1
        self.front = -1

    def add(self, data):
        if self.isFull():
            return

        self.rear += 1
        self.rear %= self.size
        # self.queue[self.rear % self.size] = data
        self.queue[self.rear] = data

    def delete(self):
        if self.isEmpty():
            return

        self.front += 1
        self.front %= self.size
        # temp = self.queue[self.front % self.size]
        # self.queue[self.front % self.size] = None
        temp = self.queue[self.front]
        self.queue[self.front] = None

        return temp

    def isFull(self):
        return (self.rear + 1) % self.size == self.front % self.size

    def isEmpty(self):
        return self.rear % self.size == self.front % self.size






