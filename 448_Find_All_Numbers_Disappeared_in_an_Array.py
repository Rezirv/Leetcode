class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = [*range(1, len(nums) + 1)]
        for i in nums:
            r[i - 1] = 0
        for i in range(len(r) - 1, -1, -1):  # 在删除列表中的元素时防止索引异常
            if r[i] == 0:
                r.pop(i)
        return r
