class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    

    def helper(self, nums: List[int]) -> int:
        prev_one,prev_two = 0,0
        
        # dp[0] stand for not start to rob
        
        for i in range(len(nums)):
            tmp = max(prev_one, nums[i] + prev_two)
            prev_two = prev_one
            prev_one = tmp
        

        return prev_one