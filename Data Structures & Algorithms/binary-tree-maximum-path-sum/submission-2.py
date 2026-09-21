# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001
        def dfs(node, parent_sum) -> int:
            nonlocal res
            if not node:
                return 0
            
            left = max(dfs(node.left, parent_sum + node.val), 0)
            right = max( dfs(node.right, parent_sum + node.val), 0)

            _max = max(left + right + node.val, max(left, right) + node.val + parent_sum)
            res = max(res, _max)
            return node.val + max(left, right)

        dfs(root, 0)
        return res
        