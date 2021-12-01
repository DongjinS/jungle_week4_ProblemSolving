class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N+1)
        dp[0] = nums[0]
        if N>1:
            for i in range(1,len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
            return dp[N-1]
        else:
            return nums[0]