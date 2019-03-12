class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        if length == 1:
            return nums[0]
        for i in range(length):
            if i == 0 and nums[i] != nums[i + 1]:
                return nums[i]
            elif i == length - 1 and nums[i] != nums[i - 1]:
                return nums[i]
            elif nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
                return nums[i]

