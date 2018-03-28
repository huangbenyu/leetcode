# Definition for singly-linked list.
 class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        LL1=[]
        LL2=[]
        while l1 :
            LL1.append(l1.val)
            l1 =l1.next
        while l2 :
            LL2.append(l2.val)
            l2 =l2.next
        
        sum =0
        result = ListNode(0)
        while len(LL1)>0 or len(LL2)>0:
            a1=a2=0
            if len(LL1)>0:
                a1= LL1.pop()
            if len(LL2)>0:
                a2 =LL2.pop()
            sum = sum+a1+a2
            node =ListNode(sum %10)
            node.next = result.next
            result.next = node
            sum=sum //10
        if sum>0:
            node =ListNode(sum)
            node.next = result.next
            result.next = node    
            
        return  result.next