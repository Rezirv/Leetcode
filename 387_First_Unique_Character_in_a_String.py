class Solution:
    def firstUniqChar(self, s: str) -> int:
        nums = {}
        for i in s:
            if i in nums:
                nums[i] += 1
            else:
                nums[i] = 1
        for i, value in enumerate(s):
            if nums[value] == 1:
                return i
        return -1
