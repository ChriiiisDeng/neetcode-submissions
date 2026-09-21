# Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.dfs(root, 0)

    def dfs(self, root, depth : int):
        if root is None:
            return 0

        depth += 1

        max_dep = max(self.dfs(root.left, 0), self.dfs(root.right, 0))

        return depth + max_dep
        