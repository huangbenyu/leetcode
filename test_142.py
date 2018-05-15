# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tortoise = head
        hare = head
        flag = False
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                flag = True
                break
            
        if flag:
            ptr1 = head
            ptr2 = tortoise
            while ptr1!=ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1
        else:
            return None
