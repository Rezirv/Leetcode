class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 = {}
        tem = 0
        length = len(nums)
        for i in range(length):
            tem = nums[i]
            if not tem in dict1 or i - dict1[tem] > k:
                dict1[tem] = i
            else:
                return True
        return False
