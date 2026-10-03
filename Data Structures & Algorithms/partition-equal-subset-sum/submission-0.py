class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        def dfs(idx, current_sum, total_sum):
            if current_sum == total_sum - current_sum:
                return True
            if current_sum > total_sum - current_sum:
                return False

            for i in range(idx, len(nums)):

                current_sum += nums[i]
                if dfs(i + 1, current_sum, total_sum):
                    return True

                current_sum -= nums[i]

            return False

        return dfs(0, 0, total_sum)
        
        