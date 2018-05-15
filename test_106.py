# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        self.buildsubtree(root,inorder,postorder)
        return  root

    def split_inorder(self,inorder,x):
        for i  in range(len(inorder)):
            if inorder[i] == x:
                return inorder[0:i],inorder[i+1:]
        return [],[]

    def split_postorder(self,leftlist, postorder):
        for i in range(len(postorder)):
            if postorder[i] not in leftlist:
                return postorder[0:i],postorder[i:]
        if leftlist:
            return postorder,[]
        else:
            return [],postorder

    def buildsubtree(self, root,inorder, postorder):
        leftinorder, rightinorder = self.split_inorder(inorder,root.val)
        #print(leftinorder)
        #print(rightinorder)
        leftpostorder, rightpostorder = self.split_postorder(leftinorder,postorder[0:-1])
        #print(leftpostorder)
        #print(rightpostorder)
        
        if  leftinorder :
            left = TreeNode(leftpostorder[-1])
            root.left =left
            self.buildsubtree(left,leftinorder,leftpostorder)
            
        if  rightinorder :
            right = TreeNode(rightpostorder[-1])
            root.right =right
            self.buildsubtree(right,rightinorder,rightpostorder)