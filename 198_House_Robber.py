class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            robs = [i for i in range(n)]
            robs[0] = nums[0]
            robs[1] = max(nums[0], nums[1])
            for i in range(2, n):
                robs[i] = max(robs[i - 2] + nums[i], robs[i - 1])
            return robs[n - 1]
