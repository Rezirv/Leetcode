class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            x = 1
            while x < len(nums):
                if nums[x - 1] < target and nums[x] > target:
                    return x
                else:
                    x += 1

