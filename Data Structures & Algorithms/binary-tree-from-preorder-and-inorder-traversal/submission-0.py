# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])

        idx = inorder.index(root.val)

        left_inorder = inorder[:idx]     
        right_inorder = inorder[idx+1:]
        
        left_size = len(left_inorder)
        
        left_preorder = preorder[1:1+left_size]
        right_preorder = preorder[1+left_size:]
        
        root.left = self.buildTree(left_preorder , left_inorder)
        root.right = self.buildTree(right_preorder , right_inorder)
        
        return root

