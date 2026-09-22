class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def dfs(idx, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(i + 1, path)
                path.pop()
                visited[i] = False

        dfs(0, [])
        return res
        