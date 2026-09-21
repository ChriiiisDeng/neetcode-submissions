# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            dfs(node.left)
            dfs(node.right)
            res.append(str(node.val))

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")
        i = len(vals) - 1

        def dfs():
            nonlocal i
            val = vals[i]
            i -= 1

            if val == "N":
                return None
            node = TreeNode(int(val))
            node.right = dfs()
            node.left = dfs()
            return node
        return dfs()
