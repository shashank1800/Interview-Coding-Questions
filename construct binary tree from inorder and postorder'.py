"""

106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


"""

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        m = inorder.index(postorder[-1])
        postorder.pop()
        root.right = self.buildTree(inorder[m+1: ], postorder)
        root.left = self.buildTree(inorder[0: m], postorder)
        return root
