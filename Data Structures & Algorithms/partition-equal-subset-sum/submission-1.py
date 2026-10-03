class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(idx, target) -> bool:
            if target == 0:
                return True

            if idx >= n or target < 0:
                return False

            if memo[idx][target] != -1:
                return memo[idx][target]

            memo[idx][target] = (dfs(idx + 1, target) or dfs(idx + 1, target - nums[idx]))

            return memo[idx][target] 

        return dfs(0, target)
        
        