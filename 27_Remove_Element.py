class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        while len(nums) - 1 >= x:
            if nums[x] == val:
                nums.pop(x)
            else:
                x += 1
        return x



