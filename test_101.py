# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        return self.is_sym(root.left, root.right)

    def is_sym(self, lefttree, righttree):
        
        if lefttree is None  and righttree is not None:
            return False

        if lefttree is not None  and righttree is  None:
            return False

        if lefttree is None  and righttree is  None:
            return True

        if  lefttree.val != righttree.val:
            return False
        
        if  not self.is_sym(lefttree.left, righttree.right):
            return False
        
        if  not self.is_sym(righttree.left, lefttree.right):
            return False
        
        return True
        