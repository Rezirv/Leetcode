class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        else:
            x = 0
            while len(nums) - 1 >= x + 1:
                if nums[x] == nums[x + 1]:
                    nums.pop(x + 1)
                else:
                    x += 1
            return x + 1

