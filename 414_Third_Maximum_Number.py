class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        flag = 1
        my = nums[-1]
        index = 0
        while flag < 3 and abs(index) < len(nums):
            index -= 1
            if nums[index] < my:
                my = nums[index]
                flag += 1
        if flag >= 3:
            return nums[index]
        else:
            return nums[-1]

def thirdMax(self, nums: List[int]) -> int:
    l = sorted(set(nums))
    if len(l)<3:
        return l[-1]
    else:
        return l[-3]