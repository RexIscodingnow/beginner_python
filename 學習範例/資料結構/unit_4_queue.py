'''
Python Data Structure: Queue (佇列)

    notes:
        1. Queue is use First In First Out. It is oppsite operation of Stack.
        2. The entrance and exit are difference side.
        3. Entrance is called rear. And exit is called front.

    圖示:
    
    rear                             front
        -----------------------------
  In -->                             --> Out
        -----------------------------

'''

from unit_1_array import Row_Column

class Queue():
    def __init__(self, MaxLength=0, dtype=float):
        self.length = MaxLength
        if MaxLength > 0:
            self.queue = Row_Column(row=self.length, dtype=dtype).array
            self.rear = -1
            self.front = -1

            # list 操作
            self.queueList = []
        
        else:
            raise Exception("Length must be over 0")

    def add(self, data):
        # use list
        if self.isFull():
            self.queueList.append(data)

    def delete(self):
        # use list
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:
            return self.queueList.pop(0)

    def isFull(self):
        # use list
        if len(self.queueList) == self.length:
            return True
        else:
            return False

    def isEmpty(self):
        # use list
        if len(self.queueList) == 0:
            return True
        else:
            return False








