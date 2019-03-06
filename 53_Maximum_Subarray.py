class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]
        maxnum = nums[0]

        for i in range(1, n):
            if dp[i - 1] > 0:
                dp.append(nums[i] + dp[i - 1])
            else:
                dp.append(nums[i] + 0)
            maxnum = max(maxnum, dp[i])
        return maxnum
