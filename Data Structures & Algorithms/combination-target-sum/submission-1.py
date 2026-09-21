class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, path, current_sum):
            if current_sum == target:
                res.append(path[:])
                return
            for i in range(idx, len(nums)):
                if current_sum + nums[i] > target:
                    break
                path.append(nums[i])
                dfs(i, path, current_sum + nums[i])
                path.pop()

        dfs(0, [], 0)

        return res
        