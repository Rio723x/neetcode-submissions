# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])

        ##print(queue[0])
        if not root:
            return res
        while queue:
            temp_res = []
            size = len(queue)
            for i in range (size):
                node = queue.popleft()
                temp_res.append(node.val)
            ##print node     
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(temp_res)
        return res