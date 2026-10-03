class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        
        res = -10001

        for i in range(1, len(nums) + 1):
            
            if dp[i - 1] > 0 and (dp[i - 1] + nums[i - 1]) > 0:
                dp[i] = dp[i - 1] + nums[i - 1]
            else:
                dp[i] = nums[i - 1]
            res = max(dp[i], res)
        
        return res
