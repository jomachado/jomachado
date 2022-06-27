# Definition for a binary tree node.


from pickle import NONE
from turtle import right
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:            
        
                
        traversalValues = []

        def inorderTraversalCustom( root: Optional[TreeNode]):             
            if(root.left != None):
                inorderTraversalCustom(root.left)
            
            traversalValues.append(root.val)

            if(root.right != None):
                inorderTraversalCustom(root.right)

        inorderTraversalCustom(root)
        return traversalValues


firstTreeNode = TreeNode(3,None, None)
secondTreeNode = TreeNode(2,firstTreeNode, None)
treeRoot = TreeNode(1, None, secondTreeNode)

obj = Solution()
print(obj.inorderTraversal(treeRoot))