class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, idx, path):
            res.append(path[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(nums, i + 1, path)
                path.pop()

        dfs(nums, 0, [])
        return res
        