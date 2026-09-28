class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        
        # dp[0] stand for not start to rob
        
        for i in range(len(nums)):
            dp[i + 1] = max(dp[i], nums[i] + dp[i - 1])


        return dp[-1]

        