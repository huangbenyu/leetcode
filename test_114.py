# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

import sys
class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.current = root
        left  = root.left
        right = root.right

        self._flat(left)
        self._flat(right)
        self.current = None

    
    def _flat(self, root):
        if root is None:
            return 

        left  = root.left
        right = root.right

        self.current.left = None
        self.current.right = root
        self.current = self.current.right 

        self._flat(left)
        self._flat(right)


def stringToTreeNode(input):
    #input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def main():
    

    #lines = readlines()
    #while True:
    #try:
    line = "[1,2]"
    root = stringToTreeNode(line)
    
    ret = Solution().flatten(root)

    out = treeNodeToString(root)
    if ret is not None:
        print ("Do not return anything, modify root in-place instead.")
    else:
        print(out)
   

if __name__ == '__main__':
    main()