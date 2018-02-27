# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = []
        layer =[]
        result=[]
        q.append(root)
        sub_q =[]
        while len(q)>0:
            node = q[0]
            layer.append(node.val)
            if node.left:
                sub_q.append(node.left)
            if node.right:
                sub_q.append(node.right)
            del q[0]
            if len(q)<1:
                result.append(layer)
                layer=[]
                q=sub_q
                sub_q=[]
        return  result