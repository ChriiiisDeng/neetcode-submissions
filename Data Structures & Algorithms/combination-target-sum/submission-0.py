class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(nums, idx, path, sum):
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return
            for i in range(idx, len(nums)):
                if sum + nums[i] > target:
                    continue
                sum += nums[i]
                path.append(nums[i])
                dfs(nums, i, path, sum)
                sum -= nums[i]
                path.pop()

        dfs(nums, 0, [], 0)

        return res
        