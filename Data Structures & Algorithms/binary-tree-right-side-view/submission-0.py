# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            num = None
            for _ in range(size):
                node = queue.popleft()
                if node:
                    num = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if num:
                res.append(num)

        return res
        
        