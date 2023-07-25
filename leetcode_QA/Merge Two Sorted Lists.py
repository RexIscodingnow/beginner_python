"""
title: Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
Example 2:
    Input: list1 = [], list2 = []
    Output: []
Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merge_ls = ListNode()
        current = merge_ls

        while list1 and list2:
            """
            較小的數值，整個節點接到 merge_ls
            """
            if list1.val <= list2.val:
                current.next = list1                
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return merge_ls.next


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

list1 = [1, 2, 4]
list2 = [1, 3, 4]
list1 = linkedList(list1)
list2 = linkedList(list2)

result = solution.mergeTwoLists(list1, list2)
printNode(result)