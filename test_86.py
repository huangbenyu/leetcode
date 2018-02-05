# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    #86
    def partition(self, head, x):
        
        startnode = lessnode = None
        startgreaternode = greaternode = None

        while head :
            if head.val >= x :
                if greaternode:
                    greaternode.next = head
                    greaternode = greaternode.next
                   
                else:
                    greaternode = head
                    startgreaternode = greaternode
            else:
                if lessnode :
                    lessnode.next =head 
                    lessnode = lessnode.next
                else:
                    lessnode = head
                    startnode = lessnode

            head = head.next

        if startnode :
            lessnode.next = startgreaternode
            if greaternode :
                greaternode.next =None
            return startnode
        else:
            return startgreaternode  



    def partition1(self, head, x):

        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lastnode = None
        if head is None:
            return

        if head.val < x:
            lastnode = head

        nextnode = head
        while nextnode.next :
            curnode = nextnode.next
            if curnode.val < x:

                if lastnode is None:
                    lastnode = curnode

                    #move to head
                    nextnode.next = nextnode.next.next
                    lastnode.next = head
                    head  = lastnode
                else: 
                    nextnode.next = curnode.next
                    curnode.next = lastnode.next
                    lastnode.next = curnode
                    lastnode = curnode
            else :
                nextnode = nextnode.next     

