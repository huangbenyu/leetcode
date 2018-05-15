# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k<2:
            return head
        i = 0
     
        front = head
        t_list=[]
        while front :
            t_list.append(front)
            i+=1
            front = front.next
            if  i==k:
                self.reverseK(t_list)
                i=0
                t_list=[]
               
        return head

    def reverseK(self, t_list):
        length = len(t_list)
        for i in range(length//2):
            t_list[i].val, t_list[length-1-i].val = t_list[length-1-i].val, t_list[i].val