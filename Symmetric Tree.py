"""
101. Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        else :
            return self.checkInBothSide(root.left, root.right)
    
    def checkInBothSide(self,root1,root2)->bool:
        
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False

        if root1.val!=root2.val:
            return False

        else:
            return self.checkInBothSide(root1.left,root2.right) and self.checkInBothSide(root1.right,root2.left)
            
        
