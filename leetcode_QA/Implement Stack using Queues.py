"""
title: Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
* void push(int x) Pushes element x to the top of the stack.
* int pop() Removes the element on the top of the stack and returns it.
* int top() Returns the element on the top of the stack.
* boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
* You must use only standard operations of a queue, which means that only push to back,
    peek/pop from front, size and is empty operations are valid.
* Depending on your language, the queue may not be supported natively.
  You may simulate a queue using a list or deque (double-ended queue) 
    as long as you use only a queue's standard operations.

Example:
    Input
    ["MyStack", "push", "push", "top", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 2, 2, false]

    Explanation
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // return 2
    myStack.pop(); // return 2
    myStack.empty(); // return False
"""

class MyStack(object):
    
    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return

        for i in range(len(self.queue) - 1):
            # Queue cycle one times until rear to front side
            # 佇列 資料繞一圈 (循環)，直到 "開頭資料 到達 出口"
            self.queue.append(self.queue.pop())

        return self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.empty() != True:
            return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue:
            return False
        else:
            return True


solution = MyStack()

nums = [1, 5, 4, 8, 6]
for i in nums:
    solution.push(i)
    print(i)

for i in range(len(nums)):
    print(solution.pop())