"""
title: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


List1: 2 --> 4 --> 3
List2: 5 --> 6 --> 4
-----------------------
Output: 7 --> 0 --> 8

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]
Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0   # 進位
        result = ListNode()
        head = result   # 指向 result 頭節點
        num1 = 0
        num2 = 0

        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0

            sum = num1 + num2 + carry
            digit = sum % 10    # 每一位數
            carry = sum // 10   # 進位值

            head.next = ListNode(digit)
            head = head.next

            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None

        return result.next


def linkedList(ls_num: list):
    '''
    To create a Singly-linked list
    '''
    if len(ls_num) > 0:
        head = ListNode(ls_num[0])
        current = head
        
        for i in range(1, len(ls_num)):
            new_node = ListNode(ls_num[i])
            current.next = new_node
            current = current.next

        return head

def printNode(head: ListNode):
    '''
    print Singly-linked list
    '''
    if head == None:
        return

    current = head

    while current:
        print(current.val, end=' ')
        if current.next:
            print("->", end=' ')


        current = current.next
    
    print()


solution = Solution()

# result = solution.addTwoNumbers(
#     linkedList([1, 8]),
#     linkedList([0])
# )
# printNode(result)

l1 = [2, 4, 3]
l2 = [5, 6, 4]
l1 = linkedList(l1)
l2 = linkedList(l2)
result = solution.addTwoNumbers(l1, l2)
printNode(result)

l1 = [0]
l2 = [0]
l1 = linkedList(l1)
l2 = linkedList(l2)
result = solution.addTwoNumbers(l1, l2)
printNode(result)

l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
l1 = linkedList(l1)
l2 = linkedList(l2)
result = solution.addTwoNumbers(l1, l2)
printNode(result)